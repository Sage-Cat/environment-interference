# Scientific Wi-Fi Environment Interference Report

## Abstract

This report characterizes the current laboratory Wi-Fi field with emphasis on `5 GHz` channel `36` at `20 MHz`, which is the planned operating point for `cws-lab`. The target channel currently maps to interference level `L1` and radio-load level `L1`, while the lowest modeled alternatives in-band are `52, 56, 60`.

## Measurement Setup

- Generated at (UTC): `2026-04-20T11:59:22Z`
- Source: `live nmcli repeated collection from interface wlp3s0 (8 scans, 5.0 s interval)`
- Collection backend: `nmcli`
- Location: `Current cws-lab room`
- Strong-neighbor threshold: `-67.0 dBm`
- Scan source: `/home/sagecat/Projects/research-workspace/environment-interference/out/current_cwslab_5ghz_experiment_environment_20260420T115839Z/current_cwslab_5ghz_experiment_environment_20260420T115839Z.scan.txt`
- Survey source: `not available`
- Notes: Repeated ambient 5 GHz environment scan for ongoing cws-lab experiments on channel 36 at 20 MHz; experiment AP excluded from interference scoring so the report reflects surrounding radio only.

## Executive Summary

- **2.4 GHz**: `24` APs observed, `2` strong emitters, recommended channels `1, 2, 3`.
- **5 GHz**: `2` APs observed, `2` strong emitters, recommended channels `52, 56, 60`.
- **Focus assessment**: `5 GHz` channel `36` / `20 MHz` maps to interference level `L1` and radio-load level `L1`.

## 5 GHz Experiment Focus

| Metric | Value |
| --- | --- |
| Focus channel | 36 |
| Focus width | 20 MHz |
| Rank within band | 22 |
| 5 GHz block | 36-48 |
| Exact-channel APs | 0 |
| Exact-channel strong APs | 0 |
| Overlapping / same-block APs | 2 |
| Overlapping / same-block strong APs | 2 |
| Strongest exact signal | n/a |
| Strongest overlap signal | -63.0 dBm |
| Congestion score | 0.825 |
| Survey busy ratio | n/a |
| Inferred interference level | L1 |
| Inferred radio-load level | L1 |
| Recommended in-band channels | 52, 56, 60 |

Interpretation:
- The channel should be retuned or the environment should be isolated before claiming a clean cws-lab baseline.
- The current channel state should be treated as `L1` for interference and `L1` for radio loading when mapping the lab to `L0-L2` cws-lab assumptions.
- This channel should not be described as a clean `L0` baseline without extra isolation or a channel move.

## Observed Band Results


### 2.4 GHz

| Metric | Value |
| --- | --- |
| AP count | 24 |
| Unique SSID count | 21 |
| Strong-neighbor count | 2 |
| Median signal (dBm) | -83.00 |
| Mean survey busy ratio | n/a |
| Mean noise floor (dBm) | n/a |
| Recommended channels | 1, 2, 3 |

#### Channel Occupancy

| Channel | Exact APs | Exact Strong | Overlap APs | Overlap Strong | Congestion | Strongest Exact | Strongest Overlap | Survey Busy | Noise |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 3 | 0 | 7 | 0 | 0.445 | -79.0 dBm | -79.0 dBm | n/a | n/a |
| 2 | 1 | 0 | 17 | 0 | 0.560 | -84.0 dBm | -77.5 dBm | n/a | n/a |
| 3 | 2 | 0 | 19 | 2 | 0.815 | -87.5 dBm | -57.5 dBm | n/a | n/a |
| 4 | 1 | 0 | 19 | 2 | 1.198 | -79.0 dBm | -57.5 dBm | n/a | n/a |
| 6 | 10 | 0 | 18 | 2 | 2.195 | -77.5 dBm | -57.5 dBm | n/a | n/a |
| 7 | 2 | 2 | 19 | 2 | 2.373 | -57.5 dBm | -57.5 dBm | n/a | n/a |
| 9 | 1 | 0 | 17 | 2 | 1.652 | -77.5 dBm | -57.5 dBm | n/a | n/a |
| 10 | 1 | 0 | 17 | 2 | 1.312 | -91.5 dBm | -57.5 dBm | n/a | n/a |
| 11 | 2 | 0 | 7 | 2 | 1.160 | -68.0 dBm | -57.5 dBm | n/a | n/a |
| 12 | 1 | 0 | 5 | 0 | 0.928 | -67.5 dBm | -67.5 dBm | n/a | n/a |

#### Strongest Nearby APs

| SSID | BSSID | Channel | Signal | Estimated | Last seen |
| --- | --- | --- | --- | --- | --- |
| EOM | `5c:62:8b:36:83:e1` | 7 | -57.5 dBm | yes | n/a |
| <hidden> | `5e:62:8b:26:83:e1` | 7 | -60.5 dBm | yes | n/a |
| POCO F4 GT | `66:6e:81:ee:cb:f9` | 12 | -67.5 dBm | yes | n/a |
| Redmi 10C | `ae:86:7b:2c:a9:56` | 11 | -68.0 dBm | yes | n/a |
| MyTenda | `82:4e:26:83:bc:fb` | 6 | -77.5 dBm | yes | n/a |

#### Interpretation

- Highest modeled congestion is on channel `7` with score `2.373`.
- Lowest modeled congestion is on channel `1` with score `0.445`.
- Recommended channels for experiments in this band: `1, 2, 3`.
- Airtime utilization counters were not available, so interpretation is driven mainly by neighboring AP presence and signal strength.

### 5 GHz

| Metric | Value |
| --- | --- |
| AP count | 2 |
| Unique SSID count | 2 |
| Strong-neighbor count | 2 |
| Median signal (dBm) | -63.00 |
| Mean survey busy ratio | n/a |
| Mean noise floor (dBm) | n/a |
| Recommended channels | 52, 56, 60 |

#### Channel Occupancy

| Channel | Exact APs | Exact Strong | Overlap APs | Overlap Strong | Congestion | Strongest Exact | Strongest Overlap | Survey Busy | Noise |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 36 | 0 | 0 | 2 | 2 | 0.825 | n/a | -63.0 dBm | n/a | n/a |
| 40 | 2 | 2 | 2 | 2 | 1.500 | -63.0 dBm | -63.0 dBm | n/a | n/a |
| 44 | 0 | 0 | 2 | 2 | 0.450 | n/a | -63.0 dBm | n/a | n/a |
| 48 | 0 | 0 | 2 | 2 | 0.450 | n/a | -63.0 dBm | n/a | n/a |
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
| EOM | `5c:62:8b:36:83:e0` | 40 | -63.0 dBm | yes | n/a |
| <hidden> | `5e:62:8b:56:83:e1` | 40 | -63.0 dBm | yes | n/a |

#### Interpretation

- Highest modeled congestion is on channel `40` with score `1.500`.
- Lowest modeled congestion is on channel `52` with score `0.000`.
- Recommended channels for experiments in this band: `52, 56, 60`.
- Airtime utilization counters were not available, so interpretation is driven mainly by neighboring AP presence and signal strength.

## Methodological Limitations

- Signal levels were estimated from `nmcli` quality percentages, so absolute dBm values should be treated as approximate.
- Channel-survey airtime utilization was not available because `nmcli` does not expose `iw survey dump` counters.
- One or more SSID/BSSID filters were applied before interference scoring.
