# Repeated 5 GHz Environment Series Report

## Objective

This companion report summarizes repeated ambient Wi-Fi scans for the current 5 GHz cws-lab operating point. It is intended to support experiment-facing channel interpretation rather than a one-shot convenience snapshot.

## Measurement Design

- Generated at (UTC): `2026-04-27T09:28:55Z`
- Interface: `wlp3s0`
- Backend: `nmcli`
- Location: `cws-lab D05-D09 experiment environment, external 2.4 GHz view`
- Focus: `2.4 GHz` channel `6` / `20 MHz`
- Repeat count: `8`
- Inter-scan interval: `5.0 s`
- Strong-neighbor threshold: `-67.0 dBm`
- Aggregate report: `out/current_cwslab_d05_d09_24ghz_external_environment_20260427T092816Z/current_cwslab_d05_d09_24ghz_external_environment_20260427T092816Z.md`
- Notes: Ambient pre-experiment environment measurement for D05-D09. Focus is the Node-C/T2 support operating point used by D07/D09: 2.4 GHz, channel 6, 20 MHz. Known cws-lab SSIDs are excluded from interference scoring to estimate external background.
- Exclusions before scoring: SSIDs `cwslab-rpi5-node-c-24g, cwslab-rpi5-mgmt-24g, cwslab-rpi4-mgmt-24g`, BSSIDs `-`

## Experiment-Facing Summary

- Unique 5 GHz BSS observed across series: `4`
- Unique focus-block (n/a) BSS observed across series: `5`
- Focus exact-channel presence ratio: `100.0%`
- Focus exact strong-emitter presence ratio: `0.0%`
- Focus overlap presence ratio: `100.0%`
- Focus overlap strong-emitter presence ratio: `100.0%`
- Mean / median / worst focus congestion score: `1.472` / `1.472` / `1.557`
- Median focus rank in band: `7.5`
- Best repeated-scan alternatives: `13, 1, 3`

## Focus-Block Channel Stability

| Channel | Exact Presence | Exact Strong | Overlap Presence | Overlap Strong | Mean Exact APs | Mean Overlap APs | Mean Congestion | Max Congestion | Strongest Overlap |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 100.0% | 0.0% | 100.0% | 0.0% | 4.50 | 12.00 | 0.655 | 0.938 | -75.0 dBm |
| 2 | 50.0% | 0.0% | 50.0% | 0.0% | 2.00 | 18.00 | 1.178 | 1.178 | -75.0 dBm |
| 3 | 100.0% | 0.0% | 100.0% | 0.0% | 1.50 | 16.00 | 1.094 | 1.333 | -75.0 dBm |
| 4 | 100.0% | 0.0% | 100.0% | 0.0% | 4.00 | 16.50 | 1.274 | 1.460 | -75.0 dBm |
| 5 | 100.0% | 0.0% | 100.0% | 100.0% | 1.00 | 18.50 | 1.355 | 1.482 | -53.0 dBm |
| 6 | 100.0% | 0.0% | 100.0% | 100.0% | 4.00 | 14.00 | 1.472 | 1.557 | -53.0 dBm |
| 8 | 50.0% | 0.0% | 50.0% | 50.0% | 1.00 | 14.00 | 1.828 | 1.828 | -54.0 dBm |
| 9 | 100.0% | 100.0% | 100.0% | 100.0% | 2.00 | 9.50 | 2.058 | 2.135 | -53.0 dBm |
| 11 | 50.0% | 0.0% | 100.0% | 100.0% | 1.00 | 4.50 | 1.115 | 1.128 | -53.0 dBm |
| 13 | 100.0% | 0.0% | 100.0% | 100.0% | 1.00 | 4.00 | 0.265 | 0.280 | -53.0 dBm |

## Persistent 5 GHz Focus-Block Emitters

| SSID | BSSID | Channel | Observations | Presence | Strongest | Median |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| OPPO A74 | `46:6a:f2:83:51:5a` | 6 | 8 | 100.0% | -77.5 dBm | -79.5 dBm |
| lleh fo esiR | `72:c2:bb:7d:b1:6c` | 6 | 8 | 100.0% | -81.5 dBm | -81.5 dBm |
| dudjfb | `4e:45:75:e0:15:60` | 6 | 8 | 100.0% | -82.5 dBm | -82.5 dBm |
| <hidden> | `c6:b2:5b:d6:2f:45` | 6 | 4 | 50.0% | -82.5 dBm | -82.5 dBm |
| ZTE_25631B | `b8:d4:bc:25:63:1b` | 6 | 4 | 50.0% | -84.0 dBm | -84.0 dBm |

## Per-Sample Trace

| Sample | Captured At (UTC) | 2.4 GHz APs | 5 GHz APs | Focus Exact | Focus Overlap | Focus Strong Overlap | Focus Congestion | Focus Rank |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 2026-04-27T09:28:16Z | 20 | 2 | 4 | 14 | 2 | 1.388 | 7 |
| 2 | 2026-04-27T09:28:21Z | 20 | 2 | 4 | 14 | 2 | 1.388 | 7 |
| 3 | 2026-04-27T09:28:26Z | 20 | 2 | 4 | 14 | 2 | 1.388 | 7 |
| 4 | 2026-04-27T09:28:31Z | 20 | 2 | 4 | 14 | 2 | 1.388 | 7 |
| 5 | 2026-04-27T09:28:36Z | 21 | 4 | 4 | 14 | 2 | 1.557 | 8 |
| 6 | 2026-04-27T09:28:45Z | 21 | 4 | 4 | 14 | 2 | 1.557 | 8 |
| 7 | 2026-04-27T09:28:50Z | 21 | 4 | 4 | 14 | 2 | 1.557 | 8 |
| 8 | 2026-04-27T09:28:55Z | 21 | 4 | 4 | 14 | 2 | 1.557 | 8 |

## Interpretation

- The focus block shows repeated external occupancy strong enough that the current 5 GHz operating point should be treated as an active interference surface, not a clean baseline.
- The lowest repeated-scan alternatives were `13, 1, 3`; use them only if the experiment design permits a channel move.
- Methodological warnings inherited from the aggregate report:
  - Signal levels were estimated from `nmcli` quality percentages, so absolute dBm values should be treated as approximate.
  - Channel-survey airtime utilization was not available because `nmcli` does not expose `iw survey dump` counters.
  - One or more SSID/BSSID filters were applied before interference scoring.
