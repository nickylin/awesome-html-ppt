# Awesome HTML PPT

[中文](README.md) · English

A living catalog of the **best HTML slide / PPT agent skills and related repos** we can find — for Cursor, Claude Code, and Codex. Most of them turn a prompt or outline into a zero-build, keyboard-navigable HTML deck.

This list is maintained over time: new public skills, template libraries, and slide frameworks get reviewed and added. **Submissions are welcome** (your own project or someone else's).

[**Submit a skill →**](https://github.com/nickylin/awesome-html-ppt/issues/new?template=submit-skill.yml)

Stars refreshed from the GitHub API on **2026-09-12**. Star rank is a discovery signal, not a quality ranking for your use case.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Skills](https://img.shields.io/badge/skills-22-111111)

**[Visual catalog](https://nickylin.github.io/awesome-html-ppt/)**

## Look first

<table>
  <tr>
    <td width="50%">
      <a href="https://github.com/zarazhangrui/frontend-slides"><img src="previews/frontend-slides.png" alt="Frontend Slides"></a>
      <p><strong><a href="https://github.com/zarazhangrui/frontend-slides">Frontend Slides</a></strong> · 29k★ — preview three looks, then generate.</p>
    </td>
    <td width="50%">
      <a href="https://github.com/op7418/guizang-ppt-skill"><img src="previews/guizang-ppt-skill.png" alt="Guizang PPT"></a>
      <p><strong><a href="https://github.com/op7418/guizang-ppt-skill">Guizang PPT</a></strong> · 26k★ — magazine × Swiss grid. AGPL-3.0.</p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <a href="https://github.com/lewislulu/html-ppt-skill"><img src="previews/html-ppt-skill.png" alt="HTML PPT Studio"></a>
      <p><strong><a href="https://github.com/lewislulu/html-ppt-skill">HTML PPT Studio</a></strong> · 8.3k★ — 36 themes, real presenter window.</p>
    </td>
    <td width="50%">
      <a href="https://github.com/1weiho/open-slide"><img src="previews/open-slide.png" alt="open-slide"></a>
      <p><strong><a href="https://github.com/1weiho/open-slide">open-slide</a></strong> · 7.6k★ — React canvas for decks you keep editing.</p>
    </td>
  </tr>
</table>

Full illustrated catalog (all 22 skills) is in the [Chinese README](README.md).

## Pick one

| Need | Skill | Stars |
|------|--------|------:|
| Magazine / Swiss-grid talks | [guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | 26.2k |
| Don't know the look — preview first | [frontend-slides](https://github.com/zarazhangrui/frontend-slides) | 29.2k |
| Biggest theme kit + real presenter window | [html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) | 8.3k |
| Iterate like code | [open-slide](https://github.com/1weiho/open-slide) | 7.6k |
| HTML **and** editable PPTX | [huashu-design](https://github.com/alchaincyf/huashu-design) | 24.1k |
| Diffs, plan audits, recaps | [visual-explainer](https://github.com/nicobailon/visual-explainer) | 9.8k |

Guizang is **AGPL-3.0**. Frontend Slides / html-ppt-skill / open-slide / Huashu are MIT.

## What belongs here

A skill is a `SKILL.md` plus themes/layouts (and sometimes a small runtime) that an agent can load to produce slides. Templates are static scaffolds. Frameworks (open-slide) render arbitrary React pages onto a fixed 1920×1080 canvas.

Full write-ups, screenshots, and the feature matrix live in the [Chinese README](README.md). Machine-readable data: [data/skills.json](data/skills.json).

```bash
./scripts/refresh-stars.sh
```

## Ongoing collection · submit

This is not a one-shot ranking. We keep scanning public HTML PPT skills / templates / frameworks and add entries that are agent-usable and HTML-first.

- Fastest: [open a submission issue](https://github.com/nickylin/awesome-html-ppt/issues/new?template=submit-skill.yml)
- Or send a PR that updates both [README.md](README.md) and [`data/skills.json`](data/skills.json)
- Rules: [CONTRIBUTING.md](CONTRIBUTING.md)

High stars are optional. Niche jobs (teaching, enterprise templates, in-browser edit, HTML→PPTX) count.

## Related

- [ToseaAI/awesome-html-slide-skills](https://github.com/ToseaAI/awesome-html-slide-skills) — independent English gallery; this repo writes its own entries.

## License

Curated text is [CC BY 4.0](LICENSE). Linked projects keep their own licenses.
