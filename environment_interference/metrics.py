from __future__ import annotations

from datetime import datetime, timezone
from statistics import fmean, median

from .models import AnalysisReport, BandMetrics, BssRecord, ChannelMetrics, SurveyRecord

_COMMON_24_CHANNELS = (1, 6, 11)
_COMMON_5_CHANNELS = (36, 40, 44, 48, 149, 153, 157, 161)


def analyze_environment(
    *,
    bss_records: list[BssRecord],
    survey_records: list[SurveyRecord],
    source_description: str,
    location_label: str,
    notes: str,
    scan_path: str | None,
    survey_path: str | None,
    strong_rssi_threshold_dbm: float,
) -> AnalysisReport:
    bands: list[BandMetrics] = []
    for band in ("2.4 GHz", "5 GHz"):
        band_bss = [record for record in bss_records if record.band == band]
        band_survey = [record for record in survey_records if record.band == band]
        bands.append(
            _build_band_metrics(
                band=band,
                bss_records=band_bss,
                survey_records=band_survey,
                strong_rssi_threshold_dbm=strong_rssi_threshold_dbm,
            )
        )
    return AnalysisReport(
        generated_at_utc=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        source_description=source_description,
        location_label=location_label,
        notes=notes,
        scan_path=scan_path,
        survey_path=survey_path,
        strong_rssi_threshold_dbm=strong_rssi_threshold_dbm,
        bands=tuple(bands),
    )


def _build_band_metrics(
    *,
    band: str,
    bss_records: list[BssRecord],
    survey_records: list[SurveyRecord],
    strong_rssi_threshold_dbm: float,
) -> BandMetrics:
    candidate_channels = _candidate_channels(band=band, bss_records=bss_records, survey_records=survey_records)
    survey_by_channel = {record.channel: record for record in survey_records}

    channel_metrics: list[ChannelMetrics] = []
    for channel in candidate_channels:
        channel_neighbors = [record for record in bss_records if _overlap_factor(record.channel, channel, band) > 0]
        exact_channel_neighbors = [record for record in bss_records if record.channel == channel]
        strong_neighbors = [
            record
            for record in channel_neighbors
            if record.signal_dbm is not None and record.signal_dbm >= strong_rssi_threshold_dbm
        ]
        score = sum(
            _overlap_factor(record.channel, channel, band) * _rssi_weight(record.signal_dbm)
            for record in channel_neighbors
        )
        survey = survey_by_channel.get(channel)
        channel_metrics.append(
            ChannelMetrics(
                channel=channel,
                band=band,
                ap_count=len(exact_channel_neighbors),
                unique_ssid_count=len({record.ssid for record in exact_channel_neighbors}),
                strong_ap_count=len(strong_neighbors),
                congestion_score=round(score, 3),
                strongest_signal_dbm=max(
                    (record.signal_dbm for record in channel_neighbors if record.signal_dbm is not None),
                    default=None,
                ),
                survey_busy_ratio=survey.busy_ratio if survey is not None else None,
                survey_noise_dbm=survey.noise_dbm if survey is not None else None,
            )
        )

    recommended_channels = tuple(
        metric.channel
        for metric in sorted(
            channel_metrics,
            key=lambda item: (
                0 if _channel_has_observed_data(item) else 1,
                item.congestion_score,
                item.strong_ap_count,
                item.ap_count,
                2.0 if item.survey_busy_ratio is None else item.survey_busy_ratio,
                item.channel,
            ),
        )[:3]
    )

    signals = [record.signal_dbm for record in bss_records if record.signal_dbm is not None]
    busy_ratios = [record.busy_ratio for record in survey_records if record.busy_ratio is not None]
    noises = [record.noise_dbm for record in survey_records if record.noise_dbm is not None]
    strongest_neighbors = tuple(
        sorted(
            [record for record in bss_records if record.signal_dbm is not None],
            key=lambda item: item.signal_dbm or -999.0,
            reverse=True,
        )[:5]
    )

    return BandMetrics(
        band=band,
        ap_count=len(bss_records),
        unique_ssid_count=len({record.ssid for record in bss_records}),
        strong_ap_count=len(
            [
                record
                for record in bss_records
                if record.signal_dbm is not None and record.signal_dbm >= strong_rssi_threshold_dbm
            ]
        ),
        median_signal_dbm=round(median(signals), 2) if signals else None,
        mean_survey_busy_ratio=round(fmean(busy_ratios), 4) if busy_ratios else None,
        mean_noise_dbm=round(fmean(noises), 2) if noises else None,
        recommended_channels=recommended_channels,
        channel_metrics=tuple(channel_metrics),
        strongest_neighbors=strongest_neighbors,
    )


def _candidate_channels(
    *,
    band: str,
    bss_records: list[BssRecord],
    survey_records: list[SurveyRecord],
) -> list[int]:
    channels = {record.channel for record in bss_records}
    channels.update(record.channel for record in survey_records)
    if band == "2.4 GHz":
        channels.update(_COMMON_24_CHANNELS)
    elif band == "5 GHz":
        channels.update(_COMMON_5_CHANNELS)
    return sorted(channel for channel in channels if channel > 0)


def _overlap_factor(ap_channel: int, candidate_channel: int, band: str) -> float:
    if band == "2.4 GHz":
        gap = abs(ap_channel - candidate_channel)
        if gap == 0:
            return 1.0
        if gap == 1:
            return 0.8
        if gap == 2:
            return 0.55
        if gap == 3:
            return 0.25
        if gap == 4:
            return 0.1
        return 0.0
    return 1.0 if ap_channel == candidate_channel else 0.0


def _rssi_weight(signal_dbm: float | None) -> float:
    if signal_dbm is None:
        return 0.05
    if signal_dbm >= -55:
        return 1.0
    if signal_dbm >= -67:
        return 0.75
    if signal_dbm >= -75:
        return 0.45
    if signal_dbm >= -82:
        return 0.2
    return 0.05


def _channel_has_observed_data(metric: ChannelMetrics) -> bool:
    return metric.ap_count > 0 or metric.survey_busy_ratio is not None or metric.survey_noise_dbm is not None
