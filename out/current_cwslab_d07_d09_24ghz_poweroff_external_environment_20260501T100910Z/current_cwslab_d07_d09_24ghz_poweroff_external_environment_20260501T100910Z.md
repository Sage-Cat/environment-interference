# Scientific Wi-Fi Environment Interference Report

## Abstract

This report characterizes the current laboratory Wi-Fi field with emphasis on `2.4 GHz` channel `6` at `20 MHz`, which is the planned operating point for `cws-lab`. The target channel currently maps to interference level `L3` and radio-load level `L2`, while the lowest modeled alternatives in-band are `11, 1, 2`.

## Measurement Setup

- Generated at (UTC): `2026-05-01T10:10:55Z`
- Source: `live nmcli repeated collection from interface wlp3s0 (8 scans, 5.0 s interval)`
- Collection backend: `nmcli`
- Location: `cws-lab experiment area`
- Strong-neighbor threshold: `-67.0 dBm`
- Scan source: `out/current_cwslab_d07_d09_24ghz_poweroff_external_environment_20260501T100910Z/current_cwslab_d07_d09_24ghz_poweroff_external_environment_20260501T100910Z.scan.txt`
- Survey source: `not available`
- Notes: Ambient pre-experiment environment measurement for D07-D09 after the operator powered off all experiment devices. This canonical run followed forced nmcli rescans to clear stale lab SSID cache entries. Focus is the Node-C/T2 support surface: 2.4 GHz channel 6 / 20 MHz. Known cws-lab SSIDs are excluded from interference scoring to estimate external background.

## Executive Summary

- **2.4 GHz**: `33` APs observed, `3` strong emitters, recommended channels `11, 1, 2`.
- **5 GHz**: `4` APs observed, `2` strong emitters, recommended channels `52, 56, 60`.
- **Focus assessment**: `2.4 GHz` channel `6` / `20 MHz` maps to interference level `L3` and radio-load level `L2`.

## 2.4 GHz Experiment Focus

| Metric | Value |
| --- | --- |
| Focus channel | 6 |
| Focus width | 20 MHz |
| Rank within band | 10 |
| 5 GHz block | n/a |
| Exact-channel APs | 7 |
| Exact-channel strong APs | 1 |
| Overlapping / same-block APs | 21 |
| Overlapping / same-block strong APs | 3 |
| Strongest exact signal | -59.0 dBm |
| Strongest overlap signal | -53.0 dBm |
| Congestion score | 3.707 |
| Survey busy ratio | n/a |
| Inferred interference level | L3 |
| Inferred radio-load level | L2 |
| Recommended in-band channels | 11, 1, 2 |

Interpretation:
- The channel should be retuned or the environment should be isolated before claiming a clean cws-lab baseline.
- The current channel state should be treated as `L3` for interference and `L2` for radio loading when mapping the lab to `L0-L2` cws-lab assumptions.
- This channel should not be described as a clean `L0` baseline without extra isolation or a channel move.

## Observed Band Results


### 2.4 GHz

| Metric | Value |
| --- | --- |
| AP count | 33 |
| Unique SSID count | 29 |
| Strong-neighbor count | 3 |
| Median signal (dBm) | -85.00 |
| Mean survey busy ratio | n/a |
| Mean noise floor (dBm) | n/a |
| Recommended channels | 11, 1, 2 |

#### Channel Occupancy

