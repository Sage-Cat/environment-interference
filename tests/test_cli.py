from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def test_cli_analyze_writes_markdown_from_fixture_inputs(tmp_path: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    scan_file = repo_root / "tests" / "fixtures" / "sample_scan.txt"
    survey_file = repo_root / "tests" / "fixtures" / "sample_survey.txt"

    proc = subprocess.run(
        [
            sys.executable,
            "-m",
            "environment_interference.cli",
            "analyze",
            "--scan-file",
            str(scan_file),
            "--survey-file",
            str(survey_file),
            "--location-label",
            "Fixture lab",
            "--output-dir",
            str(tmp_path),
            "--report-name",
            "fixture_report",
            "--skip-pdf",
        ],
        cwd=repo_root,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    assert proc.returncode == 0, proc.stderr
    markdown_path = tmp_path / "fixture_report.md"
    assert markdown_path.is_file()
    text = markdown_path.read_text(encoding="utf-8")
    assert "### 2.4 GHz" in text
    assert "### 5 GHz" in text
    assert "Experiment Focus" in text
    assert "Inferred interference level" in text
