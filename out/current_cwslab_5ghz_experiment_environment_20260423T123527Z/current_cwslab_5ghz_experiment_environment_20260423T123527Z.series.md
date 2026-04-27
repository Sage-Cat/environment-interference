# Repeated 5 GHz Environment Series Report

## Objective

This companion report summarizes repeated ambient Wi-Fi scans for the current 5 GHz cws-lab operating point. It is intended to support experiment-facing channel interpretation rather than a one-shot convenience snapshot.

## Measurement Design

- Generated at (UTC): `2026-04-23T12:36:18Z`
- Interface: `wlp3s0`
- Backend: `nmcli`
- Location: `Current cws-lab room`
- Focus: `5 GHz` channel `36` / `20 MHz`
- Repeat count: `8`
- Inter-scan interval: `5.0 s`
- Strong-neighbor threshold: `-67.0 dBm`
- Aggregate report: `out/current_cwslab_5ghz_experiment_environment_20260423T123527Z/current_cwslab_5ghz_experiment_environment_20260423T123527Z.md`
- Notes: Repeated ambient 5 GHz environment scan for cws-lab experiments on April 23, 2026 on channel 36 at 20 MHz; experiment AP excluded from interference scoring so the report reflects surrounding radio only.
- Exclusions before scoring: SSIDs `cwslab-exp1-main-5g`, BSSIDs `-`

## Experiment-Facing Summary

- Unique 5 GHz BSS observed across series: `11`
- Unique focus-block (36-48) BSS observed across series: `5`
- Focus exact-channel presence ratio: `100.0%`
- Focus exact strong-emitter presence ratio: `100.0%`
- Focus overlap presence ratio: `100.0%`
- Focus overlap strong-emitter presence ratio: `100.0%`
- Mean / median / worst focus congestion score: `2.104` / `2.005` / `2.305`
- Median focus rank in band: `23.0`
- Best repeated-scan alternatives: `52, 56, 60`

## Focus-Block Channel Stability

| Channel | Exact Presence | Exact Strong | Overlap Presence | Overlap Strong | Mean Exact APs | Mean Overlap APs | Mean Congestion | Max Congestion | Strongest Overlap |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 36 | 100.0% | 100.0% | 100.0% | 100.0% | 3.00 | 4.50 | 2.104 | 2.305 | -58.0 dBm |
| 40 | 75.0% | 0.0% | 100.0% | 100.0% | 1.50 | 4.50 | 1.210 | 1.338 | -58.0 dBm |
| 44 | 0.0% | 0.0% | 100.0% | 100.0% | 0.00 | 4.50 | 0.641 | 0.705 | -58.0 dBm |
| 48 | 0.0% | 0.0% | 100.0% | 100.0% | 0.00 | 4.50 | 0.641 | 0.705 | -58.0 dBm |
| 52 | 0.0% | 0.0% | 0.0% | 0.0% | 0.00 | 0.00 | 0.000 | 0.000 | n/a |
| 56 | 0.0% | 0.0% | 0.0% | 0.0% | 0.00 | 0.00 | 0.000 | 0.000 | n/a |
| 60 | 0.0% | 0.0% | 0.0% | 0.0% | 0.00 | 0.00 | 0.000 | 0.000 | n/a |
| 64 | 0.0% | 0.0% | 0.0% | 0.0% | 0.00 | 0.00 | 0.000 | 0.000 | n/a |
| 100 | 0.0% | 0.0% | 0.0% | 0.0% | 0.00 | 0.00 | 0.000 | 0.000 | n/a |
| 104 | 0.0% | 0.0% | 0.0% | 0.0% | 0.00 | 0.00 | 0.000 | 0.000 | n/a |
| 108 | 0.0% | 0.0% | 0.0% | 0.0% | 0.00 | 0.00 | 0.000 | 0.000 | n/a |
| 112 | 0.0% | 0.0% | 0.0% | 0.0% | 0.00 | 0.00 | 0.000 | 0.000 | n/a |
| 116 | 0.0% | 0.0% | 0.0% | 0.0% | 0.00 | 0.00 | 0.000 | 0.000 | n/a |
| 120 | 0.0% | 0.0% | 0.0% | 0.0% | 0.00 | 0.00 | 0.000 | 0.000 | n/a |
| 124 | 0.0% | 0.0% | 0.0% | 0.0% | 0.00 | 0.00 | 0.000 | 0.000 | n/a |
| 128 | 0.0% | 0.0% | 0.0% | 0.0% | 0.00 | 0.00 | 0.000 | 0.000 | n/a |
| 132 | 0.0% | 0.0% | 0.0% | 0.0% | 0.00 | 0.00 | 0.000 | 0.000 | n/a |
| 136 | 0.0% | 0.0% | 0.0% | 0.0% | 0.00 | 0.00 | 0.000 | 0.000 | n/a |
| 140 | 0.0% | 0.0% | 0.0% | 0.0% | 0.00 | 0.00 | 0.000 | 0.000 | n/a |
| 149 | 75.0% | 0.0% | 75.0% | 0.0% | 2.25 | 4.50 | 0.146 | 0.195 | -87.5 dBm |
| 153 | 0.0% | 0.0% | 75.0% | 0.0% | 0.00 | 4.50 | 0.096 | 0.128 | -87.5 dBm |
| 157 | 75.0% | 0.0% | 75.0% | 0.0% | 2.25 | 4.50 | 0.146 | 0.195 | -87.5 dBm |
| 161 | 0.0% | 0.0% | 75.0% | 0.0% | 0.00 | 4.50 | 0.096 | 0.128 | -87.5 dBm |

