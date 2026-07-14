#!/usr/bin/env python3
"""Hash video pipeline stage inputs and maintain resumable checkpoints."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Knowledge short-video stage checkpoint helper.")
    sub = parser.add_subparsers(dest="command", required=True)

    for name in ("status", "mark"):
        cmd = sub.add_parser(name)
        cmd.add_argument("project", help="video project directory")
        cmd.add_argument("--stage", required=True)
        cmd.add_argument("--inputs", nargs="+", required=True, help="input files or directories relative to project")
        cmd.add_argument("--extra", nargs="*", default=[], help="extra strings to include in the hash")
        if name == "mark":
            cmd.add_argument("--artifacts", nargs="*", default=[], help="artifact paths relative to project")

    return parser.parse_args()


def file_digest(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"path": str(path), "missing": True}
    if path.is_dir():
        entries = []
        for child in sorted(p for p in path.rglob("*") if p.is_file()):
            entries.append(file_digest(child))
        return {"path": str(path), "type": "dir", "entries": entries}
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return {"path": str(path), "type": "file", "size": path.stat().st_size, "sha256": h.hexdigest()}


def stage_hash(project: Path, inputs: list[str], extra: list[str]) -> str:
    payload = {
        "inputs": [file_digest(project / rel) for rel in inputs],
        "extra": extra,
    }
    blob = json.dumps(payload, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:16]


def checkpoint_path(project: Path) -> Path:
    return project / ".ksv" / "checkpoint.json"


def load_checkpoint(project: Path) -> dict[str, Any]:
    path = checkpoint_path(project)
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return {"version": 1, "stages": {}}


def save_checkpoint(project: Path, data: dict[str, Any]) -> None:
    path = checkpoint_path(project)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    args = parse_args()
    project = Path(args.project).resolve()
    if not project.exists():
        raise SystemExit(f"project not found: {project}")

    digest = stage_hash(project, args.inputs, args.extra)
    data = load_checkpoint(project)
    entry = data.get("stages", {}).get(args.stage)
    current = {
        "stage": args.stage,
        "input_hash": digest,
        "status": "cached" if entry and entry.get("input_hash") == digest and entry.get("status") == "done" else "stale",
        "checkpoint": str(checkpoint_path(project)),
    }

    if args.command == "status":
        if entry:
            current["previous"] = entry
        print(json.dumps(current, ensure_ascii=False, indent=2))
        return 0

    artifacts = [str((project / rel).resolve()) for rel in args.artifacts]
    missing = [p for p in artifacts if not Path(p).exists()]
    data.setdefault("stages", {})[args.stage] = {
        "status": "done" if not missing else "incomplete",
        "input_hash": digest,
        "inputs": args.inputs,
        "extra": args.extra,
        "artifacts": artifacts,
        "missing_artifacts": missing,
        "updated_at": datetime.now().isoformat(timespec="seconds"),
    }
    save_checkpoint(project, data)
    current["status"] = data["stages"][args.stage]["status"]
    current["artifacts"] = artifacts
    current["missing_artifacts"] = missing
    print(json.dumps(current, ensure_ascii=False, indent=2))
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
