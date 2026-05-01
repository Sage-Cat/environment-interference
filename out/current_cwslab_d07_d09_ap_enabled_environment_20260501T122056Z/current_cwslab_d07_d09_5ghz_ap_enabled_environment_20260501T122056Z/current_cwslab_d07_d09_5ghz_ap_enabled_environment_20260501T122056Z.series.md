# Repeated 5 GHz Environment Series Report

## Objective

This companion report summarizes repeated ambient Wi-Fi scans for the current 5 GHz cws-lab operating point. It is intended to support experiment-facing channel interpretation rather than a one-shot convenience snapshot.

## Measurement Design

- Generated at (UTC): `2026-05-01T12:21:35Z`
- Interface: `wlp3s0`
- Backend: `nmcli`
- Location: `CWS Lab D07-D09 AP-enabled setup`
- Focus: `5 GHz` channel `36` / `20 MHz`
- Repeat count: `8`
- Inter-scan interval: `5.0 s`
- Strong-neighbor threshold: `-67.0 dBm`
- Aggregate report: `out/current_cwslab_d07_d09_ap_enabled_environment_20260501T122056Z/current_cwslab_d07_d09_5ghz_ap_enabled_environment_20260501T122056Z/current_cwslab_d07_d09_5ghz_ap_enabled_environment_20260501T122056Z.md`
- Notes: AP-enabled D07-D09 measurement. Lab APs are intentionally included in raw scans and scoring to characterize the live radio surface with all experiment APs enabled.

## Experiment-Facing Summary

- Unique 5 GHz BSS observed across series: `6`
- Unique focus-block (36-48) BSS observed across series: `6`
- Focus exact-channel presence ratio: `100.0%`
- Focus exact strong-emitter presence ratio: `100.0%`
- Focus overlap presence ratio: `100.0%`
- Focus overlap strong-emitter presence ratio: `100.0%`
- Mean / median / worst focus congestion score: `3.942` / `3.870` / `4.195`
- Median focus rank in band: `23.0`
- Best repeated-scan alternatives: `52, 56, 60`

## Focus-Block Channel Stability

| Channel | Exact Presence | Exact Strong | Overlap Presence | Overlap Strong | Mean Exact APs | Mean Overlap APs | Mean Congestion | Max Congestion | Strongest Overlap |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 36 | 100.0% | 100.0% | 100.0% | 100.0% | 4.00 | 6.00 | 3.942 | 4.195 | -50.0 dBm |
| 40 | 0.0% | 0.0% | 100.0% | 100.0% | 0.00 | 6.00 | 2.227 | 2.395 | -50.0 dBm |
| 44 | 100.0% | 0.0% | 100.0% | 100.0% | 2.00 | 6.00 | 1.575 | 1.850 | -50.0 dBm |
| 48 | 0.0% | 0.0% | 100.0% | 100.0% | 0.00 | 6.00 | 1.381 | 1.558 | -50.0 dBm |
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
| 149 | 0.0% | 0.0% | 0.0% | 0.0% | 0.00 | 0.00 | 0.000 | 0.000 | n/a |
| 153 | 0.0% | 0.0% | 0.0% | 0.0% | 0.00 | 0.00 | 0.000 | 0.000 | n/a |
| 157 | 0.0% | 0.0% | 0.0% | 0.0% | 0.00 | 0.00 | 0.000 | 0.000 | n/a |
| 161 | 0.0% | 0.0% | 0.0% | 0.0% | 0.00 | 0.00 | 0.000 | 0.000 | n/a |

## Persistent 5 GHz Focus-Block Emitters

| SSID | BSSID | Channel | Observations | Presence | Strongest | Median |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| cwslab-exp1-main-5g | `1e:f4:3f:f0:3d:a7` | 36 | 8 | 100.0% | -50.0 dBm | -50.0 dBm |
| cwslab-rpi5-exp-5g | `2e:cf:67:d4:44:d5` | 36 | 8 | 100.0% | -51.5 dBm | -52.5 dBm |
| <hidden> | `5e:62:8b:56:83:e1` | 36 | 8 | 100.0% | -54.0 dBm | -54.0 dBm |
| EOM | `5c:62:8b:36:83:e0` | 36 | 8 | 100.0% | -55.0 dBm | -63.5 dBm |
| <hidden> | `42:ed:00:53:bc:de` | 44 | 8 | 100.0% | -75.0 dBm | -75.5 dBm |
| EOM_5Ghz | `40:ed:00:63:bc:e0` | 44 | 8 | 100.0% | -75.5 dBm | -75.5 dBm |

## Per-Sample Trace

| Sample | Captured At (UTC) | 2.4 GHz APs | 5 GHz APs | Focus Exact | Focus Overlap | Focus Strong Overlap | Focus Congestion | Focus Rank |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 2026-05-01T12:20:56Z | 19 | 6 | 4 | 6 | 4 | 3.870 | 23 |
| 2 | 2026-05-01T12:21:01Z | 25 | 6 | 4 | 6 | 4 | 4.120 | 23 |
| 3 | 2026-05-01T12:21:06Z | 25 | 6 | 4 | 6 | 4 | 3.870 | 23 |
| 4 | 2026-05-01T12:21:11Z | 25 | 6 | 4 | 6 | 4 | 3.870 | 23 |
| 5 | 2026-05-01T12:21:16Z | 25 | 6 | 4 | 6 | 4 | 3.870 | 23 |
| 6 | 2026-05-01T12:21:21Z | 25 | 6 | 4 | 6 | 4 | 3.870 | 23 |
| 7 | 2026-05-01T12:21:26Z | 25 | 6 | 4 | 6 | 4 | 3.870 | 23 |
| 8 | 2026-05-01T12:21:31Z | 27 | 6 | 4 | 6 | 4 | 4.195 | 23 |

## Interpretation

- The focus block shows repeated external occupancy strong enough that the current 5 GHz operating point should be treated as an active interference surface, not a clean baseline.
- The lowest repeated-scan alternatives were `52, 56, 60`; use them only if the experiment design permits a channel move.
- Methodological warnings inherited from the aggregate report:
  - Signal levels were estimated from `nmcli` quality percentages, so absolute dBm values should be treated as approximate.
  - Channel-survey airtime utilization was not available because `nmcli` does not expose `iw survey dump` counters.
