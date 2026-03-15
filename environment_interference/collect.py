from __future__ import annotations

import subprocess


class CollectionError(RuntimeError):
    pass


def _run_text_command(command: list[str]) -> str:
    proc = subprocess.run(
        command,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if proc.returncode != 0:
        stderr = proc.stderr.strip() or "unknown error"
        raise CollectionError(f"{' '.join(command)} failed: {stderr}")
    return proc.stdout


def collect_scan_text(interface: str) -> str:
    return _run_text_command(["iw", "dev", interface, "scan"])


def collect_survey_text(interface: str) -> str | None:
    try:
        text = _run_text_command(["iw", "dev", interface, "survey", "dump"])
    except CollectionError:
        return None
    return text or None

