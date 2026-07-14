#!/usr/bin/env python3
"""Create a knowledge short-video project skeleton."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", required=True)
    parser.add_argument("--root", default="videos")
    parser.add_argument("--type", default="ai_intro", choices=["pm_method", "ai_intro", "product_intro"])
    parser.add_argument("--platform", default="xiaohongshu")
    parser.add_argument("--language", default="zh-CN")
    parser.add_argument("--duration", type=int, default=60)
    parser.add_argument("--audience", default="产品经理、AI 应用开发者和知识工作者")
    parser.add_argument("--topic", default="")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project = Path(args.root) / args.id
    project.mkdir(parents=True, exist_ok=True)

    for child in [".ksv", "assets", "audio", "remotion", "renders", "qa"]:
        (project / child).mkdir(exist_ok=True)

    brief_path = project / "brief.json"
    if not brief_path.exists():
        brief = {
            "id": args.id,
            "type": args.type,
            "platform": args.platform,
            "language": args.language,
            "duration_s": args.duration,
            "audience": args.audience,
            "source": {"type": "topic", "text": args.topic or args.id.replace("-", " ")},
            "style": {"tone": "清晰、专业、克制", "visual": "clean diagram explainer"},
            "created_at": datetime.now().isoformat(timespec="seconds"),
        }
        brief_path.write_text(json.dumps(brief, ensure_ascii=False, indent=2), encoding="utf-8")

    placeholders = {
        "facts.json": {"facts": [], "opinions": []},
        "storyboard.json": {"video": {"id": args.id}, "scenes": []},
        "tts-manifest.json": {"language": args.language, "backend": "edge", "scenes": []},
        "timing.json": {"scenes": []},
        "pipeline-manifest.json": {
            "stages": [
                "brief",
                "facts",
                "script",
                "tts",
                "timing",
                "storyboard",
                "asset_prompting",
                "assets",
                "visual_render",
                "audio_mix",
                "frame_qa",
                "publish_render",
            ]
        },
        ".ksv/checkpoint.json": {"version": 1, "stages": {}},
        "assets/manifest.json": {"assets": []},
    }
    for rel, data in placeholders.items():
        path = project / rel
        if not path.exists():
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    text_placeholders = {
        "script.md": "# Script\n\n",
        "report.md": "# Report\n\n",
        "assets/image2-prompts.md": "# Image2 Prompts\n\n",
    }
    for rel, text in text_placeholders.items():
        path = project / rel
        if not path.exists():
            path.write_text(text, encoding="utf-8")

    print(project.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