| Channel | Exact APs | Exact Strong | Overlap APs | Overlap Strong | Congestion | Strongest Exact | Strongest Overlap | Survey Busy | Noise |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 6 | 0 | 16 | 0 | 1.335 | -70.5 dBm | -68.0 dBm | n/a | n/a |
| 2 | 4 | 0 | 23 | 1 | 1.590 | -81.5 dBm | -59.0 dBm | n/a | n/a |
| 3 | 2 | 0 | 25 | 3 | 1.980 | -85.0 dBm | -53.0 dBm | n/a | n/a |
| 4 | 2 | 0 | 26 | 3 | 2.532 | -75.5 dBm | -53.0 dBm | n/a | n/a |
| 5 | 2 | 0 | 27 | 3 | 3.260 | -68.0 dBm | -53.0 dBm | n/a | n/a |
| 6 | 7 | 1 | 21 | 3 | 3.707 | -59.0 dBm | -53.0 dBm | n/a | n/a |
| 7 | 2 | 2 | 23 | 3 | 3.645 | -53.0 dBm | -53.0 dBm | n/a | n/a |
| 8 | 1 | 0 | 21 | 3 | 2.793 | -86.5 dBm | -53.0 dBm | n/a | n/a |
| 9 | 1 | 0 | 19 | 3 | 1.893 | -77.5 dBm | -53.0 dBm | n/a | n/a |
| 11 | 6 | 0 | 10 | 2 | 0.623 | -83.0 dBm | -53.0 dBm | n/a | n/a |

#### Strongest Nearby APs

| SSID | BSSID | Channel | Signal | Estimated | Last seen |
| --- | --- | --- | --- | --- | --- |
| EOM | `5c:62:8b:36:83:e1` | 7 | -53.0 dBm | yes | n/a |
| <hidden> | `5e:62:8b:26:83:e1` | 7 | -54.0 dBm | yes | n/a |
| dlink-rustview | `00:24:01:bc:42:e5` | 6 | -59.0 dBm | yes | n/a |
| EOM | `40:ed:00:63:bc:de` | 5 | -68.0 dBm | yes | n/a |
| 1e5911a8 | `f4:91:1e:59:11:a8` | 1 | -70.5 dBm | yes | n/a |

#### Interpretation

- Highest modeled congestion is on channel `6` with score `3.707`.
- Lowest modeled congestion is on channel `11` with score `0.623`.
- Recommended channels for experiments in this band: `11, 1, 2`.
- Airtime utilization counters were not available, so interpretation is driven mainly by neighboring AP presence and signal strength.

### 5 GHz

| Metric | Value |
| --- | --- |
| AP count | 4 |
| Unique SSID count | 3 |
| Strong-neighbor count | 2 |
| Median signal (dBm) | -65.25 |
| Mean survey busy ratio | n/a |
| Mean noise floor (dBm) | n/a |
| Recommended channels | 52, 56, 60 |

#### Channel Occupancy

| Channel | Exact APs | Exact Strong | Overlap APs | Overlap Strong | Congestion | Strongest Exact | Strongest Overlap | Survey Busy | Noise |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 36 | 2 | 2 | 4 | 2 | 1.695 | -56.5 dBm | -56.5 dBm | n/a | n/a |
| 40 | 0 | 0 | 4 | 2 | 1.020 | n/a | -56.5 dBm | n/a | n/a |
| 44 | 2 | 0 | 4 | 2 | 1.100 | -74.0 dBm | -56.5 dBm | n/a | n/a |
| 48 | 0 | 0 | 4 | 2 | 0.807 | n/a | -56.5 dBm | n/a | n/a |
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
| <hidden> | `5e:62:8b:56:83:e1` | 36 | -56.5 dBm | yes | n/a |
| EOM | `5c:62:8b:36:83:e0` | 36 | -56.5 dBm | yes | n/a |
| EOM_5Ghz | `40:ed:00:63:bc:e0` | 44 | -74.0 dBm | yes | n/a |
| <hidden> | `42:ed:00:53:bc:de` | 44 | -75.5 dBm | yes | n/a |

#### Interpretation

- Highest modeled congestion is on channel `36` with score `1.695`.
- Lowest modeled congestion is on channel `52` with score `0.000`.
- Recommended channels for experiments in this band: `52, 56, 60`.
- Airtime utilization counters were not available, so interpretation is driven mainly by neighboring AP presence and signal strength.

## Methodological Limitations

- Signal levels were estimated from `nmcli` quality percentages, so absolute dBm values should be treated as approximate.
- Channel-survey airtime utilization was not available because `nmcli` does not expose `iw survey dump` counters.
- One or more SSID/BSSID filters were applied before interference scoring.
