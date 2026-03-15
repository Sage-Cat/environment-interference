from __future__ import annotations

from dataclasses import dataclass

from .radio import band_label


@dataclass(frozen=True)
class BssRecord:
    bssid: str
    ssid: str
    freq_mhz: int
    channel: int
    signal_dbm: float | None
    last_seen_ms: int | None

    @property
    def band(self) -> str:
        return band_label(self.freq_mhz)


@dataclass(frozen=True)
class SurveyRecord:
    freq_mhz: int
    channel: int
    noise_dbm: float | None
    active_ms: int | None
    busy_ms: int | None
    receive_ms: int | None
    transmit_ms: int | None
    in_use: bool = False

    @property
    def band(self) -> str:
        return band_label(self.freq_mhz)

    @property
    def busy_ratio(self) -> float | None:
        if self.active_ms is None or self.busy_ms is None or self.active_ms <= 0:
            return None
        return self.busy_ms / self.active_ms


@dataclass(frozen=True)
class ChannelMetrics:
    channel: int
    band: str
    ap_count: int
    unique_ssid_count: int
    strong_ap_count: int
    congestion_score: float
    strongest_signal_dbm: float | None
    survey_busy_ratio: float | None
    survey_noise_dbm: float | None


@dataclass(frozen=True)
class BandMetrics:
    band: str
    ap_count: int
    unique_ssid_count: int
    strong_ap_count: int
    median_signal_dbm: float | None
    mean_survey_busy_ratio: float | None
    mean_noise_dbm: float | None
    recommended_channels: tuple[int, ...]
    channel_metrics: tuple[ChannelMetrics, ...]
    strongest_neighbors: tuple[BssRecord, ...]


@dataclass(frozen=True)
class AnalysisReport:
    generated_at_utc: str
    source_description: str
    location_label: str
    notes: str
    scan_path: str | None
    survey_path: str | None
    strong_rssi_threshold_dbm: float
    bands: tuple[BandMetrics, ...]

