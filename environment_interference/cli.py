from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

from .collect import CollectionError, collect_scan_text, collect_survey_text, detect_live_backend
from .metrics import analyze_environment
from .parse import parse_iw_survey, parse_scan_text
from .report import ReportError, write_report_files


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Collect and analyze local 2.4 GHz / 5 GHz Wi-Fi interference conditions.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    collect_parser = subparsers.add_parser("collect", help="Collect raw iw scan/survey text files.")
    collect_parser.add_argument("--interface", required=True, help="Wireless interface, for example wlan0.")
    collect_parser.add_argument(
        "--backend",
        choices=("auto", "iw", "nmcli"),
        default="auto",
        help="Live scanner backend (default: auto).",
    )
    collect_parser.add_argument("--output-dir", default="out/raw", help="Output directory for raw text files.")
    collect_parser.add_argument("--prefix", default=None, help="Raw capture filename prefix.")
    collect_parser.set_defaults(func=_cmd_collect)

    analyze_parser = subparsers.add_parser("analyze", help="Generate Markdown and PDF interference reports.")
    source_group = analyze_parser.add_mutually_exclusive_group(required=True)
    source_group.add_argument("--interface", help="Collect live data from this wireless interface.")
    source_group.add_argument("--scan-file", help="Use an existing iw scan text file.")
    analyze_parser.add_argument(
        "--backend",
        choices=("auto", "iw", "nmcli"),
        default="auto",
        help="Live scanner backend for --interface mode (default: auto).",
    )
    analyze_parser.add_argument("--survey-file", help="Optional survey dump text file.")
    analyze_parser.add_argument("--output-dir", default="out/reports", help="Directory for report artifacts.")
    analyze_parser.add_argument("--report-name", default=None, help="Base name for Markdown/PDF output files.")
    analyze_parser.add_argument("--location-label", default="unspecified location", help="Human-readable experiment site.")
    analyze_parser.add_argument("--notes", default="", help="Free-form notes for the report.")
    analyze_parser.add_argument(
        "--strong-rssi-threshold-dbm",
        type=float,
        default=-67.0,
        help="Threshold for strong neighboring APs (default: -67 dBm).",
    )
    analyze_parser.add_argument("--focus-band", default="5ghz", help="Experiment focus band, for example 5ghz.")
    analyze_parser.add_argument("--focus-channel", type=int, default=36, help="Experiment focus channel (default: 36).")
    analyze_parser.add_argument("--focus-width-mhz", type=int, default=20, help="Experiment focus channel width (default: 20).")
    analyze_parser.add_argument(
        "--exclude-ssid",
        action="append",
        default=[],
        help="SSID to exclude before interference scoring. May be repeated.",
    )
    analyze_parser.add_argument(
        "--exclude-bssid",
        action="append",
        default=[],
        help="BSSID to exclude before interference scoring. May be repeated.",
    )
    analyze_parser.add_argument("--skip-pdf", action="store_true", help="Write Markdown only.")
    analyze_parser.set_defaults(func=_cmd_analyze)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args))
    except (CollectionError, ReportError, RuntimeError, ValueError) as exc:
        print(f"Error: {exc}")
        return 2


def _cmd_collect(args: argparse.Namespace) -> int:
    output_dir = Path(args.output_dir)
    prefix = args.prefix or _default_prefix("raw")
    output_dir.mkdir(parents=True, exist_ok=True)
    scan_path = output_dir / f"{prefix}.scan.txt"
    survey_path = output_dir / f"{prefix}.survey.txt"

    backend, scan_text = collect_scan_text(args.interface, backend=args.backend)
    survey_text = collect_survey_text(args.interface, backend=backend)

    scan_path.write_text(scan_text, encoding="utf-8")
    print(f"backend: {backend}")
    print(f"scan: {scan_path}")
    if survey_text:
        survey_path.write_text(survey_text, encoding="utf-8")
        print(f"survey: {survey_path}")
    else:
        print("survey: not available")
    return 0


def _cmd_analyze(args: argparse.Namespace) -> int:
    output_dir = Path(args.output_dir)
    report_name = args.report_name or _default_prefix("environment_interference")
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.interface:
        backend = detect_live_backend(args.backend)
        backend, scan_text = collect_scan_text(args.interface, backend=backend)
        survey_text = collect_survey_text(args.interface, backend=backend)
        scan_path = output_dir / f"{report_name}.scan.txt"
        survey_path = output_dir / f"{report_name}.survey.txt"
        scan_path.write_text(scan_text, encoding="utf-8")
        if survey_text:
            survey_path.write_text(survey_text, encoding="utf-8")
            survey_path_str = str(survey_path)
        else:
            survey_path_str = None
        scan_path_str = str(scan_path)
        source_description = f"live {backend} collection from interface {args.interface}"
    else:
        scan_path = Path(args.scan_file)
        scan_text = scan_path.read_text(encoding="utf-8")
        if args.survey_file:
            survey_path = Path(args.survey_file)
            survey_text = survey_path.read_text(encoding="utf-8")
            survey_path_str = str(survey_path)
        else:
            survey_text = None
            survey_path_str = None
        scan_path_str = str(scan_path)
        backend = "file"
        source_description = "offline analysis from saved scan text files"

    bss_records = parse_scan_text(scan_text)
    if not bss_records:
        raise RuntimeError("no BSS records parsed from scan input")
    survey_records = parse_iw_survey(survey_text or "")

    report = analyze_environment(
        bss_records=bss_records,
        survey_records=survey_records,
        source_description=source_description,
        location_label=args.location_label,
        notes=args.notes,
        scan_path=scan_path_str,
        survey_path=survey_path_str,
        strong_rssi_threshold_dbm=args.strong_rssi_threshold_dbm,
        collection_backend=backend,
        focus_band=args.focus_band,
        focus_channel=args.focus_channel,
        focus_width_mhz=args.focus_width_mhz,
        exclude_ssids=tuple(args.exclude_ssid),
        exclude_bssids=tuple(args.exclude_bssid),
    )
    markdown_path, pdf_path = write_report_files(
        report,
        output_dir=output_dir,
        report_name=report_name,
        write_pdf=not args.skip_pdf,
    )
    print(f"backend: {backend}")
    print(f"markdown: {markdown_path}")
    print(f"pdf: {pdf_path if pdf_path is not None else 'skipped'}")
    return 0


def _default_prefix(prefix: str) -> str:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{stamp}"


if __name__ == "__main__":
    raise SystemExit(main())
