# Environment Interference

Standalone Wi-Fi environment survey toolkit for checking local 2.4 GHz and 5 GHz interference conditions before Wi-Fi sensing experiments.

The project collects nearby BSS information from `iw`, optionally reads channel survey data, computes practical congestion metrics, and generates:

- a Markdown report
- a PDF report

The goal is to quickly understand whether an experiment location is suitable for Wi-Fi sensing and which channels are the least congested.

## What the report includes

- separate 2.4 GHz and 5 GHz sections
- access-point counts and strong-neighbor counts
- per-channel occupancy and congestion score
- optional survey busy-ratio and noise-floor metrics
- strongest neighboring APs
- recommended lower-congestion channels for experiments

## Requirements

- Linux with `iw`
- `pandoc`
- `xelatex`
- Python 3.10+

## Quick start

### 1. Analyze the live environment

```bash
python3 -m environment_interference.cli analyze \
  --interface wlan0 \
  --location-label "Lab 314" \
  --notes "Baseline room survey before CSI runs" \
  --output-dir out/lab_314
```

This writes:

- `*.scan.txt`
- `*.survey.txt` when available
- `*.md`
- `*.pdf`

### 2. Analyze saved raw scan files

```bash
python3 -m environment_interference.cli analyze \
  --scan-file tests/fixtures/sample_scan.txt \
  --survey-file tests/fixtures/sample_survey.txt \
  --location-label "Fixture demo" \
  --output-dir out/fixture_demo \
  --report-name fixture_demo
```

### 3. Raw collection only

```bash
python3 -m environment_interference.cli collect \
  --interface wlan0 \
  --output-dir out/raw \
  --prefix lab_314_precheck
```

## Operator wrapper

```bash
./scripts/run_environment_report.sh analyze --interface wlan0 --location-label "Lab 314"
```

## Notes

- `iw dev <iface> scan` may require elevated privileges depending on the machine setup.
- `survey dump` support depends on the Wi-Fi driver/chipset. The report still works without survey data.
- The congestion score is a practical heuristic for experiment-site selection, not a regulatory spectrum measurement.

