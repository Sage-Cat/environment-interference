from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from statistics import fmean, median

from .collect import collect_scan_text, collect_survey_text, detect_live_backend
from .metrics import analyze_environment
from .models import BssRecord
from .radio import band_label, five_ghz_block_label, same_5ghz_40mhz_pair, same_5ghz_80mhz_block
from .report import write_report_files
from .parse import parse_iw_survey, parse_scan_text


@dataclass(frozen=True)
class ScanSeriesSample:
    sample_index: int
    captured_at_utc: str
    scan_path: str
    bss_records: tuple[BssRecord, ...]


@dataclass(frozen=True)
class ScanSeriesSampleSummary:
    sample_index: int
    captured_at_utc: str
    scan_path: str
    total_ap_count: int
    band_24_ap_count: int
    band_5_ap_count: int
    focus_exact_ap_count: int
    focus_exact_strong_ap_count: int
    focus_overlap_ap_count: int
    focus_overlap_strong_ap_count: int
    focus_congestion_score: float
    focus_rank_in_band: int | None
    strongest_overlap_signal_dbm: float | None


@dataclass(frozen=True)
class FocusChannelSeriesMetrics:
    channel: int
    exact_presence_ratio: float
    exact_strong_presence_ratio: float
    overlap_presence_ratio: float
    overlap_strong_presence_ratio: float
    mean_exact_ap_count: float
    max_exact_ap_count: int
    mean_overlap_ap_count: float
    max_overlap_ap_count: int
    mean_congestion_score: float
    median_congestion_score: float
    max_congestion_score: float
    strongest_overlap_signal_dbm: float | None
    strongest_exact_signal_dbm: float | None


@dataclass(frozen=True)
class PersistentEmitter:
    bssid: str
    ssid: str
    channel: int
    observations: int
    presence_ratio: float
    strongest_signal_dbm: float | None
    median_signal_dbm: float | None


@dataclass(frozen=True)
class ScanSeriesSummary:
    generated_at_utc: str
    interface: str
    backend: str
    location_label: str
    notes: str
    focus_band: str
    focus_channel: int
    focus_width_mhz: int
    strong_rssi_threshold_dbm: float
    sample_count: int
    repeat_interval_s: float
    excluded_ssids: tuple[str, ...]
    excluded_bssids: tuple[str, ...]
    aggregate_report_markdown_path: str
    aggregate_report_pdf_path: str | None
    scan_series_paths: tuple[str, ...]
    unique_5ghz_bss_count: int
    unique_focus_block_bss_count: int
    exact_presence_ratio: float
    exact_strong_presence_ratio: float
    overlap_presence_ratio: float
    overlap_strong_presence_ratio: float
    mean_focus_congestion_score: float
    median_focus_congestion_score: float
    worst_focus_congestion_score: float
    median_focus_rank_in_band: float | None
    best_alternative_channels: tuple[int, ...]
    focus_block_channels: tuple[FocusChannelSeriesMetrics, ...]
    persistent_emitters: tuple[PersistentEmitter, ...]
    sample_summaries: tuple[ScanSeriesSampleSummary, ...]
    warnings: tuple[str, ...]


def collect_scan_series(
    *,
    interface: str,
    output_dir: Path,
    report_name: str,
    backend: str = "auto",
    repeat_count: int = 6,
    repeat_interval_s: float = 5.0,
) -> tuple[str, tuple[ScanSeriesSample, ...], str | None, str | None]:
    resolved_backend = detect_live_backend(backend)
    if repeat_count < 1:
        raise ValueError("repeat_count must be at least 1")
    output_dir.mkdir(parents=True, exist_ok=True)

    samples: list[ScanSeriesSample] = []
    combined_scan_lines: list[str] = []
    last_survey_text: str | None = None
    last_survey_path: str | None = None

    for sample_index in range(1, repeat_count + 1):
        captured_at_utc = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
        _, scan_text = collect_scan_text(interface, backend=resolved_backend)
        scan_path = output_dir / f"{report_name}.scan.{sample_index:02d}.txt"
        scan_path.write_text(scan_text, encoding="utf-8")
        bss_records = tuple(parse_scan_text(scan_text))
        samples.append(
            ScanSeriesSample(
                sample_index=sample_index,
                captured_at_utc=captured_at_utc,
                scan_path=str(scan_path),
                bss_records=bss_records,
            )
        )
        combined_scan_lines.extend(
            [
                f"# sample_index={sample_index}",
                f"# captured_at_utc={captured_at_utc}",
                scan_text.rstrip(),
                "",
            ]
        )
        if resolved_backend == "iw":
            survey_text = collect_survey_text(interface, backend=resolved_backend)
            if survey_text:
                survey_path = output_dir / f"{report_name}.survey.{sample_index:02d}.txt"
                survey_path.write_text(survey_text, encoding="utf-8")
                last_survey_text = survey_text
                last_survey_path = str(survey_path)
        if sample_index < repeat_count and repeat_interval_s > 0:
            time.sleep(repeat_interval_s)

    combined_scan_path = output_dir / f"{report_name}.scan.txt"
    combined_scan_path.write_text("\n".join(combined_scan_lines).rstrip() + "\n", encoding="utf-8")
    return resolved_backend, tuple(samples), str(combined_scan_path), last_survey_path


