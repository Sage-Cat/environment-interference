from __future__ import annotations


def band_label(freq_mhz: int) -> str:
    if 2400 <= freq_mhz <= 2500:
        return "2.4 GHz"
    if 5000 <= freq_mhz <= 5900:
        return "5 GHz"
    return "Other"


def freq_to_channel(freq_mhz: int) -> int | None:
    if freq_mhz == 2484:
        return 14
    if 2412 <= freq_mhz <= 2472:
        return ((freq_mhz - 2412) // 5) + 1
    if 5000 <= freq_mhz <= 5895:
        return (freq_mhz - 5000) // 5
    return None

