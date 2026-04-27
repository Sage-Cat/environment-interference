# Scientific Wi-Fi Environment Interference Report

## Abstract

This report characterizes the current laboratory Wi-Fi field with emphasis on `5 GHz` channel `36` at `20 MHz`, which is the planned operating point for `cws-lab`. The target channel currently maps to interference level `L3` and radio-load level `L2`, while the lowest modeled alternatives in-band are `52, 56, 60`.

## Measurement Setup

- Generated at (UTC): `2026-04-23T12:36:18Z`
- Source: `live nmcli repeated collection from interface wlp3s0 (8 scans, 5.0 s interval)`
- Collection backend: `nmcli`
- Location: `Current cws-lab room`
- Strong-neighbor threshold: `-67.0 dBm`
- Scan source: `out/current_cwslab_5ghz_experiment_environment_20260423T123527Z/current_cwslab_5ghz_experiment_environment_20260423T123527Z.scan.txt`
- Survey source: `not available`
- Notes: Repeated ambient 5 GHz environment scan for cws-lab experiments on April 23, 2026 on channel 36 at 20 MHz; experiment AP excluded from interference scoring so the report reflects surrounding radio only.

## Executive Summary

- **2.4 GHz**: `38` APs observed, `2` strong emitters, recommended channels `1, 2, 3`.
- **5 GHz**: `11` APs observed, `3` strong emitters, recommended channels `52, 56, 60`.
- **Focus assessment**: `5 GHz` channel `36` / `20 MHz` maps to interference level `L3` and radio-load level `L2`.

## 5 GHz Experiment Focus

| Metric | Value |
| --- | --- |
| Focus channel | 36 |
| Focus width | 20 MHz |
| Rank within band | 23 |
| 5 GHz block | 36-48 |
| Exact-channel APs | 3 |
| Exact-channel strong APs | 3 |
| Overlapping / same-block APs | 5 |
| Overlapping / same-block strong APs | 3 |
| Strongest exact signal | -58.0 dBm |
| Strongest overlap signal | -58.0 dBm |
| Congestion score | 2.305 |
| Survey busy ratio | n/a |
| Inferred interference level | L3 |
| Inferred radio-load level | L2 |
| Recommended in-band channels | 52, 56, 60 |

Interpretation:
- The channel should be retuned or the environment should be isolated before claiming a clean cws-lab baseline.
- The current channel state should be treated as `L3` for interference and `L2` for radio loading when mapping the lab to `L0-L2` cws-lab assumptions.
- This channel should not be described as a clean `L0` baseline without extra isolation or a channel move.

## Observed Band Results


### 2.4 GHz

| Metric | Value |
| --- | --- |
| AP count | 38 |
| Unique SSID count | 31 |
| Strong-neighbor count | 2 |
| Median signal (dBm) | -86.00 |
| Mean survey busy ratio | n/a |
| Mean noise floor (dBm) | n/a |
| Recommended channels | 1, 2, 3 |

#### Channel Occupancy

| Channel | Exact APs | Exact Strong | Overlap APs | Overlap Strong | Congestion | Strongest Exact | Strongest Overlap | Survey Busy | Noise |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 10 | 0 | 18 | 0 | 0.845 | -82.5 dBm | -76.5 dBm | n/a | n/a |
| 2 | 1 | 0 | 28 | 0 | 1.128 | -89.0 dBm | -73.0 dBm | n/a | n/a |
| 3 | 4 | 0 | 28 | 0 | 1.400 | -77.5 dBm | -73.0 dBm | n/a | n/a |
| 4 | 3 | 0 | 29 | 0 | 1.713 | -76.5 dBm | -73.0 dBm | n/a | n/a |
| 6 | 10 | 0 | 23 | 2 | 2.392 | -73.0 dBm | -50.5 dBm | n/a | n/a |
| 8 | 1 | 0 | 23 | 2 | 2.720 | -84.0 dBm | -50.5 dBm | n/a | n/a |
| 9 | 2 | 2 | 20 | 2 | 2.752 | -50.5 dBm | -50.5 dBm | n/a | n/a |
| 10 | 2 | 0 | 20 | 2 | 2.227 | -80.5 dBm | -50.5 dBm | n/a | n/a |
| 11 | 5 | 0 | 10 | 2 | 1.563 | -86.5 dBm | -50.5 dBm | n/a | n/a |