def collapse_series_bss_records(samples: tuple[ScanSeriesSample, ...]) -> list[BssRecord]:
    best_by_bssid: dict[str, BssRecord] = {}
    for sample in samples:
        for record in sample.bss_records:
            existing = best_by_bssid.get(record.bssid.lower())
            if existing is None or _record_sort_key(record) > _record_sort_key(existing):
                best_by_bssid[record.bssid.lower()] = record
    return list(best_by_bssid.values())


def analyze_scan_series(
    *,
    interface: str,
    backend: str,
    samples: tuple[ScanSeriesSample, ...],
    location_label: str,
    notes: str,
    scan_path: str,
    survey_path: str | None,
    strong_rssi_threshold_dbm: float,
    focus_band: str,
    focus_channel: int,
    focus_width_mhz: int,
    repeat_interval_s: float,
    exclude_ssids: tuple[str, ...] = (),
    exclude_bssids: tuple[str, ...] = (),
    output_dir: Path,
    report_name: str,
    write_pdf: bool = True,
) -> ScanSeriesSummary:
    if not samples:
        raise RuntimeError("no scan samples were collected")

    filtered_samples: list[ScanSeriesSample] = []
    for sample in samples:
        filtered_records = tuple(
            _filter_bss_records(sample.bss_records, exclude_ssids=exclude_ssids, exclude_bssids=exclude_bssids)
        )
        filtered_samples.append(
            ScanSeriesSample(
                sample_index=sample.sample_index,
                captured_at_utc=sample.captured_at_utc,
                scan_path=sample.scan_path,
                bss_records=filtered_records,
            )
        )

    collapsed_records = collapse_series_bss_records(tuple(filtered_samples))
    survey_records = parse_iw_survey(Path(survey_path).read_text(encoding="utf-8")) if survey_path else []
    aggregate_report = analyze_environment(
        bss_records=collapsed_records,
        survey_records=survey_records,
        source_description=(
            f"live {backend} repeated collection from interface {interface} "
            f"({len(samples)} scans, {repeat_interval_s:.1f} s interval)"
        ),
        location_label=location_label,
        notes=notes,
        scan_path=scan_path,
        survey_path=survey_path,
        strong_rssi_threshold_dbm=strong_rssi_threshold_dbm,
        collection_backend=backend,
        focus_band=focus_band,
        focus_channel=focus_channel,
        focus_width_mhz=focus_width_mhz,
        exclude_ssids=exclude_ssids,
        exclude_bssids=exclude_bssids,
    )
    aggregate_md_path, aggregate_pdf_path = write_report_files(
        aggregate_report,
        output_dir=output_dir,
        report_name=report_name,
        write_pdf=write_pdf,
    )

    sample_reports = [
        analyze_environment(
            bss_records=list(sample.bss_records),
            survey_records=[],
            source_description=f"sample {sample.sample_index}",
            location_label=location_label,
            notes=notes,
            scan_path=sample.scan_path,
            survey_path=None,
            strong_rssi_threshold_dbm=strong_rssi_threshold_dbm,
            collection_backend=backend,
            focus_band=focus_band,
            focus_channel=focus_channel,
            focus_width_mhz=focus_width_mhz,
        )
        for sample in filtered_samples
    ]

    focus_band_label = _normalize_focus_band(focus_band)
    focus_metrics_by_sample = [
        report.focus_assessment
        for report in sample_reports
        if report.focus_assessment is not None and report.focus_assessment.band == focus_band_label
    ]
    if len(focus_metrics_by_sample) != len(filtered_samples):
        raise RuntimeError("focus assessment was not available for every collected sample")

    channel_series_metrics = _build_channel_series_metrics(sample_reports=sample_reports, focus_band=focus_band_label)
    persistent_emitters = _build_persistent_emitters(
        samples=filtered_samples,
        focus_channel=focus_channel,
        focus_band=focus_band_label,
    )
    best_alternative_channels = tuple(
        metric.channel
        for metric in sorted(
            [metric for metric in channel_series_metrics if metric.channel != focus_channel],
            key=lambda item: (item.mean_congestion_score, item.overlap_presence_ratio, item.channel),
        )[:3]
    )

    sample_summaries = tuple(
        ScanSeriesSampleSummary(
            sample_index=sample.sample_index,
            captured_at_utc=sample.captured_at_utc,
            scan_path=sample.scan_path,
            total_ap_count=len(sample.bss_records),
            band_24_ap_count=sum(1 for record in sample.bss_records if record.band == "2.4 GHz"),
            band_5_ap_count=sum(1 for record in sample.bss_records if record.band == "5 GHz"),
            focus_exact_ap_count=focus.exact_ap_count,
            focus_exact_strong_ap_count=focus.exact_strong_ap_count,
            focus_overlap_ap_count=focus.overlap_ap_count,
            focus_overlap_strong_ap_count=focus.overlap_strong_ap_count,
            focus_congestion_score=focus.congestion_score or 0.0,
            focus_rank_in_band=focus.rank_in_band,
            strongest_overlap_signal_dbm=focus.strongest_overlap_signal_dbm,
        )
        for sample, focus in zip(filtered_samples, focus_metrics_by_sample, strict=True)
    )

    unique_5ghz_bss = {
        record.bssid.lower()
        for sample in filtered_samples
        for record in sample.bss_records
        if record.band == "5 GHz"
    }
    unique_focus_block_bss = {
        record.bssid.lower()
        for sample in filtered_samples
        for record in sample.bss_records
        if record.band == focus_band_label and _five_ghz_overlap(record.channel, focus_channel)
    }
    focus_congestion_scores = [float(focus.congestion_score or 0.0) for focus in focus_metrics_by_sample]
    focus_ranks = [focus.rank_in_band for focus in focus_metrics_by_sample if focus.rank_in_band is not None]

    summary = ScanSeriesSummary(
        generated_at_utc=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        interface=interface,
        backend=backend,
        location_label=location_label,
        notes=notes,
        focus_band=focus_band_label,
        focus_channel=focus_channel,
        focus_width_mhz=focus_width_mhz,
        strong_rssi_threshold_dbm=strong_rssi_threshold_dbm,
        sample_count=len(filtered_samples),
        repeat_interval_s=repeat_interval_s,
        excluded_ssids=tuple(exclude_ssids),
        excluded_bssids=tuple(exclude_bssids),
        aggregate_report_markdown_path=str(aggregate_md_path),
        aggregate_report_pdf_path=str(aggregate_pdf_path) if aggregate_pdf_path is not None else None,
        scan_series_paths=tuple(sample.scan_path for sample in filtered_samples),
        unique_5ghz_bss_count=len(unique_5ghz_bss),
        unique_focus_block_bss_count=len(unique_focus_block_bss),
        exact_presence_ratio=round(_ratio(sum(1 for focus in focus_metrics_by_sample if focus.exact_ap_count > 0), len(filtered_samples)), 4),
        exact_strong_presence_ratio=round(_ratio(sum(1 for focus in focus_metrics_by_sample if focus.exact_strong_ap_count > 0), len(filtered_samples)), 4),
        overlap_presence_ratio=round(_ratio(sum(1 for focus in focus_metrics_by_sample if focus.overlap_ap_count > 0), len(filtered_samples)), 4),
        overlap_strong_presence_ratio=round(_ratio(sum(1 for focus in focus_metrics_by_sample if focus.overlap_strong_ap_count > 0), len(filtered_samples)), 4),
        mean_focus_congestion_score=round(fmean(focus_congestion_scores), 4),
        median_focus_congestion_score=round(float(median(focus_congestion_scores)), 4),
        worst_focus_congestion_score=round(max(focus_congestion_scores), 4),
        median_focus_rank_in_band=round(float(median(focus_ranks)), 2) if focus_ranks else None,
        best_alternative_channels=best_alternative_channels,
        focus_block_channels=channel_series_metrics,
        persistent_emitters=persistent_emitters,
        sample_summaries=sample_summaries,
        warnings=aggregate_report.warnings,
    )

    series_md_path = output_dir / f"{report_name}.series.md"
    series_json_path = output_dir / f"{report_name}.series.json"
    series_md_path.write_text(render_series_markdown(summary), encoding="utf-8")
    series_json_path.write_text(json.dumps(asdict(summary), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return summary


def render_series_markdown(summary: ScanSeriesSummary) -> str:
    lines = [
        "# Repeated 5 GHz Environment Series Report",
        "",
        "## Objective",
        "",
        "This companion report summarizes repeated ambient Wi-Fi scans for the current 5 GHz cws-lab operating point. "
        "It is intended to support experiment-facing channel interpretation rather than a one-shot convenience snapshot.",
        "",
        "## Measurement Design",
        "",
        f"- Generated at (UTC): `{summary.generated_at_utc}`",
        f"- Interface: `{summary.interface}`",
        f"- Backend: `{summary.backend}`",
        f"- Location: `{summary.location_label}`",
        f"- Focus: `{summary.focus_band}` channel `{summary.focus_channel}` / `{summary.focus_width_mhz} MHz`",
        f"- Repeat count: `{summary.sample_count}`",
        f"- Inter-scan interval: `{summary.repeat_interval_s:.1f} s`",
        f"- Strong-neighbor threshold: `{summary.strong_rssi_threshold_dbm:.1f} dBm`",
        f"- Aggregate report: `{summary.aggregate_report_markdown_path}`",
    ]
    if summary.notes.strip():
        lines.append(f"- Notes: {summary.notes.strip()}")
    if summary.excluded_ssids or summary.excluded_bssids:
        lines.append(
            "- Exclusions before scoring: "
            f"SSIDs `{', '.join(summary.excluded_ssids) if summary.excluded_ssids else '-'}`, "
            f"BSSIDs `{', '.join(summary.excluded_bssids) if summary.excluded_bssids else '-'}`"
        )

    lines.extend(
        [
            "",
            "## Experiment-Facing Summary",
            "",
            f"- Unique 5 GHz BSS observed across series: `{summary.unique_5ghz_bss_count}`",
            f"- Unique focus-block (" + (five_ghz_block_label(summary.focus_channel) or "n/a") + f") BSS observed across series: `{summary.unique_focus_block_bss_count}`",
            f"- Focus exact-channel presence ratio: `{summary.exact_presence_ratio * 100:.1f}%`",
            f"- Focus exact strong-emitter presence ratio: `{summary.exact_strong_presence_ratio * 100:.1f}%`",
            f"- Focus overlap presence ratio: `{summary.overlap_presence_ratio * 100:.1f}%`",
            f"- Focus overlap strong-emitter presence ratio: `{summary.overlap_strong_presence_ratio * 100:.1f}%`",
            f"- Mean / median / worst focus congestion score: `{summary.mean_focus_congestion_score:.3f}` / `{summary.median_focus_congestion_score:.3f}` / `{summary.worst_focus_congestion_score:.3f}`",
            f"- Median focus rank in band: `{summary.median_focus_rank_in_band if summary.median_focus_rank_in_band is not None else 'n/a'}`",
            f"- Best repeated-scan alternatives: `{', '.join(str(channel) for channel in summary.best_alternative_channels) or 'n/a'}`",
        ]
    )

    lines.extend(
        [
            "",
            "## Focus-Block Channel Stability",
            "",
            "| Channel | Exact Presence | Exact Strong | Overlap Presence | Overlap Strong | Mean Exact APs | Mean Overlap APs | Mean Congestion | Max Congestion | Strongest Overlap |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for metric in summary.focus_block_channels:
        lines.append(
            f"| {metric.channel} | {metric.exact_presence_ratio * 100:.1f}% | {metric.exact_strong_presence_ratio * 100:.1f}% | "
            f"{metric.overlap_presence_ratio * 100:.1f}% | {metric.overlap_strong_presence_ratio * 100:.1f}% | "
            f"{metric.mean_exact_ap_count:.2f} | {metric.mean_overlap_ap_count:.2f} | {metric.mean_congestion_score:.3f} | {metric.max_congestion_score:.3f} | "
            f"{_fmt_optional(metric.strongest_overlap_signal_dbm, suffix=' dBm')} |"
        )

    lines.extend(["", "## Persistent 5 GHz Focus-Block Emitters", ""])
    if summary.persistent_emitters:
        lines.extend(
            [
                "| SSID | BSSID | Channel | Observations | Presence | Strongest | Median |",
                "| --- | --- | ---: | ---: | ---: | ---: | ---: |",
            ]
        )
        for emitter in summary.persistent_emitters:
            lines.append(
                f"| {emitter.ssid or '<hidden>'} | `{emitter.bssid}` | {emitter.channel} | {emitter.observations} | "
                f"{emitter.presence_ratio * 100:.1f}% | {_fmt_optional(emitter.strongest_signal_dbm, suffix=' dBm')} | "
                f"{_fmt_optional(emitter.median_signal_dbm, suffix=' dBm')} |"
            )
    else:
        lines.append("No persistent focus-block emitters were observed after filtering.")

    lines.extend(
        [
            "",
            "## Per-Sample Trace",
            "",
            "| Sample | Captured At (UTC) | 2.4 GHz APs | 5 GHz APs | Focus Exact | Focus Overlap | Focus Strong Overlap | Focus Congestion | Focus Rank |",
            "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for sample in summary.sample_summaries:
        lines.append(
            f"| {sample.sample_index} | {sample.captured_at_utc} | {sample.band_24_ap_count} | {sample.band_5_ap_count} | "
            f"{sample.focus_exact_ap_count} | {sample.focus_overlap_ap_count} | {sample.focus_overlap_strong_ap_count} | "
            f"{sample.focus_congestion_score:.3f} | {sample.focus_rank_in_band if sample.focus_rank_in_band is not None else 'n/a'} |"
        )

    lines.extend(["", "## Interpretation", ""])
    if summary.overlap_strong_presence_ratio >= 0.5 or summary.worst_focus_congestion_score >= 1.0:
        lines.append(
            "- The focus block shows repeated external occupancy strong enough that the current 5 GHz operating point should be treated as an active interference surface, not a clean baseline."
        )
    else:
        lines.append(
            "- The focus block did not show sustained strong overlap across the repeated scans, so the current 5 GHz operating point remains a plausible baseline candidate."
        )
    if summary.best_alternative_channels:
        lines.append(
            f"- The lowest repeated-scan alternatives were `{', '.join(str(channel) for channel in summary.best_alternative_channels)}`; use them only if the experiment design permits a channel move."
        )
    if summary.warnings:
        lines.append("- Methodological warnings inherited from the aggregate report:")
        for warning in summary.warnings:
            lines.append(f"  - {warning}")
    return "\n".join(lines) + "\n"


def _build_channel_series_metrics(*, sample_reports: list, focus_band: str) -> tuple[FocusChannelSeriesMetrics, ...]:
    per_channel: dict[int, list] = {}
    for report in sample_reports:
        band_metrics = next(band for band in report.bands if band.band == focus_band)
        for channel_metric in band_metrics.channel_metrics:
            per_channel.setdefault(channel_metric.channel, []).append(channel_metric)

    metrics: list[FocusChannelSeriesMetrics] = []
    sample_count = len(sample_reports)
    for channel in sorted(per_channel):
        items = per_channel[channel]
        metrics.append(
            FocusChannelSeriesMetrics(
                channel=channel,
                exact_presence_ratio=round(_ratio(sum(1 for item in items if item.ap_count > 0), sample_count), 4),
                exact_strong_presence_ratio=round(_ratio(sum(1 for item in items if item.exact_strong_ap_count > 0), sample_count), 4),
                overlap_presence_ratio=round(_ratio(sum(1 for item in items if item.overlap_ap_count > 0), sample_count), 4),
                overlap_strong_presence_ratio=round(_ratio(sum(1 for item in items if item.overlap_strong_ap_count > 0), sample_count), 4),
                mean_exact_ap_count=round(fmean(item.ap_count for item in items), 4),
                max_exact_ap_count=max(item.ap_count for item in items),
                mean_overlap_ap_count=round(fmean(item.overlap_ap_count for item in items), 4),
                max_overlap_ap_count=max(item.overlap_ap_count for item in items),
                mean_congestion_score=round(fmean(item.congestion_score for item in items), 4),
                median_congestion_score=round(float(median(item.congestion_score for item in items)), 4),
                max_congestion_score=round(max(item.congestion_score for item in items), 4),
                strongest_overlap_signal_dbm=max(
                    (item.strongest_signal_dbm for item in items if item.strongest_signal_dbm is not None),
                    default=None,
                ),
                strongest_exact_signal_dbm=max(
                    (item.strongest_exact_signal_dbm for item in items if item.strongest_exact_signal_dbm is not None),
                    default=None,
                ),
            )
        )
    return tuple(metrics)


def _build_persistent_emitters(
    *,
    samples: list[ScanSeriesSample],
    focus_channel: int,
    focus_band: str,
) -> tuple[PersistentEmitter, ...]:
    sample_count = len(samples)
    seen: dict[str, list[BssRecord]] = {}
    seen_samples: dict[str, set[int]] = {}
    for sample in samples:
        for record in sample.bss_records:
            if record.band != focus_band:
                continue
            if not _five_ghz_overlap(record.channel, focus_channel):
                continue
            key = record.bssid.lower()
            seen.setdefault(key, []).append(record)
            seen_samples.setdefault(key, set()).add(sample.sample_index)

    emitters: list[PersistentEmitter] = []
    for key, records in seen.items():
        observations = len(seen_samples[key])
        strongest = max((record.signal_dbm for record in records if record.signal_dbm is not None), default=None)
        signal_values = [record.signal_dbm for record in records if record.signal_dbm is not None]
        emitters.append(
            PersistentEmitter(
                bssid=key,
                ssid=records[0].ssid,
                channel=records[0].channel,
                observations=observations,
                presence_ratio=round(_ratio(observations, sample_count), 4),
                strongest_signal_dbm=strongest,
                median_signal_dbm=round(float(median(signal_values)), 2) if signal_values else None,
            )
        )
    emitters.sort(key=lambda item: (-item.presence_ratio, -(item.strongest_signal_dbm or -999.0), item.channel, item.bssid))
    return tuple(emitters[:8])


def _five_ghz_overlap(channel: int, focus_channel: int) -> bool:
    return (
        channel == focus_channel
        or same_5ghz_40mhz_pair(channel, focus_channel)
        or same_5ghz_80mhz_block(channel, focus_channel)
    )


def _record_sort_key(record: BssRecord) -> tuple[float, int]:
    signal = record.signal_dbm if record.signal_dbm is not None else -999.0
    return (signal, record.last_seen_ms or 0)


def _filter_bss_records(
    records: tuple[BssRecord, ...],
    *,
    exclude_ssids: tuple[str, ...],
    exclude_bssids: tuple[str, ...],
) -> list[BssRecord]:
    excluded_ssids = {item for item in exclude_ssids if item}
    excluded_bssids = {item.lower() for item in exclude_bssids if item}
    return [
        record
        for record in records
        if record.ssid not in excluded_ssids and record.bssid.lower() not in excluded_bssids
    ]


def _ratio(numerator: int, denominator: int) -> float:
    if denominator <= 0:
        return 0.0
    return numerator / denominator


def _normalize_focus_band(value: str) -> str:
    normalized = value.strip().lower().replace(" ", "")
    if normalized in {"5", "5ghz"}:
        return "5 GHz"
    if normalized in {"24", "2.4", "24ghz", "2.4ghz"}:
        return "2.4 GHz"
    return value


def _fmt_optional(value: float | None, *, suffix: str = "") -> str:
    if value is None:
        return "n/a"
    return f"{value:.1f}{suffix}"
