# Local Wi-Fi Environment Interference Report

- Generated at (UTC): `2026-03-13T15:54:26Z`
- Source: `offline analysis from saved iw text files`
- Location: `Fixture lab`
- Strong-neighbor threshold: `-67.0 dBm`
- Scan source: `tests/fixtures/sample_scan.txt`
- Survey source: `tests/fixtures/sample_survey.txt`

## Executive Summary

- **2.4 GHz**: `4` APs, `3` strong neighbors, recommended channels `11, 1, 6`.
- **5 GHz**: `3` APs, `2` strong neighbors, recommended channels `149, 44, 36`.

## 2.4 GHz

| Metric | Value |
| --- | --- |
| AP count | 4 |
| Unique SSID count | 4 |
| Strong-neighbor count | 3 |
| Median signal (dBm) | -56.50 |
| Mean survey busy ratio | 32.0% |
| Mean noise floor (dBm) | -95.00 |
| Recommended channels | 11, 1, 6 |

### Channel Occupancy

| Channel | APs | Unique SSIDs | Strong APs | Congestion score | Strongest signal | Survey busy | Noise |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 1 | 1.000 | -43.0 dBm | 34.0% | -95.0 dBm |
| 6 | 2 | 2 | 2 | 1.750 | -52.0 dBm | 54.0% | -94.0 dBm |
| 11 | 1 | 1 | 0 | 0.450 | -74.0 dBm | 8.0% | -96.0 dBm |

### Strongest Nearby APs

| SSID | BSSID | Channel | Signal | Last seen |
| --- | --- | --- | --- | --- |
| Lab_AP_24 | `aa:bb:cc:dd:ee:01` | 1 | -43.0 dBm | 12 ms |
| Nearby_24_A | `aa:bb:cc:dd:ee:02` | 6 | -52.0 dBm | 18 ms |
| Nearby_24_B | `aa:bb:cc:dd:ee:03` | 6 | -61.0 dBm | 19 ms |
| Far_24 | `aa:bb:cc:dd:ee:04` | 11 | -74.0 dBm | 31 ms |

### Interpretation

- Highest modeled congestion is on channel `6` (score `1.750`).
- Lowest modeled congestion is on channel `11` (score `0.450`).
- Recommended channels for experiments in this band: `11, 1, 6`.
- Mean channel busy ratio is `32.0%`, which helps separate true airtime pressure from simple AP count.

## 5 GHz

| Metric | Value |
| --- | --- |
| AP count | 3 |
| Unique SSID count | 3 |
| Strong-neighbor count | 2 |
| Median signal (dBm) | -67.00 |
| Mean survey busy ratio | 15.5% |
| Mean noise floor (dBm) | -98.67 |
| Recommended channels | 149, 44, 36 |

### Channel Occupancy

| Channel | APs | Unique SSIDs | Strong APs | Congestion score | Strongest signal | Survey busy | Noise |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 36 | 1 | 1 | 1 | 1.000 | -50.0 dBm | 26.0% | -97.0 dBm |
| 40 | 0 | 0 | 0 | 0.000 | n/a | n/a | n/a |
| 44 | 1 | 1 | 1 | 0.750 | -67.0 dBm | 17.0% | -98.0 dBm |
| 48 | 0 | 0 | 0 | 0.000 | n/a | n/a | n/a |
| 149 | 1 | 1 | 0 | 0.200 | -80.0 dBm | 3.5% | -101.0 dBm |
| 153 | 0 | 0 | 0 | 0.000 | n/a | n/a | n/a |
| 157 | 0 | 0 | 0 | 0.000 | n/a | n/a | n/a |
| 161 | 0 | 0 | 0 | 0.000 | n/a | n/a | n/a |

### Strongest Nearby APs

| SSID | BSSID | Channel | Signal | Last seen |
| --- | --- | --- | --- | --- |
| Lab_AP_5 | `aa:bb:cc:dd:ee:05` | 36 | -50.0 dBm | 7 ms |
| Nearby_5_A | `aa:bb:cc:dd:ee:06` | 44 | -67.0 dBm | 21 ms |
| Far_5 | `aa:bb:cc:dd:ee:07` | 149 | -80.0 dBm | 25 ms |

### Interpretation

- Highest modeled congestion is on channel `36` (score `1.000`).
- Lowest modeled congestion is on channel `149` (score `0.200`).
- Recommended channels for experiments in this band: `149, 44, 36`.
- Mean channel busy ratio is `15.5%`, which helps separate true airtime pressure from simple AP count.
