# Maintainer notes

- `data/skills.json` is the machine-readable source for the GitHub Pages catalog.
- After adding a repo, run `./scripts/refresh-stars.sh` (needs `gh` auth) and copy star counts into README tables if they drifted.
- Gallery thumbs live in `previews/` (vendored from upstream README / demo HTML). GitHub `user-attachments` hotlinks often fail on Pages, so prefer a local file. Keep `screenshot_kind: upstream-hotlink` only for files too large to vendor (Huashu GIF).
- Guizang is AGPL-3.0 — keep that visible in the pick table.
