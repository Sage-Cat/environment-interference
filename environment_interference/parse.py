from __future__ import annotations

import re

from .models import BssRecord, SurveyRecord
from .radio import freq_to_channel

_BSS_RE = re.compile(r"^BSS\s+([0-9a-fA-F:]{17})")
_FREQ_RE = re.compile(r"^freq:\s*(\d+)")
_SIGNAL_RE = re.compile(r"^signal:\s*([-0-9.]+)")
_LAST_SEEN_RE = re.compile(r"^last seen:\s*(\d+)")
_DS_CHANNEL_RE = re.compile(r"DS Parameter set:\s*channel\s*(\d+)")
_PRIMARY_CHANNEL_RE = re.compile(r"(?:\*?\s*)?primary channel:\s*(\d+)")
_SURVEY_FREQ_RE = re.compile(r"^frequency:\s*(\d+)\s+MHz(.*)$")
_SURVEY_VALUE_RE = re.compile(r"^(noise|channel active time|channel busy time|channel receive time|channel transmit time):\s*([-0-9.]+)")


def parse_scan_text(text: str, *, scan_format: str = "auto") -> list[BssRecord]:
    resolved_format = detect_scan_format(text) if scan_format == "auto" else scan_format
    if resolved_format == "iw":
        return parse_iw_scan(text)
    if resolved_format == "nmcli":
        return parse_nmcli_scan(text)
    raise ValueError(f"unsupported scan format: {resolved_format}")


def detect_scan_format(text: str) -> str:
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if _BSS_RE.match(line):
            return "iw"
        return "nmcli"
    return "iw"


def parse_iw_scan(text: str) -> list[BssRecord]:
    records: list[BssRecord] = []
    current_block: list[str] = []
    for line in text.splitlines():
        if _BSS_RE.match(line):
            if current_block:
                parsed = _parse_bss_block(current_block)
                if parsed is not None:
                    records.append(parsed)
            current_block = [line]
            continue
        if current_block:
            current_block.append(line)
    if current_block:
        parsed = _parse_bss_block(current_block)
        if parsed is not None:
            records.append(parsed)
    return records


def parse_nmcli_scan(text: str) -> list[BssRecord]:
    records: list[BssRecord] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        fields = split_nmcli_escaped_fields(line)
        if len(fields) != 8:
            raise ValueError(f"unexpected nmcli row shape: expected 8 fields, got {len(fields)} in {raw_line!r}")
        _in_use, ssid, bssid, channel_raw, freq_raw, _rate_raw, signal_raw, _security = fields
        try:
            channel = int(channel_raw)
            signal_pct = int(signal_raw)
        except ValueError as exc:
            raise ValueError(f"failed to parse nmcli row: {raw_line!r}") from exc
        freq_match = re.search(r"(\d+)", freq_raw)
        freq_mhz = int(freq_match.group(1)) if freq_match else None
        if freq_mhz is None:
            freq_mhz = _channel_to_frequency_mhz(channel)
        if freq_mhz is None:
            continue
        records.append(
            BssRecord(
                bssid=bssid.lower(),
                ssid=ssid,
                freq_mhz=freq_mhz,
                channel=channel,
                signal_dbm=None if signal_pct <= 0 else signal_percent_to_dbm(signal_pct),
                last_seen_ms=None,
                signal_dbm_estimated=True,
            )
        )
    return records


def _parse_bss_block(lines: list[str]) -> BssRecord | None:
    bss_match = _BSS_RE.match(lines[0])
    if bss_match is None:
        return None
    bssid = bss_match.group(1).lower()
    ssid = ""
    freq_mhz: int | None = None
    channel: int | None = None
    signal_dbm: float | None = None
    last_seen_ms: int | None = None

    for raw_line in lines[1:]:
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("SSID:"):
            ssid = line.split(":", 1)[1].strip()
            continue
        if (match := _FREQ_RE.match(line)) is not None:
            freq_mhz = int(match.group(1))
            continue
        if (match := _SIGNAL_RE.match(line)) is not None:
            signal_dbm = float(match.group(1))
            continue
        if (match := _LAST_SEEN_RE.match(line)) is not None:
            last_seen_ms = int(match.group(1))
            continue
        if channel is None and (match := _DS_CHANNEL_RE.search(line)) is not None:
            channel = int(match.group(1))
            continue
        if channel is None and (match := _PRIMARY_CHANNEL_RE.search(line)) is not None:
            channel = int(match.group(1))
            continue

    if freq_mhz is None:
        return None
    if channel is None:
        derived_channel = freq_to_channel(freq_mhz)
        if derived_channel is None:
            return None
        channel = derived_channel
    return BssRecord(
        bssid=bssid,
        ssid=ssid,
        freq_mhz=freq_mhz,
        channel=channel,
        signal_dbm=signal_dbm,
        last_seen_ms=last_seen_ms,
        signal_dbm_estimated=False,
    )


def parse_iw_survey(text: str) -> list[SurveyRecord]:
    records: list[SurveyRecord] = []
    current: dict[str, object] | None = None

    def flush_current() -> None:
        nonlocal current
        if current is None:
            return
        freq_mhz = int(current["freq_mhz"])
        channel = freq_to_channel(freq_mhz)
        if channel is not None:
            records.append(
                SurveyRecord(
                    freq_mhz=freq_mhz,
                    channel=channel,
                    noise_dbm=_maybe_float(current.get("noise_dbm")),
                    active_ms=_maybe_int(current.get("active_ms")),
                    busy_ms=_maybe_int(current.get("busy_ms")),
                    receive_ms=_maybe_int(current.get("receive_ms")),
                    transmit_ms=_maybe_int(current.get("transmit_ms")),
                    in_use=bool(current.get("in_use")),
                )
            )
        current = None

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("Survey data from"):
            continue
        if (match := _SURVEY_FREQ_RE.match(line)) is not None:
            flush_current()
            current = {
                "freq_mhz": int(match.group(1)),
                "in_use": "[in use]" in match.group(2),
            }
            continue
        if current is None:
            continue
        if (match := _SURVEY_VALUE_RE.match(line)) is None:
            continue
        key = match.group(1)
        value = match.group(2)
        if key == "noise":
            current["noise_dbm"] = float(value)
        elif key == "channel active time":
            current["active_ms"] = int(float(value))
        elif key == "channel busy time":
            current["busy_ms"] = int(float(value))
        elif key == "channel receive time":
            current["receive_ms"] = int(float(value))
        elif key == "channel transmit time":
            current["transmit_ms"] = int(float(value))
    flush_current()
    return records


def _maybe_int(value: object | None) -> int | None:
    if value is None:
        return None
    return int(value)


def _maybe_float(value: object | None) -> float | None:
    if value is None:
        return None
    return float(value)


def split_nmcli_escaped_fields(line: str, separator: str = ":") -> list[str]:
    parts: list[str] = []
    current: list[str] = []
    escape = False
    for char in line:
        if escape:
            current.append(char)
            escape = False
            continue
        if char == "\\":
            escape = True
            continue
        if char == separator:
            parts.append("".join(current))
            current = []
            continue
        current.append(char)
    parts.append("".join(current))
    return parts


def signal_percent_to_dbm(signal_pct: int) -> float:
    bounded = max(0, min(100, int(signal_pct)))
    return -100.0 + (bounded / 2.0)


def _channel_to_frequency_mhz(channel: int) -> int | None:
    if channel == 14:
        return 2484
    if 1 <= channel <= 13:
        return 2407 + (channel * 5)
    if channel >= 30:
        return 5000 + (channel * 5)
    return None
