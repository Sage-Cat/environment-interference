from __future__ import annotations

import shutil
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


def detect_live_backend(preferred: str = "auto") -> str:
    if preferred == "auto":
        if shutil.which("iw"):
            return "iw"
        if shutil.which("nmcli"):
            return "nmcli"
        raise CollectionError("no supported live scanner found; install `iw` or `nmcli`")
    if preferred == "iw":
        if not shutil.which("iw"):
            raise CollectionError("`iw` is not available on this host")
        return preferred
    if preferred == "nmcli":
        if not shutil.which("nmcli"):
            raise CollectionError("`nmcli` is not available on this host")
        return preferred
    raise CollectionError(f"unsupported backend: {preferred}")


def collect_scan_text(interface: str, *, backend: str = "auto") -> tuple[str, str]:
    resolved_backend = detect_live_backend(backend)
    if resolved_backend == "iw":
        return resolved_backend, _run_text_command(["iw", "dev", interface, "scan"])
    return resolved_backend, _run_text_command(
        [
            "nmcli",
            "-t",
            "--escape",
            "yes",
            "-f",
            "IN-USE,SSID,BSSID,CHAN,FREQ,RATE,SIGNAL,SECURITY",
            "dev",
            "wifi",
            "list",
            "ifname",
            interface,
            "--rescan",
            "auto",
        ]
    )


def collect_survey_text(interface: str, *, backend: str = "auto") -> str | None:
    resolved_backend = detect_live_backend(backend)
    if resolved_backend != "iw":
        return None
    try:
        text = _run_text_command(["iw", "dev", interface, "survey", "dump"])
    except CollectionError:
        return None
    return text or None
