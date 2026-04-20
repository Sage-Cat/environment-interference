from __future__ import annotations

from pathlib import Path

from environment_interference.models import BssRecord
from environment_interference.series import (
    ScanSeriesSample,
    analyze_scan_series,
    collapse_series_bss_records,
)


def _record(bssid: str, ssid: str, channel: int, signal_dbm: float) -> BssRecord:
    return BssRecord(
        bssid=bssid,
        ssid=ssid,
        freq_mhz=5000 + (channel * 5),
        channel=channel,
        signal_dbm=signal_dbm,
        last_seen_ms=None,
        signal_dbm_estimated=False,
    )


def test_collapse_series_bss_records_keeps_strongest_seen_signal() -> None:
    samples = (
        ScanSeriesSample(1, "2026-04-20T12:00:00Z", "scan1.txt", (_record("aa:aa:aa:aa:aa:aa", "n1", 40, -70.0),)),
        ScanSeriesSample(2, "2026-04-20T12:00:05Z", "scan2.txt", (_record("aa:aa:aa:aa:aa:aa", "n1", 40, -61.0),)),
    )

    collapsed = collapse_series_bss_records(samples)

    assert len(collapsed) == 1
    assert collapsed[0].signal_dbm == -61.0


def test_analyze_scan_series_builds_focus_presence_and_alternatives(tmp_path: Path) -> None:
    samples = (
        ScanSeriesSample(
            1,
            "2026-04-20T12:00:00Z",
            "scan1.txt",
            (
                _record("11:11:11:11:11:11", "cwslab-exp1-main-5g", 36, -48.0),
                _record("22:22:22:22:22:22", "neighbor-40", 40, -61.0),
                _record("33:33:33:33:33:33", "neighbor-52", 52, -82.0),
            ),
        ),
        ScanSeriesSample(
            2,
            "2026-04-20T12:00:05Z",
            "scan2.txt",
            (
                _record("11:11:11:11:11:11", "cwslab-exp1-main-5g", 36, -49.0),
                _record("22:22:22:22:22:22", "neighbor-40", 40, -64.0),
                _record("33:33:33:33:33:33", "neighbor-52", 52, -80.0),
            ),
        ),
        ScanSeriesSample(
            3,
            "2026-04-20T12:00:10Z",
            "scan3.txt",
            (
                _record("11:11:11:11:11:11", "cwslab-exp1-main-5g", 36, -50.0),
                _record("44:44:44:44:44:44", "neighbor-36", 36, -72.0),
                _record("22:22:22:22:22:22", "neighbor-40", 40, -62.0),
            ),
        ),
    )

    summary = analyze_scan_series(
        interface="wlp3s0",
        backend="nmcli",
        samples=samples,
        location_label="Fixture lab",
        notes="",
        scan_path="series.scan.txt",
        survey_path=None,
        strong_rssi_threshold_dbm=-67.0,
        focus_band="5ghz",
        focus_channel=36,
        focus_width_mhz=20,
        repeat_interval_s=5.0,
        exclude_ssids=("cwslab-exp1-main-5g",),
        exclude_bssids=(),
        output_dir=tmp_path,
        report_name="fixture_series",
        write_pdf=False,
    )

    assert summary.sample_count == 3
    assert round(summary.exact_presence_ratio, 4) == round(1 / 3, 4)
    assert summary.overlap_presence_ratio == 1.0
    assert summary.persistent_emitters[0].bssid == "22:22:22:22:22:22"
    assert 36 not in summary.best_alternative_channels
    assert any(channel >= 52 for channel in summary.best_alternative_channels)
    assert (tmp_path / "fixture_series.md").is_file()
    assert (tmp_path / "fixture_series.series.md").is_file()
    assert (tmp_path / "fixture_series.series.json").is_file()
