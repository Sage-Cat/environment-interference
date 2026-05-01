# Repeated 5 GHz Environment Series Report

## Objective

This companion report summarizes repeated ambient Wi-Fi scans for the current 5 GHz cws-lab operating point. It is intended to support experiment-facing channel interpretation rather than a one-shot convenience snapshot.

## Measurement Design

- Generated at (UTC): `2026-05-01T10:10:55Z`
- Interface: `wlp3s0`
- Backend: `nmcli`
- Location: `cws-lab experiment area`
- Focus: `2.4 GHz` channel `6` / `20 MHz`
- Repeat count: `8`
- Inter-scan interval: `5.0 s`
- Strong-neighbor threshold: `-67.0 dBm`
- Aggregate report: `out/current_cwslab_d07_d09_24ghz_poweroff_external_environment_20260501T100910Z/current_cwslab_d07_d09_24ghz_poweroff_external_environment_20260501T100910Z.md`
- Notes: Ambient pre-experiment environment measurement for D07-D09 after the operator powered off all experiment devices. This canonical run followed forced nmcli rescans to clear stale lab SSID cache entries. Focus is the Node-C/T2 support surface: 2.4 GHz channel 6 / 20 MHz. Known cws-lab SSIDs are excluded from interference scoring to estimate external background.
- Exclusions before scoring: SSIDs `cwslab-exp1-main-5g, cws-lab-exp1-5g, cwslab-rpi5-exp-5g, cwslab-rpi5-node-c-24g, cwslab-rpi5-mgmt-24g, cwslab-rpi4-mgmt-24g`, BSSIDs `-`

## Experiment-Facing Summary

- Unique 5 GHz BSS observed across series: `4`
- Unique focus-block (n/a) BSS observed across series: `7`
- Focus exact-channel presence ratio: `100.0%`
- Focus exact strong-emitter presence ratio: `100.0%`
- Focus overlap presence ratio: `100.0%`
- Focus overlap strong-emitter presence ratio: `100.0%`
- Mean / median / worst focus congestion score: `3.458` / `3.442` / `3.507`
- Median focus rank in band: `10.0`
- Best repeated-scan alternatives: `11, 1, 2`

## Focus-Block Channel Stability

| Channel | Exact Presence | Exact Strong | Overlap Presence | Overlap Strong | Mean Exact APs | Mean Overlap APs | Mean Congestion | Max Congestion | Strongest Overlap |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 100.0% | 0.0% | 100.0% | 0.0% | 4.50 | 14.50 | 1.170 | 1.335 | -68.0 dBm |
| 2 | 100.0% | 0.0% | 100.0% | 100.0% | 4.00 | 20.75 | 1.414 | 1.590 | -59.0 dBm |
| 3 | 100.0% | 0.0% | 100.0% | 100.0% | 2.00 | 22.75 | 1.815 | 1.955 | -53.0 dBm |
| 4 | 100.0% | 0.0% | 100.0% | 100.0% | 2.00 | 23.75 | 2.369 | 2.470 | -53.0 dBm |
| 5 | 100.0% | 0.0% | 100.0% | 100.0% | 2.00 | 24.75 | 3.057 | 3.123 | -53.0 dBm |
| 6 | 100.0% | 100.0% | 100.0% | 100.0% | 6.25 | 20.25 | 3.458 | 3.507 | -53.0 dBm |
| 7 | 100.0% | 100.0% | 100.0% | 100.0% | 2.00 | 22.25 | 3.365 | 3.395 | -53.0 dBm |
| 8 | 100.0% | 0.0% | 100.0% | 100.0% | 1.00 | 20.25 | 2.572 | 2.593 | -53.0 dBm |
| 9 | 100.0% | 0.0% | 100.0% | 100.0% | 1.00 | 18.25 | 1.746 | 1.755 | -53.0 dBm |
| 11 | 100.0% | 0.0% | 100.0% | 100.0% | 6.00 | 10.00 | 0.598 | 0.598 | -53.0 dBm |

## Persistent 5 GHz Focus-Block Emitters

| SSID | BSSID | Channel | Observations | Presence | Strongest | Median |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| dlink-rustview | `00:24:01:bc:42:e5` | 6 | 8 | 100.0% | -59.0 dBm | -60.0 dBm |
| <hidden> | `c6:b2:5b:d6:2f:45` | 6 | 8 | 100.0% | -78.0 dBm | -78.0 dBm |
| Nest | `c6:b2:5b:86:2f:45` | 6 | 8 | 100.0% | -79.0 dBm | -79.0 dBm |
| TP-LINK_AD1C | `18:d6:c7:71:ad:1c` | 6 | 8 | 100.0% | -85.0 dBm | -85.0 dBm |
| iPhonTD | `62:85:84:5b:08:6d` | 6 | 8 | 100.0% | -88.0 dBm | -88.0 dBm |
| 👻 | `7e:dc:73:6d:1b:52` | 6 | 8 | 100.0% | -90.5 dBm | -90.5 dBm |
| iPhone | `92:2a:67:ca:a5:ca` | 6 | 2 | 25.0% | -88.0 dBm | -88.0 dBm |

## Per-Sample Trace

| Sample | Captured At (UTC) | 2.4 GHz APs | 5 GHz APs | Focus Exact | Focus Overlap | Focus Strong Overlap | Focus Congestion | Focus Rank |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 2026-05-01T10:10:16Z | 30 | 3 | 6 | 20 | 3 | 3.442 | 10 |
| 2 | 2026-05-01T10:10:21Z | 30 | 3 | 6 | 20 | 3 | 3.442 | 10 |
| 3 | 2026-05-01T10:10:26Z | 30 | 3 | 6 | 20 | 3 | 3.442 | 10 |
| 4 | 2026-05-01T10:10:31Z | 30 | 3 | 6 | 20 | 3 | 3.442 | 10 |
| 5 | 2026-05-01T10:10:36Z | 30 | 3 | 6 | 20 | 3 | 3.442 | 10 |
| 6 | 2026-05-01T10:10:41Z | 30 | 3 | 6 | 20 | 3 | 3.442 | 10 |
| 7 | 2026-05-01T10:10:46Z | 33 | 4 | 7 | 21 | 3 | 3.507 | 10 |
| 8 | 2026-05-01T10:10:55Z | 33 | 4 | 7 | 21 | 3 | 3.507 | 10 |

## Interpretation

- The focus block shows repeated external occupancy strong enough that the current 5 GHz operating point should be treated as an active interference surface, not a clean baseline.
- The lowest repeated-scan alternatives were `11, 1, 2`; use them only if the experiment design permits a channel move.
- Methodological warnings inherited from the aggregate report:
  - Signal levels were estimated from `nmcli` quality percentages, so absolute dBm values should be treated as approximate.
  - Channel-survey airtime utilization was not available because `nmcli` does not expose `iw survey dump` counters.
  - One or more SSID/BSSID filters were applied before interference scoring.
