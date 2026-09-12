#!/usr/bin/env python3
"""Refresh GitHub star counts in data/skills.json. Requires `gh` auth."""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "skills.json"


def stars_for(repo: str) -> int:
    owner, name = repo.split("/", 1)
    raw = subprocess.check_output(
        ["gh", "api", f"repos/{owner}/{name}", "--jq", ".stargazerCount"],
        text=True,
    )
    return int(raw.strip())


def main() -> int:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    failed: list[str] = []
    for group in ("skills", "related"):
        for item in payload.get(group, []):
            repo = item.get("repo")
            if not repo:
                continue
            try:
                item["stars"] = stars_for(repo)
                print(f"{repo:48} {item['stars']}")
            except subprocess.CalledProcessError as exc:
                failed.append(repo)
                print(f"{repo:48} FAIL {exc}", file=sys.stderr)
    payload["updated"] = date.today().isoformat()
    payload["source"] = "GitHub API"
    DATA.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\nwrote {DATA.relative_to(ROOT)}  updated={payload['updated']}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
