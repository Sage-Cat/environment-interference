# Scientific Wi-Fi Environment Interference Report

## Abstract

This report characterizes the current laboratory Wi-Fi field with emphasis on `5 GHz` channel `36` at `20 MHz`, which is the planned operating point for `cws-lab`. The target channel currently maps to interference level `L3` and radio-load level `L2`, while the lowest modeled alternatives in-band are `52, 56, 60`.

## Measurement Setup

- Generated at (UTC): `2026-05-01T12:21:35Z`
- Source: `live nmcli repeated collection from interface wlp3s0 (8 scans, 5.0 s interval)`
- Collection backend: `nmcli`
- Location: `CWS Lab D07-D09 AP-enabled setup`
- Strong-neighbor threshold: `-67.0 dBm`
- Scan source: `out/current_cwslab_d07_d09_ap_enabled_environment_20260501T122056Z/current_cwslab_d07_d09_5ghz_ap_enabled_environment_20260501T122056Z/current_cwslab_d07_d09_5ghz_ap_enabled_environment_20260501T122056Z.scan.txt`
- Survey source: `not available`
- Notes: AP-enabled D07-D09 measurement. Lab APs are intentionally included in raw scans and scoring to characterize the live radio surface with all experiment APs enabled.

## Executive Summary

- **2.4 GHz**: `27` APs observed, `7` strong emitters, recommended channels `11, 1, 2`.
- **5 GHz**: `6` APs observed, `4` strong emitters, recommended channels `52, 56, 60`.
- **Focus assessment**: `5 GHz` channel `36` / `20 MHz` maps to interference level `L3` and radio-load level `L2`.

## 5 GHz Experiment Focus

| Metric | Value |
| --- | --- |
| Focus channel | 36 |
| Focus width | 20 MHz |
| Rank within band | 23 |
| 5 GHz block | 36-48 |
| Exact-channel APs | 4 |
| Exact-channel strong APs | 4 |
| Overlapping / same-block APs | 6 |
| Overlapping / same-block strong APs | 4 |
| Strongest exact signal | -50.0 dBm |
| Strongest overlap signal | -50.0 dBm |
| Congestion score | 4.195 |
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
| AP count | 27 |
| Unique SSID count | 22 |
| Strong-neighbor count | 7 |
| Median signal (dBm) | -83.00 |
| Mean survey busy ratio | n/a |
| Mean noise floor (dBm) | n/a |
| Recommended channels | 11, 1, 2 |

#### Channel Occupancy

| Channel | Exact APs | Exact Strong | Overlap APs | Overlap Strong | Congestion | Strongest Exact | Strongest Overlap | Survey Busy | Noise |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 3 | 1 | 13 | 3 | 1.623 | -60.5 dBm | -60.5 dBm | n/a | n/a |
| 2 | 3 | 0 | 19 | 5 | 2.230 | -84.0 dBm | -50.0 dBm | n/a | n/a |
| 3 | 1 | 0 | 21 | 7 | 3.183 | -81.5 dBm | -50.0 dBm | n/a | n/a |
| 4 | 3 | 0 | 22 | 7 | 4.280 | -74.0 dBm | -50.0 dBm | n/a | n/a |
| 5 | 3 | 2 | 22 | 7 | 5.213 | -65.5 dBm | -50.0 dBm | n/a | n/a |
| 6 | 6 | 2 | 19 | 6 | 5.355 | -50.0 dBm | -50.0 dBm | n/a | n/a |
| 7 | 2 | 2 | 21 | 6 | 4.605 | -52.5 dBm | -50.0 dBm | n/a | n/a |
| 8 | 1 | 0 | 20 | 6 | 3.150 | -82.5 dBm | -50.0 dBm | n/a | n/a |
| 11 | 5 | 0 | 8 | 2 | 0.438 | -85.5 dBm | -52.5 dBm | n/a | n/a |

#### Strongest Nearby APs

| SSID | BSSID | Channel | Signal | Estimated | Last seen |
| --- | --- | --- | --- | --- | --- |
| cwslab-rpi5-node-c-24g | `2e:cf:67:b4:c1:66` | 6 | -50.0 dBm | yes | n/a |
| EOM | `5c:62:8b:36:83:e1` | 7 | -52.5 dBm | yes | n/a |
| <hidden> | `5e:62:8b:26:83:e1` | 7 | -57.5 dBm | yes | n/a |
| dlink-rustview | `00:24:01:bc:42:e5` | 6 | -60.0 dBm | yes | n/a |
| 1e5911a8 | `f4:91:1e:59:11:a8` | 1 | -60.5 dBm | yes | n/a |

#### Interpretation

- Highest modeled congestion is on channel `6` with score `5.355`.
- Lowest modeled congestion is on channel `11` with score `0.438`.
- Recommended channels for experiments in this band: `11, 1, 2`.
- Airtime utilization counters were not available, so interpretation is driven mainly by neighboring AP presence and signal strength.

### 5 GHz

| Metric | Value |
| --- | --- |
| AP count | 6 |
| Unique SSID count | 5 |
| Strong-neighbor count | 4 |
| Median signal (dBm) | -54.50 |
| Mean survey busy ratio | n/a |
| Mean noise floor (dBm) | n/a |
| Recommended channels | 52, 56, 60 |

#### Channel Occupancy

| Channel | Exact APs | Exact Strong | Overlap APs | Overlap Strong | Congestion | Strongest Exact | Strongest Overlap | Survey Busy | Noise |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 36 | 4 | 4 | 6 | 4 | 4.195 | -50.0 dBm | -50.0 dBm | n/a | n/a |
| 40 | 0 | 0 | 6 | 4 | 2.395 | n/a | -50.0 dBm | n/a | n/a |
| 44 | 2 | 0 | 6 | 4 | 1.850 | -75.0 dBm | -50.0 dBm | n/a | n/a |
| 48 | 0 | 0 | 6 | 4 | 1.558 | n/a | -50.0 dBm | n/a | n/a |
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
| <hidden> | `5e:62:8b:56:83:e1` | 36 | -54.0 dBm | yes | n/a |
| EOM | `5c:62:8b:36:83:e0` | 36 | -55.0 dBm | yes | n/a |
| <hidden> | `42:ed:00:53:bc:de` | 44 | -75.0 dBm | yes | n/a |

#### Interpretation

- Highest modeled congestion is on channel `36` with score `4.195`.
- Lowest modeled congestion is on channel `52` with score `0.000`.
- Recommended channels for experiments in this band: `52, 56, 60`.
- Airtime utilization counters were not available, so interpretation is driven mainly by neighboring AP presence and signal strength.

## Methodological Limitations

- Signal levels were estimated from `nmcli` quality percentages, so absolute dBm values should be treated as approximate.
- Channel-survey airtime utilization was not available because `nmcli` does not expose `iw survey dump` counters.
