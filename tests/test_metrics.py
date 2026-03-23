from __future__ import annotations

from pathlib import Path

from environment_interference.metrics import analyze_environment
from environment_interference.parse import parse_iw_scan, parse_iw_survey


def _fixture(name: str) -> str:
    return (Path(__file__).parent / "fixtures" / name).read_text(encoding="utf-8")


def test_analyze_environment_separates_bands_and_recommends_channels() -> None:
    report = analyze_environment(
        bss_records=parse_iw_scan(_fixture("sample_scan.txt")),
        survey_records=parse_iw_survey(_fixture("sample_survey.txt")),
        source_description="fixture",
        location_label="fixture-lab",
        notes="",
        scan_path="sample_scan.txt",
        survey_path="sample_survey.txt",
        strong_rssi_threshold_dbm=-67.0,
        collection_backend="iw",
        focus_band="5 GHz",
        focus_channel=36,
        focus_width_mhz=20,
    )

    band_24 = next(band for band in report.bands if band.band == "2.4 GHz")
    band_5 = next(band for band in report.bands if band.band == "5 GHz")

    assert band_24.ap_count == 4
    assert band_24.recommended_channels[0] == 11
    assert band_5.ap_count == 3
    assert band_5.recommended_channels[0] == 52
    assert report.focus_assessment is not None
    assert report.focus_assessment.channel == 36
    assert report.focus_assessment.inferred_interference_level in {"L2", "L3"}
