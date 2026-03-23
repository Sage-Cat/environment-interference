from __future__ import annotations

COMMON_24_CHANNELS: tuple[int, ...] = (1, 6, 11)
COMMON_5_CHANNELS: tuple[int, ...] = (
    36,
    40,
    44,
    48,
    52,
    56,
    60,
    64,
    100,
    104,
    108,
    112,
    116,
    120,
    124,
    128,
    132,
    136,
    140,
    149,
    153,
    157,
    161,
)


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


def same_5ghz_40mhz_pair(channel_a: int, channel_b: int) -> bool:
    root_a = _five_ghz_pair_root(channel_a)
    root_b = _five_ghz_pair_root(channel_b)
    return root_a is not None and root_a == root_b


def same_5ghz_80mhz_block(channel_a: int, channel_b: int) -> bool:
    root_a = _five_ghz_block_root(channel_a)
    root_b = _five_ghz_block_root(channel_b)
    return root_a is not None and root_a == root_b


def five_ghz_block_label(channel: int) -> str | None:
    root = _five_ghz_block_root(channel)
    if root is None:
        return None
    return f"{root}-{root + 12}"


def _five_ghz_pair_root(channel: int) -> int | None:
    for root in (36, 44, 52, 60, 100, 108, 116, 124, 132, 149, 157):
        if channel in {root, root + 4}:
            return root
    return None


def _five_ghz_block_root(channel: int) -> int | None:
    for root in (36, 52, 100, 116, 132, 149):
        if channel in {root, root + 4, root + 8, root + 12}:
            return root
    return None
