# Contributing

本仓库**持续收录**全网公开的 HTML 幻灯片 / PPT Agent Skills、模板库和相关框架，也**支持投稿**。别人的仓库、你自己写的都可以。

This list is collected ongoing. Submit other people's repos or your own.

## 怎么投稿

任选一种：

1. **Issue（推荐）** — 用投稿模板：[Submit a skill](https://github.com/nickylin/awesome-html-ppt/issues/new?template=submit-skill.yml)
2. **Pull Request** — 同一 PR 里改 [README.md](README.md) 和 [`data/skills.json`](data/skills.json)；有静帧的话放到 `previews/<id>.png`

请写清：

1. 公开 GitHub URL
2. 许可证（MIT / Apache / AGPL / 等）
3. 产出是什么（单文件 HTML、React 框架、PPTX、模板库…）
4. 和现有条目的差异（解决什么上台问题）
5. 预览：优先从该项目自己的 README / demo 截一张 16:9 放到 `previews/<id>.png`。GitHub `user-attachments` 热链在 Pages 上经常挂。

## 收录标准

- 必须有真实的 `SKILL.md`（或模板目录 / 幻灯片框架），不能只有广告 README。
- **HTML 优先**；若是被搜「HTML PPT skill」时总会撞上的 PPTX 兄弟项目，可进 Related，并在 json 里标 `html_first: false`。
- 条目描述自己写，不要整段复制别的 awesome list。
- 星标用 `./scripts/refresh-stars.sh` 刷新，不要手改（API 错了除外）。
- 不要求高星。教学、企业模板、可编辑、HTML→PPTX 等独特场景同样收录。

## After merge

Maintainers may shorten copy for scanability. Preview images stay attributed to the upstream project.
