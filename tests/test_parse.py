from __future__ import annotations

from pathlib import Path

from environment_interference.parse import parse_iw_scan, parse_iw_survey, parse_nmcli_scan, parse_scan_text


def _fixture(name: str) -> str:
    return (Path(__file__).parent / "fixtures" / name).read_text(encoding="utf-8")


def test_parse_iw_scan_extracts_records_from_both_bands() -> None:
    records = parse_iw_scan(_fixture("sample_scan.txt"))

    assert len(records) == 7
    assert records[0].ssid == "Lab_AP_24"
    assert records[0].channel == 1
    assert records[4].band == "5 GHz"
    assert records[4].channel == 36


def test_parse_iw_survey_extracts_busy_ratio_inputs() -> None:
    records = parse_iw_survey(_fixture("sample_survey.txt"))

    assert len(records) == 6
    assert records[1].in_use is True
    assert records[1].channel == 6
    assert records[1].busy_ratio == 0.54


def test_parse_nmcli_scan_extracts_records_from_both_bands() -> None:
    records = parse_nmcli_scan(_fixture("sample_nmcli_scan.txt"))

    assert len(records) == 5
    assert records[0].ssid == "Lab:AP:5G"
    assert records[0].channel == 36
    assert records[0].signal_dbm_estimated is True
    assert records[2].band == "5 GHz"
    assert records[3].band == "2.4 GHz"


def test_parse_scan_text_auto_detects_nmcli_fixture() -> None:
    records = parse_scan_text(_fixture("sample_nmcli_scan.txt"))

    assert len(records) == 5
    assert records[1].channel == 44
