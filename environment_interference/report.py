from __future__ import annotations

import shutil
import subprocess
import textwrap
from pathlib import Path

from .models import AnalysisReport, BandMetrics, ChannelMetrics, FocusChannelAssessment, BssRecord


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
        "# Scientific Wi-Fi Environment Interference Report",
        "",
        "## Abstract",
        "",
        _render_abstract(report),
        "",
        "## Measurement Setup",
        "",
        f"- Generated at (UTC): `{report.generated_at_utc}`",
        f"- Source: `{report.source_description}`",
        f"- Collection backend: `{report.collection_backend}`",
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
            f"- **{band.band}**: `{band.ap_count}` APs observed, `{band.strong_ap_count}` strong emitters, "
            f"recommended channels `{recommended}`."
        )
    if report.focus_assessment is not None:
        focus = report.focus_assessment
        lines.append(
            f"- **Focus assessment**: `{focus.band}` channel `{focus.channel}` / `{focus.channel_width_mhz} MHz` "
            f"maps to interference level `{focus.inferred_interference_level}` and radio-load level "
            f"`{focus.inferred_radio_load_level}`."
        )

    if report.focus_assessment is not None:
        lines.extend(["", f"## {report.focus_assessment.band} Experiment Focus", ""])
        lines.extend(_render_focus_assessment(report.focus_assessment))

    lines.extend(["", "## Observed Band Results", ""])
    for band in report.bands:
        lines.extend(["", f"### {band.band}", ""])
        lines.extend(_render_band_metrics(band))
        lines.extend(["", "#### Channel Occupancy", ""])
        lines.extend(_render_channel_table(band.channel_metrics))
        lines.extend(["", "#### Strongest Nearby APs", ""])
        lines.extend(_render_neighbors_table(band.strongest_neighbors))
        lines.extend(["", "#### Interpretation", ""])
        lines.extend(_render_interpretation(band))

    lines.extend(["", "## Methodological Limitations", ""])
    if report.warnings:
        lines.extend(f"- {warning}" for warning in report.warnings)
    else:
        lines.append("- No major methodological warnings were recorded.")
    lines.append("")
    return "\n".join(lines)


def _render_abstract(report: AnalysisReport) -> str:
    if report.focus_assessment is None:
        return (
            "This report summarizes local 2.4 GHz and 5 GHz interference conditions for Wi-Fi sensing preparation. "
            "It provides band-level congestion estimates, strongest-neighbor summaries, and channel recommendations."
        )
    focus = report.focus_assessment
    recommended = ", ".join(str(channel) for channel in focus.recommended_channels) or "n/a"
    return (
        f"This report characterizes the current laboratory Wi-Fi field with emphasis on `{focus.band}` "
        f"channel `{focus.channel}` at `{focus.channel_width_mhz} MHz`, which is the planned operating point for "
        f"`cws-lab`. The target channel currently maps to interference level `{focus.inferred_interference_level}` "
        f"and radio-load level `{focus.inferred_radio_load_level}`, while the lowest modeled alternatives in-band are "
        f"`{recommended}`."
    )


