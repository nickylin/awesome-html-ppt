# Contributing

PRs welcome. This list stays **HTML-first** and **agent-usable**.

## Add a skill

Open an issue or PR with:

1. Public GitHub URL
2. License (MIT / Apache / AGPL / etc.)
3. One-line: what it outputs (single-file HTML, React framework, PPTX, …)
4. Why it is not a duplicate of an existing entry
5. A preview: prefer dropping a 16:9 still into `previews/<id>.png` (copied from the project's own README/demo). Hot-linking GitHub `user-attachments` often breaks on Pages.

## Rules

- Must contain a real `SKILL.md` (or a template directory / slide framework), not just a README.
- HTML should be the source of truth, **or** the project is a widely-used PPTX sibling that people searching “HTML PPT skill” will hit (mark `html_first: false` in `data/skills.json`).
- Write original descriptions. Do not paste another awesome-list's copy.
- Update `data/skills.json` in the same PR as the README.
- Star counts are refreshed with `./scripts/refresh-stars.sh`. Don't hand-edit stars unless the API is wrong.

## After merge

Maintainers may tweak wording for length and scanability. Previews stay hot-linked to the upstream repo so authors keep control.
