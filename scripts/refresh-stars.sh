#!/usr/bin/env bash
# Refresh GitHub stars in data/skills.json. Requires `gh` auth.
set -euo pipefail
exec python3 "$(cd "$(dirname "$0")" && pwd)/refresh-stars.py"