def _render_focus_assessment(focus: FocusChannelAssessment) -> list[str]:
    recommended = ", ".join(str(channel) for channel in focus.recommended_channels) or "n/a"
    readiness_text = {
        "ready_with_documented_baseline": "The channel is suitable for baseline cws-lab work if the measured baseline is documented and repeated before each run.",
        "usable_with_controls": "The channel is usable, but the experiment should log radio conditions, keep channel width fixed, and treat the baseline as at least lightly loaded.",
        "retune_or_isolate_before_cwslab": "The channel should be retuned or the environment should be isolated before claiming a clean cws-lab baseline.",
    }[focus.readiness]
    lines = [
        "| Metric | Value |",
        "| --- | --- |",
        f"| Focus channel | {focus.channel} |",
        f"| Focus width | {focus.channel_width_mhz} MHz |",
        f"| Rank within band | {focus.rank_in_band if focus.rank_in_band is not None else 'n/a'} |",
        f"| 5 GHz block | {focus.block_label or 'n/a'} |",
        f"| Exact-channel APs | {focus.exact_ap_count} |",
        f"| Exact-channel strong APs | {focus.exact_strong_ap_count} |",
        f"| Overlapping / same-block APs | {focus.overlap_ap_count} |",
        f"| Overlapping / same-block strong APs | {focus.overlap_strong_ap_count} |",
        f"| Strongest exact signal | {_fmt_optional(focus.strongest_exact_signal_dbm, precision=1, suffix=' dBm')} |",
        f"| Strongest overlap signal | {_fmt_optional(focus.strongest_overlap_signal_dbm, precision=1, suffix=' dBm')} |",
        f"| Congestion score | {_fmt_optional(focus.congestion_score, precision=3)} |",
        f"| Survey busy ratio | {_fmt_ratio(focus.survey_busy_ratio)} |",
        f"| Inferred interference level | {focus.inferred_interference_level} |",
        f"| Inferred radio-load level | {focus.inferred_radio_load_level} |",
        f"| Recommended in-band channels | {recommended} |",
        "",
        "Interpretation:",
        f"- {readiness_text}",
        f"- The current channel state should be treated as `{focus.inferred_interference_level}` for interference and `{focus.inferred_radio_load_level}` for radio loading when mapping the lab to `L0-L2` cws-lab assumptions.",
    ]
    if focus.inferred_interference_level == "L0" and focus.inferred_radio_load_level == "L0":
        lines.append("- This channel is close to a clean `L0` baseline.")
    elif focus.inferred_interference_level in {"L1", "L2"} or focus.inferred_radio_load_level in {"L1", "L2"}:
        lines.append("- This channel should not be described as a clean `L0` baseline without extra isolation or a channel move.")
    else:
        lines.append("- This channel exceeds the intended `L0-L2` preparation window and should be considered unstable for baseline work.")
    return lines


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
        "| Channel | Exact APs | Exact Strong | Overlap APs | Overlap Strong | Congestion | Strongest Exact | Strongest Overlap | Survey Busy | Noise |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for metric in channel_metrics:
        lines.append(
            f"| {metric.channel} | {metric.ap_count} | {metric.exact_strong_ap_count} | {metric.overlap_ap_count} | "
            f"{metric.overlap_strong_ap_count} | {metric.congestion_score:.3f} | "
            f"{_fmt_optional(metric.strongest_exact_signal_dbm, precision=1, suffix=' dBm')} | "
            f"{_fmt_optional(metric.strongest_signal_dbm, precision=1, suffix=' dBm')} | "
            f"{_fmt_ratio(metric.survey_busy_ratio)} | "
            f"{_fmt_optional(metric.survey_noise_dbm, precision=1, suffix=' dBm')} |"
        )
    return lines


