#!/usr/bin/env python3
"""Validate the minimal brief contract for knowledge-short-video."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED = {
    "id": str,
    "type": str,
    "platform": str,
    "language": str,
    "duration_s": (int, float),
    "audience": str,
    "source": dict,
}

ALLOWED_TYPES = {"pm_method", "ai_intro", "product_intro"}
ALLOWED_SOURCE_TYPES = {"topic", "document", "url", "readme", "outline", "script"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("brief")
    args = parser.parse_args()

    data = json.loads(Path(args.brief).read_text(encoding="utf-8"))
    errors: list[str] = []

    for key, expected in REQUIRED.items():
        if key not in data:
            errors.append(f"missing required field: {key}")
        elif not isinstance(data[key], expected):
            errors.append(f"invalid type for {key}: expected {expected}")

    if data.get("type") not in ALLOWED_TYPES:
        errors.append(f"type must be one of {sorted(ALLOWED_TYPES)}")

    source = data.get("source") if isinstance(data.get("source"), dict) else {}
    if source.get("type") not in ALLOWED_SOURCE_TYPES:
        errors.append(f"source.type must be one of {sorted(ALLOWED_SOURCE_TYPES)}")
    if not source.get("text") and not source.get("path") and not source.get("url"):
        errors.append("source must include one of: text, path, url")

    duration = data.get("duration_s")
    if isinstance(duration, (int, float)) and duration <= 0:
        errors.append("duration_s must be positive")

    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1

    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
