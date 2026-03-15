from __future__ import annotations

import subprocess
from pathlib import Path

from .models import AnalysisReport, BandMetrics, ChannelMetrics, BssRecord


class ReportError(RuntimeError):
    pass


def write_report_files(
    report: AnalysisReport,
    *,
    output_dir: Path,
    report_name: str,
    write_pdf: bool = True,
) -> tuple[Path, Path | None]:
    output_dir.mkdir(parents=True, exist_ok=True)
    markdown_path = output_dir / f"{report_name}.md"
    pdf_path = output_dir / f"{report_name}.pdf"
    markdown_path.write_text(render_markdown(report), encoding="utf-8")
    if not write_pdf:
        return markdown_path, None
    _render_pdf(markdown_path, pdf_path)
    return markdown_path, pdf_path


def render_markdown(report: AnalysisReport) -> str:
    lines: list[str] = [
        "# Local Wi-Fi Environment Interference Report",
        "",
        f"- Generated at (UTC): `{report.generated_at_utc}`",
        f"- Source: `{report.source_description}`",
        f"- Location: `{report.location_label}`",
        f"- Strong-neighbor threshold: `{report.strong_rssi_threshold_dbm:.1f} dBm`",
        f"- Scan source: `{report.scan_path or 'live collection'}`",
        f"- Survey source: `{report.survey_path or 'not available'}`",
    ]
    if report.notes.strip():
        lines.append(f"- Notes: {report.notes.strip()}")
    lines.extend(["", "## Executive Summary", ""])
    for band in report.bands:
        recommended = ", ".join(str(channel) for channel in band.recommended_channels) or "n/a"
        lines.append(
            f"- **{band.band}**: `{band.ap_count}` APs, `{band.strong_ap_count}` strong neighbors, "
            f"recommended channels `{recommended}`."
        )
    for band in report.bands:
        lines.extend(["", f"## {band.band}", ""])
        lines.extend(_render_band_metrics(band))
        lines.extend(["", "### Channel Occupancy", ""])
        lines.extend(_render_channel_table(band.channel_metrics))
        lines.extend(["", "### Strongest Nearby APs", ""])
        lines.extend(_render_neighbors_table(band.strongest_neighbors))
        lines.extend(["", "### Interpretation", ""])
        lines.extend(_render_interpretation(band))
    lines.append("")
    return "\n".join(lines)


def _render_band_metrics(band: BandMetrics) -> list[str]:
    recommended = ", ".join(str(channel) for channel in band.recommended_channels) or "n/a"
    return [
        "| Metric | Value |",
        "| --- | --- |",
        f"| AP count | {band.ap_count} |",
        f"| Unique SSID count | {band.unique_ssid_count} |",
        f"| Strong-neighbor count | {band.strong_ap_count} |",
        f"| Median signal (dBm) | {_fmt_optional(band.median_signal_dbm, precision=2)} |",
        f"| Mean survey busy ratio | {_fmt_ratio(band.mean_survey_busy_ratio)} |",
        f"| Mean noise floor (dBm) | {_fmt_optional(band.mean_noise_dbm, precision=2)} |",
        f"| Recommended channels | {recommended} |",
    ]


def _render_channel_table(channel_metrics: tuple[ChannelMetrics, ...]) -> list[str]:
    lines = [
        "| Channel | APs | Unique SSIDs | Strong APs | Congestion score | Strongest signal | Survey busy | Noise |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for metric in channel_metrics:
        lines.append(
            f"| {metric.channel} | {metric.ap_count} | {metric.unique_ssid_count} | {metric.strong_ap_count} | "
            f"{metric.congestion_score:.3f} | {_fmt_optional(metric.strongest_signal_dbm, precision=1, suffix=' dBm')} | "
            f"{_fmt_ratio(metric.survey_busy_ratio)} | {_fmt_optional(metric.survey_noise_dbm, precision=1, suffix=' dBm')} |"
        )
    return lines


def _render_neighbors_table(neighbors: tuple[BssRecord, ...]) -> list[str]:
    if not neighbors:
        return ["No APs detected in this band."]
    lines = [
        "| SSID | BSSID | Channel | Signal | Last seen |",
        "| --- | --- | --- | --- | --- |",
    ]
    for record in neighbors:
        ssid = record.ssid or "<hidden>"
        lines.append(
            f"| {ssid} | `{record.bssid}` | {record.channel} | "
            f"{_fmt_optional(record.signal_dbm, precision=1, suffix=' dBm')} | "
            f"{_fmt_optional(record.last_seen_ms, precision=0, suffix=' ms')} |"
        )
    return lines


def _render_interpretation(band: BandMetrics) -> list[str]:
    lines: list[str] = []
    recommended = ", ".join(str(channel) for channel in band.recommended_channels) or "n/a"
    busiest = max(band.channel_metrics, key=lambda item: item.congestion_score, default=None)
    cleanest = min(
        band.channel_metrics,
        key=lambda item: (
            0 if _channel_has_observed_data(item) else 1,
            item.congestion_score,
            item.strong_ap_count,
            item.ap_count,
            2.0 if item.survey_busy_ratio is None else item.survey_busy_ratio,
            item.channel,
        ),
        default=None,
    )
    if busiest is not None:
        lines.append(
            f"- Highest modeled congestion is on channel `{busiest.channel}` "
            f"(score `{busiest.congestion_score:.3f}`)."
        )
    if cleanest is not None:
        lines.append(
            f"- Lowest modeled congestion is on channel `{cleanest.channel}` "
            f"(score `{cleanest.congestion_score:.3f}`)."
        )
    lines.append(f"- Recommended channels for experiments in this band: `{recommended}`.")
    if band.mean_survey_busy_ratio is None:
        lines.append("- Channel-survey utilization data was not available, so the assessment is based on neighboring AP presence and signal strength.")
    else:
        lines.append(
            f"- Mean channel busy ratio is `{_fmt_ratio(band.mean_survey_busy_ratio)}`, which helps separate true airtime pressure from simple AP count."
        )
    return lines


def _fmt_optional(value: float | int | None, *, precision: int, suffix: str = "") -> str:
    if value is None:
        return "n/a"
    if precision == 0:
        return f"{int(value)}{suffix}"
    return f"{float(value):.{precision}f}{suffix}"


def _fmt_ratio(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value * 100:.1f}%"


def _channel_has_observed_data(metric: ChannelMetrics) -> bool:
    return metric.ap_count > 0 or metric.survey_busy_ratio is not None or metric.survey_noise_dbm is not None


def _render_pdf(markdown_path: Path, pdf_path: Path) -> None:
    proc = subprocess.run(
        [
            "pandoc",
            str(markdown_path),
            "--pdf-engine=xelatex",
            "-V",
            "geometry:margin=1in",
            "-V",
            "mainfont=DejaVu Sans",
            "-o",
            str(pdf_path),
        ],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if proc.returncode != 0:
        stderr = proc.stderr.strip() or "unknown pandoc error"
        raise ReportError(f"failed to generate PDF report: {stderr}")
