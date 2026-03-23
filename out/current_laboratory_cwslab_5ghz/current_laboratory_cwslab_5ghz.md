# Scientific Wi-Fi Environment Interference Report

## Abstract

This report characterizes the current laboratory Wi-Fi field with emphasis on `5 GHz` channel `36` at `20 MHz`, which is the planned operating point for `cws-lab`. The target channel currently maps to interference level `L1` and radio-load level `L1`, while the lowest modeled alternatives in-band are `52, 56, 60`.

## Measurement Setup

- Generated at (UTC): `2026-03-23T10:27:44Z`
- Source: `live nmcli collection from interface wlp3s0`
- Collection backend: `nmcli`
- Location: `Current laboratory`
- Strong-neighbor threshold: `-67.0 dBm`
- Scan source: `out/current_laboratory_cwslab_5ghz/current_laboratory_cwslab_5ghz.scan.txt`
- Survey source: `not available`
- Notes: Pre-experiment 5 GHz lab-state survey for cws-lab; target configuration 5 GHz / channel 36 / 20 MHz; interpret baseline against L0-L2.

## Executive Summary

- **2.4 GHz**: `22` APs observed, `0` strong emitters, recommended channels `13, 11, 9`.
- **5 GHz**: `4` APs observed, `0` strong emitters, recommended channels `52, 56, 60`.
- **Focus assessment**: `5 GHz` channel `36` / `20 MHz` maps to interference level `L1` and radio-load level `L1`.

## 5 GHz Experiment Focus

| Metric | Value |
| --- | --- |
| Focus channel | 36 |
| Focus width | 20 MHz |
| Rank within band | 20 |
| 5 GHz block | 36-48 |
| Exact-channel APs | 0 |
| Exact-channel strong APs | 0 |
| Overlapping / same-block APs | 4 |
| Overlapping / same-block strong APs | 0 |
| Strongest exact signal | n/a |
| Strongest overlap signal | -69.5 dBm |
| Congestion score | 0.205 |
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
| AP count | 22 |
| Unique SSID count | 17 |
| Strong-neighbor count | 0 |
| Median signal (dBm) | n/a |
| Mean survey busy ratio | n/a |
| Mean noise floor (dBm) | n/a |
| Recommended channels | 13, 11, 9 |

#### Channel Occupancy

| Channel | Exact APs | Exact Strong | Overlap APs | Overlap Strong | Congestion | Strongest Exact | Strongest Overlap | Survey Busy | Noise |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 4 | 0 | 9 | 0 | 0.335 | n/a | n/a | n/a | n/a |
| 2 | 1 | 0 | 14 | 0 | 0.383 | n/a | n/a | n/a | n/a |
| 3 | 3 | 0 | 14 | 0 | 0.403 | n/a | n/a | n/a | n/a |
| 4 | 1 | 0 | 15 | 0 | 0.390 | n/a | n/a | n/a | n/a |
| 6 | 5 | 0 | 13 | 0 | 0.373 | n/a | n/a | n/a | n/a |
| 8 | 1 | 0 | 12 | 0 | 0.310 | n/a | n/a | n/a | n/a |
| 9 | 2 | 0 | 13 | 0 | 0.295 | n/a | n/a | n/a | n/a |
| 11 | 3 | 0 | 8 | 0 | 0.273 | n/a | n/a | n/a | n/a |
| 13 | 2 | 0 | 7 | 0 | 0.193 | n/a | n/a | n/a | n/a |

#### Strongest Nearby APs

No APs detected in this band.

#### Interpretation

- Highest modeled congestion is on channel `3` with score `0.403`.
- Lowest modeled congestion is on channel `13` with score `0.193`.
- Recommended channels for experiments in this band: `13, 11, 9`.
- Airtime utilization counters were not available, so interpretation is driven mainly by neighboring AP presence and signal strength.

### 5 GHz

| Metric | Value |
| --- | --- |
| AP count | 4 |
| Unique SSID count | 3 |
| Strong-neighbor count | 0 |
| Median signal (dBm) | -69.50 |
| Mean survey busy ratio | n/a |
| Mean noise floor (dBm) | n/a |
| Recommended channels | 52, 56, 60 |

#### Channel Occupancy

| Channel | Exact APs | Exact Strong | Overlap APs | Overlap Strong | Congestion | Strongest Exact | Strongest Overlap | Survey Busy | Noise |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 36 | 0 | 0 | 4 | 0 | 0.205 | n/a | -69.5 dBm | n/a | n/a |
| 40 | 2 | 0 | 4 | 0 | 0.250 | n/a | -69.5 dBm | n/a | n/a |
| 44 | 2 | 0 | 4 | 0 | 0.530 | -69.5 dBm | -69.5 dBm | n/a | n/a |
| 48 | 0 | 0 | 4 | 0 | 0.305 | n/a | -69.5 dBm | n/a | n/a |
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
| EOM | `5c:62:8b:36:83:e0` | 44 | -69.5 dBm | yes | n/a |

#### Interpretation

- Highest modeled congestion is on channel `44` with score `0.530`.
- Lowest modeled congestion is on channel `52` with score `0.000`.
- Recommended channels for experiments in this band: `52, 56, 60`.
- Airtime utilization counters were not available, so interpretation is driven mainly by neighboring AP presence and signal strength.

## Methodological Limitations

- Signal levels were estimated from `nmcli` quality percentages, so absolute dBm values should be treated as approximate.
- Channel-survey airtime utilization was not available because `nmcli` does not expose `iw survey dump` counters.
