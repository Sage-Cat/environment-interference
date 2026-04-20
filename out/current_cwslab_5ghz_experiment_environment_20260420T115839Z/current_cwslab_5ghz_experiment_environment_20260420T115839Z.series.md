# Repeated 5 GHz Environment Series Report

## Objective

This companion report summarizes repeated ambient Wi-Fi scans for the current 5 GHz cws-lab operating point. It is intended to support experiment-facing channel interpretation rather than a one-shot convenience snapshot.

## Measurement Design

- Generated at (UTC): `2026-04-20T11:59:22Z`
- Interface: `wlp3s0`
- Backend: `nmcli`
- Location: `Current cws-lab room`
- Focus: `5 GHz` channel `36` / `20 MHz`
- Repeat count: `8`
- Inter-scan interval: `5.0 s`
- Strong-neighbor threshold: `-67.0 dBm`
- Aggregate report: `/home/sagecat/Projects/research-workspace/environment-interference/out/current_cwslab_5ghz_experiment_environment_20260420T115839Z/current_cwslab_5ghz_experiment_environment_20260420T115839Z.md`
- Notes: Repeated ambient 5 GHz environment scan for ongoing cws-lab experiments on channel 36 at 20 MHz; experiment AP excluded from interference scoring so the report reflects surrounding radio only.
- Exclusions before scoring: SSIDs `cwslab-exp1-main-5g`, BSSIDs `1e:f4:3f:f0:3d:a7`

## Experiment-Facing Summary

- Unique 5 GHz BSS observed across series: `2`
- Unique focus-block (36-48) BSS observed across series: `2`
- Focus exact-channel presence ratio: `0.0%`
- Focus exact strong-emitter presence ratio: `0.0%`
- Focus overlap presence ratio: `100.0%`
- Focus overlap strong-emitter presence ratio: `100.0%`
- Mean / median / worst focus congestion score: `0.825` / `0.825` / `0.825`
- Median focus rank in band: `22.0`
- Best repeated-scan alternatives: `52, 56, 60`

## Focus-Block Channel Stability

| Channel | Exact Presence | Exact Strong | Overlap Presence | Overlap Strong | Mean Exact APs | Mean Overlap APs | Mean Congestion | Max Congestion | Strongest Overlap |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 36 | 0.0% | 0.0% | 100.0% | 100.0% | 0.00 | 2.00 | 0.825 | 0.825 | -63.0 dBm |
| 40 | 100.0% | 100.0% | 100.0% | 100.0% | 2.00 | 2.00 | 1.500 | 1.500 | -63.0 dBm |
| 44 | 0.0% | 0.0% | 100.0% | 100.0% | 0.00 | 2.00 | 0.450 | 0.450 | -63.0 dBm |
| 48 | 0.0% | 0.0% | 100.0% | 100.0% | 0.00 | 2.00 | 0.450 | 0.450 | -63.0 dBm |
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
| EOM | `5c:62:8b:36:83:e0` | 40 | 8 | 100.0% | -63.0 dBm | -63.0 dBm |
| <hidden> | `5e:62:8b:56:83:e1` | 40 | 8 | 100.0% | -63.0 dBm | -63.0 dBm |

## Per-Sample Trace

| Sample | Captured At (UTC) | 2.4 GHz APs | 5 GHz APs | Focus Exact | Focus Overlap | Focus Strong Overlap | Focus Congestion | Focus Rank |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 2026-04-20T11:58:39Z | 20 | 2 | 0 | 2 | 2 | 0.825 | 22 |
| 2 | 2026-04-20T11:58:48Z | 20 | 2 | 0 | 2 | 2 | 0.825 | 22 |
| 3 | 2026-04-20T11:58:53Z | 20 | 2 | 0 | 2 | 2 | 0.825 | 22 |
| 4 | 2026-04-20T11:58:58Z | 20 | 2 | 0 | 2 | 2 | 0.825 | 22 |
| 5 | 2026-04-20T11:59:03Z | 20 | 2 | 0 | 2 | 2 | 0.825 | 22 |
| 6 | 2026-04-20T11:59:08Z | 20 | 2 | 0 | 2 | 2 | 0.825 | 22 |
| 7 | 2026-04-20T11:59:13Z | 21 | 2 | 0 | 2 | 2 | 0.825 | 22 |
| 8 | 2026-04-20T11:59:22Z | 21 | 2 | 0 | 2 | 2 | 0.825 | 22 |

## Interpretation

- The focus block shows repeated external occupancy strong enough that the current 5 GHz operating point should be treated as an active interference surface, not a clean baseline.
- The lowest repeated-scan alternatives were `52, 56, 60`; use them only if the experiment design permits a channel move.
- Methodological warnings inherited from the aggregate report:
  - Signal levels were estimated from `nmcli` quality percentages, so absolute dBm values should be treated as approximate.
  - Channel-survey airtime utilization was not available because `nmcli` does not expose `iw survey dump` counters.
  - One or more SSID/BSSID filters were applied before interference scoring.
