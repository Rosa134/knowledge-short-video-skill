#!/usr/bin/env python3
"""Run practical media QA for rendered short videos."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Inspect rendered video with ffprobe, volumedetect, and optional contact sheet.")
    parser.add_argument("video")
    parser.add_argument("--report", help="write JSON report path")
    parser.add_argument("--contact-sheet", help="write contact sheet image path")
    parser.add_argument("--interval", type=float, default=3.0, help="seconds between contact sheet frames")
    parser.add_argument("--tile", default="4x4")
    return parser.parse_args()


def require(binary: str) -> str:
    found = shutil.which(binary)
    if not found:
        raise SystemExit(f"missing required binary: {binary}")
    return found


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")


def ffprobe(video: Path) -> dict[str, Any]:
    require("ffprobe")
    proc = run([
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration,size,bit_rate",
        "-show_entries", "stream=index,codec_type,codec_name,width,height,avg_frame_rate,sample_rate,channels",
        "-of", "json",
        str(video),
    ])
    if proc.returncode != 0:
        raise SystemExit(proc.stderr.strip() or "ffprobe failed")
    return json.loads(proc.stdout or "{}")


def volume(video: Path) -> dict[str, Any]:
    require("ffmpeg")
    proc = run(["ffmpeg", "-hide_banner", "-i", str(video), "-af", "volumedetect", "-f", "null", "-"])
    text = proc.stderr or ""
    result: dict[str, Any] = {"returncode": proc.returncode}
    for key in ("mean_volume", "max_volume"):
        m = re.search(rf"{key}:\s*([-0-9.]+)\s*dB", text)
        if m:
            result[key] = float(m.group(1))
    if proc.returncode != 0:
        result["error_tail"] = "\n".join(text.splitlines()[-12:])
    return result


def contact_sheet(video: Path, out: Path, interval: float, tile: str) -> None:
    require("ffmpeg")
    out.parent.mkdir(parents=True, exist_ok=True)
    fps = f"fps=1/{interval:g}"
    proc = run([
        "ffmpeg", "-y", "-hide_banner", "-i", str(video),
        "-vf", f"{fps},scale=216:-1,tile={tile}",
        "-frames:v", "1", "-update", "1", str(out),
    ])
    if proc.returncode != 0:
        raise SystemExit(proc.stderr.strip() or "contact sheet failed")


def main() -> int:
    args = parse_args()
    video = Path(args.video).resolve()
    if not video.exists():
        raise SystemExit(f"video not found: {video}")

    report = {
        "video": str(video),
        "ffprobe": ffprobe(video),
        "volume": volume(video),
    }
    if args.contact_sheet:
        out = Path(args.contact_sheet).resolve()
        contact_sheet(video, out, args.interval, args.tile)
        report["contact_sheet"] = str(out)

    report_path = Path(args.report).resolve() if args.report else video.with_suffix(".qa.json")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