#### Strongest Nearby APs

| SSID | BSSID | Channel | Signal | Estimated | Last seen |
| --- | --- | --- | --- | --- | --- |
| <hidden> | `5e:62:8b:26:83:e1` | 9 | -50.5 dBm | yes | n/a |
| EOM | `5c:62:8b:36:83:e1` | 9 | -52.5 dBm | yes | n/a |
| A55 Катерина | `6a:8b:e4:1b:1e:7b` | 6 | -73.0 dBm | yes | n/a |
| TP-Link_512 | `f0:09:0d:78:db:c8` | 4 | -76.5 dBm | yes | n/a |
| <hidden> | `f2:09:0d:28:db:c8` | 4 | -77.5 dBm | yes | n/a |

#### Interpretation

- Highest modeled congestion is on channel `9` with score `2.752`.
- Lowest modeled congestion is on channel `1` with score `0.845`.
- Recommended channels for experiments in this band: `1, 2, 3`.
- Airtime utilization counters were not available, so interpretation is driven mainly by neighboring AP presence and signal strength.

### 5 GHz

| Metric | Value |
| --- | --- |
| AP count | 11 |
| Unique SSID count | 7 |
| Strong-neighbor count | 3 |
| Median signal (dBm) | -89.00 |
| Mean survey busy ratio | n/a |
| Mean noise floor (dBm) | n/a |
| Recommended channels | 52, 56, 60 |

#### Channel Occupancy

| Channel | Exact APs | Exact Strong | Overlap APs | Overlap Strong | Congestion | Strongest Exact | Strongest Overlap | Survey Busy | Noise |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 36 | 3 | 3 | 5 | 3 | 2.305 | -58.0 dBm | -58.0 dBm | n/a | n/a |
| 40 | 2 | 0 | 5 | 3 | 1.338 | -88.0 dBm | -58.0 dBm | n/a | n/a |
| 44 | 0 | 0 | 5 | 3 | 0.705 | n/a | -58.0 dBm | n/a | n/a |
| 48 | 0 | 0 | 5 | 3 | 0.705 | n/a | -58.0 dBm | n/a | n/a |
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
| 149 | 3 | 0 | 6 | 0 | 0.195 | -93.0 dBm | -87.5 dBm | n/a | n/a |
| 153 | 0 | 0 | 6 | 0 | 0.128 | n/a | -87.5 dBm | n/a | n/a |
| 157 | 3 | 0 | 6 | 0 | 0.195 | -87.5 dBm | -87.5 dBm | n/a | n/a |
| 161 | 0 | 0 | 6 | 0 | 0.128 | n/a | -87.5 dBm | n/a | n/a |

#### Strongest Nearby APs

| SSID | BSSID | Channel | Signal | Estimated | Last seen |
| --- | --- | --- | --- | --- | --- |
| cwslab-rpi5-exp-5g | `2e:cf:67:d4:44:d5` | 36 | -58.0 dBm | yes | n/a |
| EOM | `5c:62:8b:36:83:e0` | 36 | -61.5 dBm | yes | n/a |
| <hidden> | `5e:62:8b:56:83:e1` | 36 | -61.5 dBm | yes | n/a |
| moto g72_3229 | `ae:e6:3f:28:28:0a` | 157 | -87.5 dBm | yes | n/a |
| TP-Link_512_5G | `f0:09:0d:78:db:ca` | 40 | -88.0 dBm | yes | n/a |

#### Interpretation

- Highest modeled congestion is on channel `36` with score `2.305`.
- Lowest modeled congestion is on channel `52` with score `0.000`.
- Recommended channels for experiments in this band: `52, 56, 60`.
- Airtime utilization counters were not available, so interpretation is driven mainly by neighboring AP presence and signal strength.

## Methodological Limitations

- Signal levels were estimated from `nmcli` quality percentages, so absolute dBm values should be treated as approximate.
- Channel-survey airtime utilization was not available because `nmcli` does not expose `iw survey dump` counters.
- One or more SSID/BSSID filters were applied before interference scoring.