## Persistent 5 GHz Focus-Block Emitters

| SSID | BSSID | Channel | Observations | Presence | Strongest | Median |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| cwslab-rpi5-exp-5g | `2e:cf:67:d4:44:d5` | 36 | 8 | 100.0% | -58.0 dBm | -58.0 dBm |
| EOM | `5c:62:8b:36:83:e0` | 36 | 8 | 100.0% | -61.5 dBm | -68.0 dBm |
| <hidden> | `5e:62:8b:56:83:e1` | 36 | 8 | 100.0% | -61.5 dBm | -61.5 dBm |
| TP-Link_512_5G | `f0:09:0d:78:db:ca` | 40 | 6 | 75.0% | -88.0 dBm | -88.0 dBm |
| <hidden> | `f2:09:0d:68:db:c8` | 40 | 6 | 75.0% | -89.0 dBm | -89.0 dBm |

## Per-Sample Trace

| Sample | Captured At (UTC) | 2.4 GHz APs | 5 GHz APs | Focus Exact | Focus Overlap | Focus Strong Overlap | Focus Congestion | Focus Rank |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 2026-04-23T12:35:34Z | 37 | 11 | 3 | 5 | 3 | 2.305 | 23 |
| 2 | 2026-04-23T12:35:43Z | 37 | 11 | 3 | 5 | 2 | 2.005 | 23 |
| 3 | 2026-04-23T12:35:48Z | 37 | 11 | 3 | 5 | 2 | 2.005 | 23 |
| 4 | 2026-04-23T12:35:53Z | 37 | 11 | 3 | 5 | 2 | 2.005 | 23 |
| 5 | 2026-04-23T12:35:59Z | 37 | 11 | 3 | 5 | 3 | 2.305 | 23 |
| 6 | 2026-04-23T12:36:04Z | 37 | 11 | 3 | 5 | 2 | 2.005 | 23 |
| 7 | 2026-04-23T12:36:09Z | 23 | 3 | 3 | 3 | 2 | 1.950 | 23 |
| 8 | 2026-04-23T12:36:18Z | 23 | 3 | 3 | 3 | 3 | 2.250 | 23 |

## Interpretation

- The focus block shows repeated external occupancy strong enough that the current 5 GHz operating point should be treated as an active interference surface, not a clean baseline.
- The lowest repeated-scan alternatives were `52, 56, 60`; use them only if the experiment design permits a channel move.
- Methodological warnings inherited from the aggregate report:
  - Signal levels were estimated from `nmcli` quality percentages, so absolute dBm values should be treated as approximate.
  - Channel-survey airtime utilization was not available because `nmcli` does not expose `iw survey dump` counters.
  - One or more SSID/BSSID filters were applied before interference scoring.
