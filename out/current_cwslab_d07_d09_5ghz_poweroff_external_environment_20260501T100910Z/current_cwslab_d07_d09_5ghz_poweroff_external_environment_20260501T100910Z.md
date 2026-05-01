# Scientific Wi-Fi Environment Interference Report

## Abstract

This report characterizes the current laboratory Wi-Fi field with emphasis on `5 GHz` channel `36` at `20 MHz`, which is the planned operating point for `cws-lab`. The target channel currently maps to interference level `L3` and radio-load level `L1`, while the lowest modeled alternatives in-band are `52, 56, 60`.

## Measurement Setup

- Generated at (UTC): `2026-05-01T10:10:02Z`
- Source: `live nmcli repeated collection from interface wlp3s0 (8 scans, 5.0 s interval)`
- Collection backend: `nmcli`
- Location: `cws-lab experiment area`
- Strong-neighbor threshold: `-67.0 dBm`
- Scan source: `out/current_cwslab_d07_d09_5ghz_poweroff_external_environment_20260501T100910Z/current_cwslab_d07_d09_5ghz_poweroff_external_environment_20260501T100910Z.scan.txt`
- Survey source: `not available`
- Notes: Ambient pre-experiment environment measurement for D07-D09 after the operator powered off all experiment devices. This canonical run followed forced nmcli rescans to clear stale lab SSID cache entries. Focus is the shared 5 GHz channel 36 / 20 MHz surface used by the primary prplOS-compatible AP node and AP-B. Known cws-lab SSIDs are excluded from interference scoring to estimate external background.

## Executive Summary

- **2.4 GHz**: `35` APs observed, `3` strong emitters, recommended channels `11, 9, 1`.
- **5 GHz**: `4` APs observed, `2` strong emitters, recommended channels `52, 56, 60`.
- **Focus assessment**: `5 GHz` channel `36` / `20 MHz` maps to interference level `L3` and radio-load level `L1`.

## 5 GHz Experiment Focus

| Metric | Value |
| --- | --- |
| Focus channel | 36 |
| Focus width | 20 MHz |
| Rank within band | 23 |
| 5 GHz block | 36-48 |
| Exact-channel APs | 2 |
| Exact-channel strong APs | 2 |
| Overlapping / same-block APs | 4 |
| Overlapping / same-block strong APs | 2 |
| Strongest exact signal | -58.0 dBm |
| Strongest overlap signal | -58.0 dBm |
| Congestion score | 1.770 |
| Survey busy ratio | n/a |
| Inferred interference level | L3 |
| Inferred radio-load level | L1 |
| Recommended in-band channels | 52, 56, 60 |

Interpretation:
- The channel should be retuned or the environment should be isolated before claiming a clean cws-lab baseline.
- The current channel state should be treated as `L3` for interference and `L1` for radio loading when mapping the lab to `L0-L2` cws-lab assumptions.
- This channel should not be described as a clean `L0` baseline without extra isolation or a channel move.

## Observed Band Results


### 2.4 GHz

| Metric | Value |
| --- | --- |
| AP count | 35 |
| Unique SSID count | 31 |
| Strong-neighbor count | 3 |
| Median signal (dBm) | -81.50 |
| Mean survey busy ratio | n/a |
| Mean noise floor (dBm) | n/a |
| Recommended channels | 11, 9, 1 |

#### Channel Occupancy

| Channel | Exact APs | Exact Strong | Overlap APs | Overlap Strong | Congestion | Strongest Exact | Strongest Overlap | Survey Busy | Noise |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 9 | 0 | 19 | 0 | 2.325 | -70.5 dBm | -70.5 dBm | n/a | n/a |
| 2 | 4 | 0 | 24 | 1 | 2.573 | -78.0 dBm | -58.0 dBm | n/a | n/a |
| 3 | 2 | 0 | 26 | 3 | 2.905 | -85.0 dBm | -54.0 dBm | n/a | n/a |
| 4 | 2 | 0 | 27 | 3 | 3.310 | -74.0 dBm | -54.0 dBm | n/a | n/a |
| 5 | 2 | 0 | 28 | 3 | 3.815 | -71.5 dBm | -54.0 dBm | n/a | n/a |
| 6 | 5 | 1 | 19 | 3 | 4.003 | -58.0 dBm | -54.0 dBm | n/a | n/a |
| 7 | 2 | 2 | 22 | 3 | 3.807 | -54.0 dBm | -54.0 dBm | n/a | n/a |
| 8 | 1 | 0 | 20 | 3 | 2.912 | -87.5 dBm | -54.0 dBm | n/a | n/a |
| 9 | 1 | 0 | 18 | 3 | 2.075 | -76.5 dBm | -54.0 dBm | n/a | n/a |
| 11 | 7 | 0 | 11 | 2 | 0.973 | -76.5 dBm | -54.0 dBm | n/a | n/a |

#### Strongest Nearby APs

