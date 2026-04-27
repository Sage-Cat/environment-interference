# Scientific Wi-Fi Environment Interference Report

## Abstract

This report characterizes the current laboratory Wi-Fi field with emphasis on `5 GHz` channel `36` at `20 MHz`, which is the planned operating point for `cws-lab`. The target channel currently maps to interference level `L3` and radio-load level `L1`, while the lowest modeled alternatives in-band are `52, 56, 60`.

## Measurement Setup

- Generated at (UTC): `2026-04-27T09:28:07Z`
- Source: `live nmcli repeated collection from interface wlp3s0 (8 scans, 5.0 s interval)`
- Collection backend: `nmcli`
- Location: `cws-lab D05-D09 experiment environment, external 5 GHz view`
- Strong-neighbor threshold: `-67.0 dBm`
- Scan source: `out/current_cwslab_d05_d09_5ghz_external_environment_20260427T092723Z/current_cwslab_d05_d09_5ghz_external_environment_20260427T092723Z.scan.txt`
- Survey source: `not available`
- Notes: Ambient pre-experiment environment measurement for D05-D09. Focus is the common main AP operating point: 5 GHz, channel 36, 20 MHz. Known cws-lab SSIDs are excluded from interference scoring to estimate external background.

## Executive Summary

- **2.4 GHz**: `20` APs observed, `2` strong emitters, recommended channels `13, 1, 3`.
- **5 GHz**: `2` APs observed, `2` strong emitters, recommended channels `52, 56, 60`.
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
| Overlapping / same-block APs | 2 |
| Overlapping / same-block strong APs | 2 |
| Strongest exact signal | -57.5 dBm |
| Strongest overlap signal | -57.5 dBm |
| Congestion score | 1.500 |
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
| AP count | 20 |
| Unique SSID count | 19 |
| Strong-neighbor count | 2 |
| Median signal (dBm) | -82.75 |
| Mean survey busy ratio | n/a |
| Mean noise floor (dBm) | n/a |
| Recommended channels | 13, 1, 3 |

#### Channel Occupancy

| Channel | Exact APs | Exact Strong | Overlap APs | Overlap Strong | Congestion | Strongest Exact | Strongest Overlap | Survey Busy | Noise |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 3 | 0 | 10 | 0 | 0.523 | -80.0 dBm | -76.5 dBm | n/a | n/a |
| 3 | 2 | 0 | 14 | 0 | 0.938 | -84.0 dBm | -76.5 dBm | n/a | n/a |
| 4 | 4 | 0 | 15 | 0 | 1.125 | -76.5 dBm | -76.5 dBm | n/a | n/a |
| 5 | 1 | 0 | 17 | 2 | 1.243 | -83.0 dBm | -54.0 dBm | n/a | n/a |
| 6 | 4 | 0 | 14 | 2 | 1.387 | -77.5 dBm | -54.0 dBm | n/a | n/a |
| 8 | 1 | 0 | 14 | 2 | 1.828 | -85.0 dBm | -54.0 dBm | n/a | n/a |
| 9 | 2 | 2 | 11 | 2 | 1.995 | -54.0 dBm | -54.0 dBm | n/a | n/a |
| 11 | 2 | 0 | 6 | 2 | 1.185 | -87.5 dBm | -54.0 dBm | n/a | n/a |
| 13 | 1 | 0 | 5 | 2 | 0.430 | -75.5 dBm | -54.0 dBm | n/a | n/a |

#### Strongest Nearby APs

| SSID | BSSID | Channel | Signal | Estimated | Last seen |
| --- | --- | --- | --- | --- | --- |
| <hidden> | `5e:62:8b:26:83:e1` | 9 | -54.0 dBm | yes | n/a |
| EOM | `5c:62:8b:36:83:e1` | 9 | -57.5 dBm | yes | n/a |
| Redmi Note 11 Pro | `4a:5d:58:f3:3a:a0` | 13 | -75.5 dBm | yes | n/a |
| TP-Link_512 | `f0:09:0d:78:db:c8` | 4 | -76.5 dBm | yes | n/a |
| <hidden> | `f2:09:0d:28:db:c8` | 4 | -76.5 dBm | yes | n/a |

#### Interpretation

- Highest modeled congestion is on channel `9` with score `1.995`.
- Lowest modeled congestion is on channel `13` with score `0.430`.
- Recommended channels for experiments in this band: `13, 1, 3`.
- Airtime utilization counters were not available, so interpretation is driven mainly by neighboring AP presence and signal strength.

### 5 GHz

| Metric | Value |
| --- | --- |
| AP count | 2 |
| Unique SSID count | 2 |
| Strong-neighbor count | 2 |
| Median signal (dBm) | -57.50 |
| Mean survey busy ratio | n/a |
| Mean noise floor (dBm) | n/a |
| Recommended channels | 52, 56, 60 |

#### Channel Occupancy

| Channel | Exact APs | Exact Strong | Overlap APs | Overlap Strong | Congestion | Strongest Exact | Strongest Overlap | Survey Busy | Noise |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 36 | 2 | 2 | 2 | 2 | 1.500 | -57.5 dBm | -57.5 dBm | n/a | n/a |
| 40 | 0 | 0 | 2 | 2 | 0.825 | n/a | -57.5 dBm | n/a | n/a |
| 44 | 0 | 0 | 2 | 2 | 0.450 | n/a | -57.5 dBm | n/a | n/a |
| 48 | 0 | 0 | 2 | 2 | 0.450 | n/a | -57.5 dBm | n/a | n/a |
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
| <hidden> | `5e:62:8b:56:83:e1` | 36 | -57.5 dBm | yes | n/a |
| EOM | `5c:62:8b:36:83:e0` | 36 | -57.5 dBm | yes | n/a |

#### Interpretation

- Highest modeled congestion is on channel `36` with score `1.500`.
- Lowest modeled congestion is on channel `52` with score `0.000`.
- Recommended channels for experiments in this band: `52, 56, 60`.
- Airtime utilization counters were not available, so interpretation is driven mainly by neighboring AP presence and signal strength.

## Methodological Limitations

- Signal levels were estimated from `nmcli` quality percentages, so absolute dBm values should be treated as approximate.
- Channel-survey airtime utilization was not available because `nmcli` does not expose `iw survey dump` counters.
- One or more SSID/BSSID filters were applied before interference scoring.
