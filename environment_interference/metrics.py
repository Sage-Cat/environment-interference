from __future__ import annotations

from datetime import datetime, timezone
from statistics import fmean, median

from .models import AnalysisReport, BandMetrics, BssRecord, ChannelMetrics, FocusChannelAssessment, SurveyRecord
from .radio import COMMON_24_CHANNELS, COMMON_5_CHANNELS, five_ghz_block_label, same_5ghz_40mhz_pair, same_5ghz_80mhz_block


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
    collection_backend: str = "unknown",
    focus_band: str = "5 GHz",
    focus_channel: int | None = None,
    focus_width_mhz: int = 20,
    exclude_ssids: tuple[str, ...] = (),
    exclude_bssids: tuple[str, ...] = (),
) -> AnalysisReport:
    filtered_bss_records = _filter_bss_records(
        bss_records=bss_records,
        exclude_ssids=exclude_ssids,
        exclude_bssids=exclude_bssids,
    )

    bands: list[BandMetrics] = []
    for band in ("2.4 GHz", "5 GHz"):
        band_bss = [record for record in filtered_bss_records if record.band == band]
        band_survey = [record for record in survey_records if record.band == band]
        bands.append(
            _build_band_metrics(
                band=band,
                bss_records=band_bss,
                survey_records=band_survey,
                strong_rssi_threshold_dbm=strong_rssi_threshold_dbm,
            )
        )

    warnings = _build_warnings(
        original_bss_records=bss_records,
        filtered_bss_records=filtered_bss_records,
        survey_records=survey_records,
        collection_backend=collection_backend,
        exclude_ssids=exclude_ssids,
        exclude_bssids=exclude_bssids,
    )

    normalized_focus_band = _normalize_band(focus_band)
    resolved_focus_channel = focus_channel or _default_focus_channel(normalized_focus_band)
    focus_assessment = _build_focus_assessment(
        bands=bands,
        focus_band=normalized_focus_band,
        focus_channel=resolved_focus_channel,
        focus_width_mhz=focus_width_mhz,
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
        collection_backend=collection_backend,
        warnings=tuple(warnings),
        focus_assessment=focus_assessment,
    )