def _render_neighbors_table(neighbors: tuple[BssRecord, ...]) -> list[str]:
    if not neighbors:
        return ["No APs detected in this band."]
    lines = [
        "| SSID | BSSID | Channel | Signal | Estimated | Last seen |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for record in neighbors:
        ssid = record.ssid or "<hidden>"
        lines.append(
            f"| {ssid} | `{record.bssid}` | {record.channel} | "
            f"{_fmt_optional(record.signal_dbm, precision=1, suffix=' dBm')} | "
            f"{'yes' if record.signal_dbm_estimated else 'no'} | "
            f"{_fmt_optional(record.last_seen_ms, precision=0, suffix=' ms')} |"
        )
    return lines


def _render_interpretation(band: BandMetrics) -> list[str]:
    lines: list[str] = []
    recommended = ", ".join(str(channel) for channel in band.recommended_channels) or "n/a"
    busiest = max(band.channel_metrics, key=lambda item: item.congestion_score, default=None)
    cleanest = min(band.channel_metrics, key=lambda item: (item.congestion_score, item.channel), default=None)
    if busiest is not None:
        lines.append(
            f"- Highest modeled congestion is on channel `{busiest.channel}` with score `{busiest.congestion_score:.3f}`."
        )
    if cleanest is not None:
        lines.append(
            f"- Lowest modeled congestion is on channel `{cleanest.channel}` with score `{cleanest.congestion_score:.3f}`."
        )
    lines.append(f"- Recommended channels for experiments in this band: `{recommended}`.")
    if band.mean_survey_busy_ratio is None:
        lines.append("- Airtime utilization counters were not available, so interpretation is driven mainly by neighboring AP presence and signal strength.")
    else:
        lines.append(
            f"- Mean channel busy ratio is `{_fmt_ratio(band.mean_survey_busy_ratio)}`, which separates actual airtime pressure from simple AP density."
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


def _render_pdf(markdown_path: Path, pdf_path: Path) -> None:
    if shutil.which("pandoc") and shutil.which("xelatex"):
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
        return
    _render_simple_pdf(markdown_path.read_text(encoding="utf-8"), pdf_path)


def _render_simple_pdf(markdown_text: str, pdf_path: Path) -> None:
    wrapped_lines = _markdown_to_pdf_lines(markdown_text)
    pages: list[list[str]] = []
    current: list[str] = []
    for line in wrapped_lines:
        current.append(line)
        if len(current) >= 48:
            pages.append(current)
            current = []
    if current or not pages:
        pages.append(current)

    objects: list[bytes] = []
    page_object_numbers: list[int] = []
    content_object_numbers: list[int] = []

    objects.append(b"<< /Type /Catalog /Pages 2 0 R >>")
    objects.append(b"")
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")

    for page_lines in pages:
        content_object_numbers.append(len(objects) + 1)
        stream = _pdf_page_stream(page_lines)
        objects.append(
            f"<< /Length {len(stream)} >>\nstream\n".encode("latin-1") + stream + b"\nendstream"
        )
        page_object_numbers.append(len(objects) + 1)
        objects.append(
            (
                "<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
                f"/Resources << /Font << /F1 3 0 R >> >> /Contents {content_object_numbers[-1]} 0 R >>"
            ).encode("latin-1")
        )

    kids = " ".join(f"{number} 0 R" for number in page_object_numbers)
    objects[1] = f"<< /Type /Pages /Kids [{kids}] /Count {len(page_object_numbers)} >>".encode("latin-1")

    pdf = bytearray()
    pdf.extend(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for index, obj in enumerate(objects, start=1):
        offsets.append(len(pdf))
        pdf.extend(f"{index} 0 obj\n".encode("latin-1"))
        pdf.extend(obj)
        pdf.extend(b"\nendobj\n")

    xref_start = len(pdf)
    pdf.extend(f"xref\n0 {len(objects) + 1}\n".encode("latin-1"))
    pdf.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        pdf.extend(f"{offset:010d} 00000 n \n".encode("latin-1"))
    pdf.extend(
        (
            f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref_start}\n%%EOF\n"
        ).encode("latin-1")
    )
    pdf_path.write_bytes(bytes(pdf))


def _markdown_to_pdf_lines(markdown_text: str) -> list[str]:
    lines: list[str] = []
    for raw_line in markdown_text.splitlines():
        stripped = raw_line.strip()
        if not stripped:
            lines.append("")
            continue
        if stripped.startswith("|"):
            stripped = " ".join(part.strip() for part in stripped.strip("|").split("|"))
        stripped = stripped.lstrip("#").strip()
        wrapped = textwrap.wrap(stripped, width=92) or [""]
        lines.extend(wrapped)
    return lines


def _pdf_page_stream(lines: list[str]) -> bytes:
    escaped_lines = [_pdf_escape(line) for line in lines]
    commands = ["BT", "/F1 10 Tf", "14 TL", "54 760 Td"]
    first = True
    for line in escaped_lines:
        if first:
            commands.append(f"({line}) Tj")
            first = False
        else:
            commands.append(f"T* ({line}) Tj")
    commands.append("ET")
    return "\n".join(commands).encode("latin-1", "replace")


def _pdf_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
