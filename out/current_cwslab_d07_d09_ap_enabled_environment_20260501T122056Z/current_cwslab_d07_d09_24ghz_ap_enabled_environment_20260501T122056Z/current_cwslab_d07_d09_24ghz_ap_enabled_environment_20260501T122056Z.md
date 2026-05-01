# Scientific Wi-Fi Environment Interference Report

## Abstract

This report characterizes the current laboratory Wi-Fi field with emphasis on `2.4 GHz` channel `6` at `20 MHz`, which is the planned operating point for `cws-lab`. The target channel currently maps to interference level `L3` and radio-load level `L2`, while the lowest modeled alternatives in-band are `11, 1, 2`.

## Measurement Setup

- Generated at (UTC): `2026-05-01T12:22:11Z`
- Source: `live nmcli repeated collection from interface wlp3s0 (8 scans, 5.0 s interval)`
- Collection backend: `nmcli`
- Location: `CWS Lab D07-D09 AP-enabled setup`
- Strong-neighbor threshold: `-67.0 dBm`
- Scan source: `out/current_cwslab_d07_d09_ap_enabled_environment_20260501T122056Z/current_cwslab_d07_d09_24ghz_ap_enabled_environment_20260501T122056Z/current_cwslab_d07_d09_24ghz_ap_enabled_environment_20260501T122056Z.scan.txt`
- Survey source: `not available`
- Notes: AP-enabled D07-D09 measurement. Lab APs are intentionally included in raw scans and scoring to characterize the live Node-C/T2 2.4 GHz surface with all experiment APs enabled.

## Executive Summary

- **2.4 GHz**: `28` APs observed, `6` strong emitters, recommended channels `11, 1, 2`.
- **5 GHz**: `6` APs observed, `4` strong emitters, recommended channels `52, 56, 60`.
- **Focus assessment**: `2.4 GHz` channel `6` / `20 MHz` maps to interference level `L3` and radio-load level `L2`.

## 2.4 GHz Experiment Focus

| Metric | Value |
| --- | --- |
| Focus channel | 6 |
| Focus width | 20 MHz |
| Rank within band | 9 |
| 5 GHz block | n/a |
| Exact-channel APs | 6 |
| Exact-channel strong APs | 2 |
| Overlapping / same-block APs | 20 |
| Overlapping / same-block strong APs | 6 |
| Strongest exact signal | -50.0 dBm |
| Strongest overlap signal | -50.0 dBm |
| Congestion score | 5.360 |
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
| AP count | 28 |
| Unique SSID count | 23 |
| Strong-neighbor count | 6 |
| Median signal (dBm) | -83.50 |
| Mean survey busy ratio | n/a |
| Mean noise floor (dBm) | n/a |
| Recommended channels | 11, 1, 2 |

#### Channel Occupancy

| Channel | Exact APs | Exact Strong | Overlap APs | Overlap Strong | Congestion | Strongest Exact | Strongest Overlap | Survey Busy | Noise |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 3 | 0 | 14 | 2 | 1.363 | -74.0 dBm | -66.5 dBm | n/a | n/a |
| 2 | 4 | 0 | 20 | 4 | 2.040 | -84.0 dBm | -50.0 dBm | n/a | n/a |
| 3 | 1 | 0 | 22 | 6 | 3.058 | -81.5 dBm | -50.0 dBm | n/a | n/a |
| 4 | 3 | 0 | 23 | 6 | 4.232 | -73.0 dBm | -50.0 dBm | n/a | n/a |
| 5 | 3 | 2 | 23 | 6 | 5.195 | -66.5 dBm | -50.0 dBm | n/a | n/a |
| 6 | 6 | 2 | 20 | 6 | 5.360 | -50.0 dBm | -50.0 dBm | n/a | n/a |
| 7 | 2 | 2 | 21 | 6 | 4.605 | -52.5 dBm | -50.0 dBm | n/a | n/a |
| 8 | 1 | 0 | 20 | 6 | 3.150 | -83.0 dBm | -50.0 dBm | n/a | n/a |
| 11 | 5 | 0 | 8 | 2 | 0.438 | -85.0 dBm | -52.5 dBm | n/a | n/a |

#### Strongest Nearby APs

| SSID | BSSID | Channel | Signal | Estimated | Last seen |
| --- | --- | --- | --- | --- | --- |
| cwslab-rpi5-node-c-24g | `2e:cf:67:b4:c1:66` | 6 | -50.0 dBm | yes | n/a |
| EOM | `5c:62:8b:36:83:e1` | 7 | -52.5 dBm | yes | n/a |
| <hidden> | `5e:62:8b:26:83:e1` | 7 | -55.5 dBm | yes | n/a |
| dlink-rustview | `00:24:01:bc:42:e5` | 6 | -60.0 dBm | yes | n/a |
| EOM | `40:ed:00:63:bc:de` | 5 | -66.5 dBm | yes | n/a |

#### Interpretation

- Highest modeled congestion is on channel `6` with score `5.360`.
- Lowest modeled congestion is on channel `11` with score `0.438`.
- Recommended channels for experiments in this band: `11, 1, 2`.
- Airtime utilization counters were not available, so interpretation is driven mainly by neighboring AP presence and signal strength.

### 5 GHz

| Metric | Value |
| --- | --- |
| AP count | 6 |
| Unique SSID count | 5 |
| Strong-neighbor count | 4 |
| Median signal (dBm) | -54.00 |
| Mean survey busy ratio | n/a |
| Mean noise floor (dBm) | n/a |
| Recommended channels | 52, 56, 60 |

#### Channel Occupancy

| Channel | Exact APs | Exact Strong | Overlap APs | Overlap Strong | Congestion | Strongest Exact | Strongest Overlap | Survey Busy | Noise |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 36 | 4 | 4 | 6 | 4 | 4.270 | -50.0 dBm | -50.0 dBm | n/a | n/a |
| 40 | 0 | 0 | 6 | 4 | 2.470 | n/a | -50.0 dBm | n/a | n/a |
| 44 | 2 | 0 | 6 | 4 | 2.100 | -75.0 dBm | -50.0 dBm | n/a | n/a |
| 48 | 0 | 0 | 6 | 4 | 1.695 | n/a | -50.0 dBm | n/a | n/a |
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
| cwslab-exp1-main-5g | `1e:f4:3f:f0:3d:a7` | 36 | -50.0 dBm | yes | n/a |
| cwslab-rpi5-exp-5g | `2e:cf:67:d4:44:d5` | 36 | -51.5 dBm | yes | n/a |
| <hidden> | `5e:62:8b:56:83:e1` | 36 | -53.0 dBm | yes | n/a |
| EOM | `5c:62:8b:36:83:e0` | 36 | -55.0 dBm | yes | n/a |
| <hidden> | `42:ed:00:53:bc:de` | 44 | -75.0 dBm | yes | n/a |

#### Interpretation

- Highest modeled congestion is on channel `36` with score `4.270`.
- Lowest modeled congestion is on channel `52` with score `0.000`.
- Recommended channels for experiments in this band: `52, 56, 60`.
- Airtime utilization counters were not available, so interpretation is driven mainly by neighboring AP presence and signal strength.

## Methodological Limitations

- Signal levels were estimated from `nmcli` quality percentages, so absolute dBm values should be treated as approximate.
- Channel-survey airtime utilization was not available because `nmcli` does not expose `iw survey dump` counters.
