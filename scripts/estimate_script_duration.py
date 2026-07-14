#!/usr/bin/env python3
"""Estimate spoken duration for Chinese or English narration scripts."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


HAN_RE = re.compile(r"[\u4e00-\u9fff]")
WORD_RE = re.compile(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)?")


def strip_markdown(text: str) -> str:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`]+`", " ", text)
    text = re.sub(r"^#+\s*", "", text, flags=re.M)
    text = re.sub(r"\[[^\]]+\]\([^)]+\)", " ", text)
    return text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("script")
    parser.add_argument("--language", default="zh-CN")
    parser.add_argument("--zh-cpm", type=int, default=260)
    parser.add_argument("--en-wpm", type=int, default=150)
    args = parser.parse_args()

    text = strip_markdown(Path(args.script).read_text(encoding="utf-8"))
    han_count = len(HAN_RE.findall(text))
    word_count = len(WORD_RE.findall(text))

    if args.language.lower().startswith("zh"):
        minutes = max(han_count / args.zh_cpm, word_count / args.en_wpm * 0.6)
        basis = f"{han_count} Han chars"
    else:
        minutes = word_count / args.en_wpm
        basis = f"{word_count} words"

    print(f"estimate_seconds={round(minutes * 60, 1)}")
    print(f"basis={basis}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