| SSID | BSSID | Channel | Signal | Estimated | Last seen |
| --- | --- | --- | --- | --- | --- |
| EOM | `5c:62:8b:36:83:e1` | 7 | -54.0 dBm | yes | n/a |
| <hidden> | `5e:62:8b:26:83:e1` | 7 | -54.0 dBm | yes | n/a |
| dlink-rustview | `00:24:01:bc:42:e5` | 6 | -58.0 dBm | yes | n/a |
| 1e5911a8 | `f4:91:1e:59:11:a8` | 1 | -70.5 dBm | yes | n/a |
| EOM | `40:ed:00:63:bc:de` | 5 | -71.5 dBm | yes | n/a |

#### Interpretation

- Highest modeled congestion is on channel `6` with score `4.003`.
- Lowest modeled congestion is on channel `11` with score `0.973`.
- Recommended channels for experiments in this band: `11, 9, 1`.
- Airtime utilization counters were not available, so interpretation is driven mainly by neighboring AP presence and signal strength.

### 5 GHz

| Metric | Value |
| --- | --- |
| AP count | 4 |
| Unique SSID count | 3 |
| Strong-neighbor count | 2 |
| Median signal (dBm) | -66.50 |
| Mean survey busy ratio | n/a |
| Mean noise floor (dBm) | n/a |
| Recommended channels | 52, 56, 60 |

#### Channel Occupancy

| Channel | Exact APs | Exact Strong | Overlap APs | Overlap Strong | Congestion | Strongest Exact | Strongest Overlap | Survey Busy | Noise |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 36 | 2 | 2 | 4 | 2 | 1.770 | -58.0 dBm | -58.0 dBm | n/a | n/a |
| 40 | 0 | 0 | 4 | 2 | 1.095 | n/a | -58.0 dBm | n/a | n/a |
| 44 | 2 | 0 | 4 | 2 | 1.350 | -75.0 dBm | -58.0 dBm | n/a | n/a |
| 48 | 0 | 0 | 4 | 2 | 0.945 | n/a | -58.0 dBm | n/a | n/a |
| 52 | 0 | 0 | 0 | 0 | 0.000 | n/a | n/a | n/a | n/a |
| 56 | 0 | 0 | 0 | 0 | 0.000 | n/a | n/a | n/a | n/a |
| 60 | 0 | 0 | 0 | 0 | 0.000 | n/a | n/a | n/a | n/a |
| 64 | 0 | 0 | 0 | 0 | 0.000 | n/a | n/a | n/a | n/a |
| 100 | 0 | 0 | 0 | 0 | 0.000 | n/a | n/a | n/a | n/a |
| 104 | 0 | 0 | 0 | 0 | 0.000 | n/a | n/a | n/a | n/a |
| 108 | 0 | 0 | 0 | 0 | 0.000 | n/a | n/a | n/a | n/a |
| 112 | 0 | 0 | 0 | 0 | 0.000 | n/a | n/a | n/a | n/a |
| 116 | 0 | 0 | 0 | 0 | 0.000 | n/a | n/a | n/a | n/a |
| 120 | 0 | 0 | 0 | 0 | 0.000 | n/a | n/a | n/a | n/a |
| 124 | 0 | 0 | 0 | 0 | 0.000 | n/a | n/a | n/a | n/a |
| 128 | 0 | 0 | 0 | 0 | 0.000 | n/a | n/a | n/a | n/a |
| 132 | 0 | 0 | 0 | 0 | 0.000 | n/a | n/a | n/a | n/a |
| 136 | 0 | 0 | 0 | 0 | 0.000 | n/a | n/a | n/a | n/a |
| 140 | 0 | 0 | 0 | 0 | 0.000 | n/a | n/a | n/a | n/a |
| 149 | 0 | 0 | 0 | 0 | 0.000 | n/a | n/a | n/a | n/a |
| 153 | 0 | 0 | 0 | 0 | 0.000 | n/a | n/a | n/a | n/a |
| 157 | 0 | 0 | 0 | 0 | 0.000 | n/a | n/a | n/a | n/a |
| 161 | 0 | 0 | 0 | 0 | 0.000 | n/a | n/a | n/a | n/a |

#### Strongest Nearby APs

| SSID | BSSID | Channel | Signal | Estimated | Last seen |
| --- | --- | --- | --- | --- | --- |
| EOM | `5c:62:8b:36:83:e0` | 36 | -58.0 dBm | yes | n/a |
| <hidden> | `5e:62:8b:56:83:e1` | 36 | -58.0 dBm | yes | n/a |
| EOM_5Ghz | `40:ed:00:63:bc:e0` | 44 | -75.0 dBm | yes | n/a |
| <hidden> | `42:ed:00:53:bc:de` | 44 | -75.0 dBm | yes | n/a |

#### Interpretation

- Highest modeled congestion is on channel `36` with score `1.770`.
- Lowest modeled congestion is on channel `52` with score `0.000`.
- Recommended channels for experiments in this band: `52, 56, 60`.
- Airtime utilization counters were not available, so interpretation is driven mainly by neighboring AP presence and signal strength.

## Methodological Limitations

- Signal levels were estimated from `nmcli` quality percentages, so absolute dBm values should be treated as approximate.
- Channel-survey airtime utilization was not available because `nmcli` does not expose `iw survey dump` counters.
- One or more SSID/BSSID filters were applied before interference scoring.
