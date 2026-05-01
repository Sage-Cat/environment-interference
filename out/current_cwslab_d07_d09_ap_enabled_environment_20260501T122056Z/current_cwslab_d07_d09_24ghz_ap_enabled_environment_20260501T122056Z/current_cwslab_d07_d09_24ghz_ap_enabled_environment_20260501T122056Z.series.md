# Repeated 5 GHz Environment Series Report

## Objective

This companion report summarizes repeated ambient Wi-Fi scans for the current 5 GHz cws-lab operating point. It is intended to support experiment-facing channel interpretation rather than a one-shot convenience snapshot.

## Measurement Design

- Generated at (UTC): `2026-05-01T12:22:11Z`
- Interface: `wlp3s0`
- Backend: `nmcli`
- Location: `CWS Lab D07-D09 AP-enabled setup`
- Focus: `2.4 GHz` channel `6` / `20 MHz`
- Repeat count: `8`
- Inter-scan interval: `5.0 s`
- Strong-neighbor threshold: `-67.0 dBm`
- Aggregate report: `out/current_cwslab_d07_d09_ap_enabled_environment_20260501T122056Z/current_cwslab_d07_d09_24ghz_ap_enabled_environment_20260501T122056Z/current_cwslab_d07_d09_24ghz_ap_enabled_environment_20260501T122056Z.md`
- Notes: AP-enabled D07-D09 measurement. Lab APs are intentionally included in raw scans and scoring to characterize the live Node-C/T2 2.4 GHz surface with all experiment APs enabled.

## Experiment-Facing Summary

- Unique 5 GHz BSS observed across series: `6`
- Unique focus-block (n/a) BSS observed across series: `6`
- Focus exact-channel presence ratio: `100.0%`
- Focus exact strong-emitter presence ratio: `100.0%`
- Focus overlap presence ratio: `100.0%`
- Focus overlap strong-emitter presence ratio: `100.0%`
- Mean / median / worst focus congestion score: `4.673` / `4.445` / `5.355`
- Median focus rank in band: `9.0`
- Best repeated-scan alternatives: `11, 1, 2`

## Focus-Block Channel Stability

| Channel | Exact Presence | Exact Strong | Overlap Presence | Overlap Strong | Mean Exact APs | Mean Overlap APs | Mean Congestion | Max Congestion | Strongest Overlap |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 100.0% | 0.0% | 100.0% | 25.0% | 3.00 | 10.75 | 1.097 | 1.323 | -66.5 dBm |
| 2 | 100.0% | 0.0% | 100.0% | 100.0% | 2.25 | 15.25 | 1.548 | 1.990 | -50.0 dBm |
| 3 | 100.0% | 0.0% | 100.0% | 100.0% | 1.00 | 17.25 | 2.318 | 3.018 | -50.0 dBm |
| 4 | 100.0% | 0.0% | 100.0% | 100.0% | 2.25 | 18.25 | 3.325 | 4.205 | -50.0 dBm |
| 5 | 100.0% | 25.0% | 100.0% | 100.0% | 2.25 | 18.25 | 4.294 | 5.183 | -50.0 dBm |
| 6 | 100.0% | 100.0% | 100.0% | 100.0% | 4.50 | 15.25 | 4.673 | 5.355 | -50.0 dBm |
| 7 | 100.0% | 100.0% | 100.0% | 100.0% | 2.00 | 17.25 | 4.178 | 4.605 | -50.0 dBm |
| 8 | 100.0% | 0.0% | 100.0% | 100.0% | 1.00 | 16.25 | 2.944 | 3.150 | -50.0 dBm |
| 11 | 100.0% | 0.0% | 100.0% | 100.0% | 4.25 | 7.25 | 0.401 | 0.438 | -52.5 dBm |

## Persistent 5 GHz Focus-Block Emitters

| SSID | BSSID | Channel | Observations | Presence | Strongest | Median |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| cwslab-rpi5-node-c-24g | `2e:cf:67:b4:c1:66` | 6 | 8 | 100.0% | -50.0 dBm | -50.0 dBm |
| dlink-rustview | `00:24:01:bc:42:e5` | 6 | 8 | 100.0% | -60.0 dBm | -60.0 dBm |
| Nest | `c6:b2:5b:86:2f:45` | 6 | 8 | 100.0% | -78.0 dBm | -79.0 dBm |
| TP-LINK_AD1C | `18:d6:c7:71:ad:1c` | 6 | 8 | 100.0% | -87.5 dBm | -87.5 dBm |
| KRISHOME | `50:c7:bf:25:36:3c` | 6 | 2 | 25.0% | -92.5 dBm | -92.5 dBm |
| <epam-lab> | `e8:ed:f3:ea:1d:c0` | 6 | 2 | 25.0% | -94.0 dBm | -94.0 dBm |

## Per-Sample Trace

| Sample | Captured At (UTC) | 2.4 GHz APs | 5 GHz APs | Focus Exact | Focus Overlap | Focus Strong Overlap | Focus Congestion | Focus Rank |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 2026-05-01T12:21:35Z | 27 | 6 | 6 | 19 | 6 | 5.355 | 9 |
| 2 | 2026-05-01T12:21:40Z | 27 | 6 | 6 | 19 | 6 | 5.355 | 9 |
| 3 | 2026-05-01T12:21:46Z | 21 | 6 | 4 | 14 | 4 | 4.445 | 9 |
| 4 | 2026-05-01T12:21:51Z | 21 | 6 | 4 | 14 | 4 | 4.445 | 9 |
| 5 | 2026-05-01T12:21:56Z | 21 | 6 | 4 | 14 | 4 | 4.445 | 9 |
| 6 | 2026-05-01T12:22:01Z | 21 | 6 | 4 | 14 | 4 | 4.445 | 9 |
| 7 | 2026-05-01T12:22:06Z | 21 | 6 | 4 | 14 | 4 | 4.445 | 9 |
| 8 | 2026-05-01T12:22:11Z | 21 | 6 | 4 | 14 | 4 | 4.445 | 9 |

## Interpretation

- The focus block shows repeated external occupancy strong enough that the current 5 GHz operating point should be treated as an active interference surface, not a clean baseline.
- The lowest repeated-scan alternatives were `11, 1, 2`; use them only if the experiment design permits a channel move.
- Methodological warnings inherited from the aggregate report:
  - Signal levels were estimated from `nmcli` quality percentages, so absolute dBm values should be treated as approximate.
  - Channel-survey airtime utilization was not available because `nmcli` does not expose `iw survey dump` counters.