def _filter_bss_records(
    *,
    bss_records: list[BssRecord],
    exclude_ssids: tuple[str, ...],
    exclude_bssids: tuple[str, ...],
) -> list[BssRecord]:
    excluded_ssids = {item for item in exclude_ssids if item}
    excluded_bssids = {item.lower() for item in exclude_bssids if item}
    return [
        record
        for record in bss_records
        if record.ssid not in excluded_ssids and record.bssid.lower() not in excluded_bssids
    ]


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
        overlap_neighbors = [record for record in bss_records if _overlap_factor(record.channel, channel, band) > 0.0]
        exact_channel_neighbors = [record for record in bss_records if record.channel == channel]
        overlap_strong_neighbors = [
            record
            for record in overlap_neighbors
            if record.signal_dbm is not None and record.signal_dbm >= strong_rssi_threshold_dbm
        ]
        exact_strong_neighbors = [
            record
            for record in exact_channel_neighbors
            if record.signal_dbm is not None and record.signal_dbm >= strong_rssi_threshold_dbm
        ]
        score = sum(
            _overlap_factor(record.channel, channel, band) * _rssi_weight(record.signal_dbm)
            for record in overlap_neighbors
        )
        survey = survey_by_channel.get(channel)
        if survey is not None and survey.busy_ratio is not None:
            score += survey.busy_ratio * 1.5
        channel_metrics.append(
            ChannelMetrics(
                channel=channel,
                band=band,
                ap_count=len(exact_channel_neighbors),
                unique_ssid_count=len({record.ssid for record in exact_channel_neighbors}),
                strong_ap_count=len(overlap_strong_neighbors),
                exact_strong_ap_count=len(exact_strong_neighbors),
                overlap_ap_count=len(overlap_neighbors),
                overlap_strong_ap_count=len(overlap_strong_neighbors),
                congestion_score=round(score, 3),
                strongest_signal_dbm=max(
                    (record.signal_dbm for record in overlap_neighbors if record.signal_dbm is not None),
                    default=None,
                ),
                strongest_exact_signal_dbm=max(
                    (record.signal_dbm for record in exact_channel_neighbors if record.signal_dbm is not None),
                    default=None,
                ),
                survey_busy_ratio=survey.busy_ratio if survey is not None else None,
                survey_noise_dbm=survey.noise_dbm if survey is not None else None,
            )
        )

    recommended_channels = tuple(
        metric.channel
        for metric in sorted(channel_metrics, key=_channel_sort_key)[:3]
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


def _build_focus_assessment(
    *,
    bands: list[BandMetrics],
    focus_band: str,
    focus_channel: int,
    focus_width_mhz: int,
) -> FocusChannelAssessment | None:
    band_metrics = next((band for band in bands if band.band == focus_band), None)
    if band_metrics is None:
        return None
    if not band_metrics.channel_metrics:
        return None

    ranked = sorted(band_metrics.channel_metrics, key=_channel_sort_key)
    by_channel = {metric.channel: metric for metric in band_metrics.channel_metrics}
    focus_metric = by_channel.get(focus_channel)
    if focus_metric is None:
        focus_metric = ChannelMetrics(
            channel=focus_channel,
            band=focus_band,
            ap_count=0,
            unique_ssid_count=0,
            strong_ap_count=0,
            exact_strong_ap_count=0,
            overlap_ap_count=0,
            overlap_strong_ap_count=0,
            congestion_score=0.0,
            strongest_signal_dbm=None,
            strongest_exact_signal_dbm=None,
            survey_busy_ratio=None,
            survey_noise_dbm=None,
        )
    rank = next((index + 1 for index, metric in enumerate(ranked) if metric.channel == focus_channel), None)

    interference_level = _classify_interference_level(focus_metric=focus_metric, rank_in_band=rank)
    radio_load_level = _classify_radio_load_level(focus_metric=focus_metric, band_metrics=band_metrics)
    readiness = _classify_readiness(
        interference_level=interference_level,
        radio_load_level=radio_load_level,
        rank_in_band=rank,
    )

    return FocusChannelAssessment(
        band=focus_band,
        channel=focus_channel,
        channel_width_mhz=focus_width_mhz,
        rank_in_band=rank,
        recommended_channels=band_metrics.recommended_channels,
        block_label=five_ghz_block_label(focus_channel) if focus_band == "5 GHz" else None,
        exact_ap_count=focus_metric.ap_count,
        exact_strong_ap_count=focus_metric.exact_strong_ap_count,
        overlap_ap_count=focus_metric.overlap_ap_count,
        overlap_strong_ap_count=focus_metric.overlap_strong_ap_count,
        strongest_exact_signal_dbm=focus_metric.strongest_exact_signal_dbm,
        strongest_overlap_signal_dbm=focus_metric.strongest_signal_dbm,
        congestion_score=focus_metric.congestion_score,
        survey_busy_ratio=focus_metric.survey_busy_ratio,
        inferred_interference_level=interference_level,
        inferred_radio_load_level=radio_load_level,
        readiness=readiness,
    )


def _build_warnings(
    *,
    original_bss_records: list[BssRecord],
    filtered_bss_records: list[BssRecord],
    survey_records: list[SurveyRecord],
    collection_backend: str,
    exclude_ssids: tuple[str, ...],
    exclude_bssids: tuple[str, ...],
) -> list[str]:
    warnings: list[str] = []
    if not filtered_bss_records:
        warnings.append("No BSS records remain after filtering; report sections will be mostly empty.")
    if any(record.signal_dbm_estimated for record in original_bss_records):
        warnings.append(
            "Signal levels were estimated from `nmcli` quality percentages, so absolute dBm values should be treated as approximate."
        )
    if not survey_records:
        if collection_backend == "nmcli":
            warnings.append(
                "Channel-survey airtime utilization was not available because `nmcli` does not expose `iw survey dump` counters."
            )
        else:
            warnings.append(
                "Channel-survey airtime utilization was not available, so radio-loading estimates rely on neighboring-AP observations."
            )
    if exclude_ssids or exclude_bssids:
        warnings.append("One or more SSID/BSSID filters were applied before interference scoring.")
    return warnings


def _candidate_channels(
    *,
    band: str,
    bss_records: list[BssRecord],
    survey_records: list[SurveyRecord],
) -> list[int]:
    channels = {record.channel for record in bss_records}
    channels.update(record.channel for record in survey_records)
    if band == "2.4 GHz":
        channels.update(COMMON_24_CHANNELS)
    elif band == "5 GHz":
        channels.update(COMMON_5_CHANNELS)
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
    if ap_channel == candidate_channel:
        return 1.0
    if same_5ghz_40mhz_pair(ap_channel, candidate_channel):
        return 0.55
    if same_5ghz_80mhz_block(ap_channel, candidate_channel):
        return 0.3
    return 0.0


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


def _channel_sort_key(item: ChannelMetrics) -> tuple[float, int, int, float, int]:
    return (
        item.congestion_score,
        item.overlap_strong_ap_count,
        item.overlap_ap_count,
        2.0 if item.survey_busy_ratio is None else item.survey_busy_ratio,
        item.channel,
    )


def _classify_interference_level(*, focus_metric: ChannelMetrics, rank_in_band: int | None) -> str:
    score = 0
    if focus_metric.ap_count >= 1:
        score += 2
    if focus_metric.exact_strong_ap_count >= 1:
        score += 2
    if focus_metric.overlap_ap_count >= 2:
        score += 1
    if focus_metric.overlap_strong_ap_count >= 1:
        score += 1
    if focus_metric.strongest_signal_dbm is not None and focus_metric.strongest_signal_dbm >= -60.0:
        score += 1
    if rank_in_band is not None and rank_in_band >= 4:
        score += 1
    if focus_metric.survey_busy_ratio is not None:
        if focus_metric.survey_busy_ratio >= 0.45:
            score += 2
        elif focus_metric.survey_busy_ratio >= 0.25:
            score += 1
    return _score_to_level(score)


def _classify_radio_load_level(*, focus_metric: ChannelMetrics, band_metrics: BandMetrics) -> str:
    score = 0
    if focus_metric.overlap_ap_count >= 1:
        score += 1
    if focus_metric.overlap_ap_count >= 3:
        score += 1
    if focus_metric.overlap_strong_ap_count >= 1:
        score += 1
    if band_metrics.ap_count >= 5:
        score += 1
    if band_metrics.ap_count >= 8:
        score += 1
    if focus_metric.survey_busy_ratio is not None:
        if focus_metric.survey_busy_ratio >= 0.35:
            score += 2
        elif focus_metric.survey_busy_ratio >= 0.15:
            score += 1
    return _score_to_level(score)


def _score_to_level(score: int) -> str:
    if score <= 1:
        return "L0"
    if score <= 3:
        return "L1"
    if score <= 5:
        return "L2"
    return "L3"


def _classify_readiness(
    *,
    interference_level: str,
    radio_load_level: str,
    rank_in_band: int | None,
) -> str:
    if interference_level in {"L0", "L1"} and radio_load_level in {"L0", "L1"} and (rank_in_band or 99) <= 2:
        return "ready_with_documented_baseline"
    if interference_level in {"L0", "L1", "L2"} and radio_load_level in {"L0", "L1", "L2"} and (rank_in_band or 99) <= 3:
        return "usable_with_controls"
    return "retune_or_isolate_before_cwslab"


def _normalize_band(value: str) -> str:
    normalized = value.strip().lower().replace(" ", "")
    if normalized in {"24", "2.4", "24ghz", "2.4ghz"}:
        return "2.4 GHz"
    if normalized in {"5", "5ghz"}:
        return "5 GHz"
    raise ValueError(f"unsupported focus band: {value}")


def _default_focus_channel(band: str) -> int:
    if band == "2.4 GHz":
        return 6
    return 36
