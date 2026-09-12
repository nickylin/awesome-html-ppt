# Awesome HTML PPT

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Stars refreshed](https://img.shields.io/badge/stars-2026--09--12-111111.svg)](data/skills.json)

精选 **HTML 幻灯片 Agent Skills**。给 Cursor / Claude Code / Codex 用：装一个 skill，让模型按设计系统出片，而不是从空白 HTML 瞎编。

**[Browse the gallery →](https://nickylin.github.io/awesome-html-ppt/)** · English names kept as-is · 星标来自 GitHub API（2026-09-12）

> 不要只看星标。2.4 万的「杂志风」和 8 千的「演讲者模式」解决的是不同的上台问题。

## 30 秒怎么选

| 你要… | 装这个 | Stars |
| --- | --- | ---: |
| 线下分享、杂志感 / 瑞士网格 | [guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) **AGPL-3.0** | 26,169 |
| 先看 3 套预览再定稿 | [frontend-slides](https://github.com/zarazhangrui/frontend-slides) | 29,179 |
| 主题库 + 真演讲者窗（讲稿/计时） | [html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) | 8,333 |
| 同一套片反复改，像写代码 | [open-slide](https://github.com/1weiho/open-slide) | 7,564 |
| 同时交 HTML **和** 可编辑 PPTX | [huashu-design](https://github.com/alchaincyf/huashu-design) | 24,086 |
| diff / 架构复盘 / 数据表 | [visual-explainer](https://github.com/nicobailon/visual-explainer) | 9,798 |

## 什么是 HTML PPT Skill

一份可被 agent 加载的包装：通常是 `SKILL.md` + 主题 / 版式 + 一小段 runtime。模型按它的设计系统写出 **浏览器能直接翻页** 的幻灯片。

和传统 PPT 生成器的差别：

- **源格式是 HTML**（可版本管理、可投影、可嵌图嵌代码）
- 多数是 **单文件、零构建**；[open-slide](https://github.com/1weiho/open-slide) 是例外（React 框架）
- PPTX 只是导出，不是工作区

## Tier S · 先看这 7 个

星标断层很明显：前三都在 2.4 万以上。

### 1. [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) · 29,179★ · MIT

生态起点。不让你用形容词描述审美，而是 **生成 3 套视觉预览** 再让你挑。可从 PPTX 转入，Playwright 出 PDF。

模板库 sibling：[beautiful-html-templates](https://github.com/zarazhangrui/beautiful-html-templates)（34 套 × 封面/中段/后段）。

![Frontend Slides](https://github.com/user-attachments/assets/ef57333e-f879-432a-afb9-180388982478)

### 2. [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) · 26,169★ · AGPL-3.0

视觉气质最稳。两套旗舰：

- **Style A 电子杂志 × 电子墨水** — 叙事、观点、个人分享
- **Style B 瑞士国际主义** — 网格、单一高饱和锚点色、产品/方法论

带配图/封面、排练和演讲者模式。不适合密表、培训手册。

**License:** AGPL-3.0。二次分发派生作品前先读许可证。

```bash
npx skills add https://github.com/op7418/guizang-ppt-skill --skill guizang-ppt-skill
```

![Guizang Swiss](https://github.com/user-attachments/assets/8960e78c-69bb-4b7e-aa95-6fad64b70314)

![Guizang Magazine](https://github.com/user-attachments/assets/5dc316a2-401c-4e37-9123-ea081b6ae470)

### 3. [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) · 24,086★ · MIT

不只是 PPT skill：同一套设计哲学出 **HTML 演示 + 可编辑 PPTX**（文本框保留），还能做原型、Infographic、MP4。有品牌协议和 5 维评审。范围比纯幻灯片 skill 大。

```bash
npx skills add alchaincyf/huashu-design
```

### 4. [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) · 9,798★ · MIT

技术内容向：diff review、计划审计、数据表、项目复盘。四套暗色优先美学（Midnight Editorial / Terminal Mono / Warm Signal / Swiss Clean）。

不是 pitch deck 首选。

![Visual Explainer](https://github.com/user-attachments/assets/55ebc81b-8732-40f6-a4b1-7c3781aa96ec)

### 5. [lewislulu/html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) · 8,333★ · MIT

功能清单最满：36 主题、15 整套模板、31 版式、47 动画（27 CSS + 20 Canvas FX）。`S` 键弹出演讲者窗：当前页 / 下一页 / 逐字稿 / 计时器。纯静态 HTML，无构建。

```bash
npx skills add https://github.com/lewislulu/html-ppt-skill
```

![html-ppt themes](https://raw.githubusercontent.com/lewislulu/html-ppt-skill/main/docs/readme/hero.gif)

### 6. [1weiho/open-slide](https://github.com/1weiho/open-slide) · 7,564★ · MIT · [open-slide.dev](https://open-slide.dev)

架构不同：**React 框架**，不是纯 `SKILL.md`。每页任意 React 组件，固定 1920×1080。点选元素写批注 → `/apply-comments`。带演讲者模式、静态 HTML/PDF 导出。

适合长期维护同一套片。不适合「一句话出单文件就走」。

```bash
npx @open-slide/cli init my-slide
```

![open-slide](https://github.com/user-attachments/assets/02f5e6d7-12a7-4a8e-88e7-ae8770a96584)

### 7. [zarazhangrui/beautiful-html-templates](https://github.com/zarazhangrui/beautiful-html-templates) · 4,545★ · MIT

纯模板库，无生成逻辑。32+ 套，每套 3 页示范不同版式职责。很多 skill 会拿它当视觉真值。

![Soft Editorial](https://raw.githubusercontent.com/zarazhangrui/beautiful-html-templates/main/screenshots/soft-editorial-4.png)

## 功能对照

| Skill | 输出 | 视觉资产 | 演讲者 | PPTX | 最适合 |
| --- | --- | --- | --- | --- | --- |
| guizang-ppt-skill | 单文件 HTML | 2 套旗舰 + 配图 | 排练 + 演讲者 | 否 | 线下分享 |
| frontend-slides | 单文件 HTML | 16 风格组 + 34 模板 | 键鼠翻页 | 可转 | 从零做片 |
| huashu-design | HTML + PPTX | 20 设计哲学 | 浏览器演示 | 是 | 双交付 |
| html-ppt-skill | 静态 HTML | 36 主题 / 31 版式 / 47 动画 | S 键真演讲者窗 | 否 | 上台带讲稿 |
| open-slide | React 画布 | 任意 React 页 | 当前/下一页 + notes | HTML/PDF | 反复改稿 |
| visual-explainer | HTML 页或 deck | 4 套暗色优先 | 键鼠翻页 | 否 | 技术复盘 |
| beautiful-html-templates | 模板（非 skill） | 32–34 套 | — | 否 | 视觉参考 |
| frontend-slides-editable | 可拖拽 HTML | 继承 frontend-slides | 键鼠翻页 | PPTX→Web | 生成后再改 |

完整机器可读表：[data/skills.json](data/skills.json)

## Tier A · 生产可用

| Repo | ★ | 一句话 |
| --- | ---: | --- |
| [mucsbr/ppt-agent-workflow-san](https://github.com/mucsbr/ppt-agent-workflow-san) | 638 | 渐进交互：计划 → HTML → PPTX，导出是一等公民 |
| [archlizheng/frontend-slides-editable](https://github.com/archlizheng/frontend-slides-editable) | 497 | frontend-slides 的可编辑 fork |
| [vigorX777/ppt-svg-generator](https://github.com/vigorX777/ppt-svg-generator) | 258 | Markdown → HTML/PDF，五套风格 |
| [Akxan/ppt-agent-skill](https://github.com/Akxan/ppt-agent-skill) | 147 | 26 风格 · 18 图表，对标真实品牌 CSS |
| [bytonylee/future-slide-skill](https://github.com/bytonylee/future-slide-skill) | 147 | 同一 IR 切 HTML 现场片或图片轮播 |

## Tier B · 专项

星少不代表弱。这些往往是 **某个场景的最佳解**。

| Repo | ★ | 场景 |
| --- | ---: | --- |
| [software-ai-life/Awesome-PPT-Design-Skills](https://github.com/software-ai-life/Awesome-PPT-Design-Skills) | 103 | 多风格包，繁中一等公民 |
| [edu-ai-builders/visual-cognition-slides](https://github.com/edu-ai-builders/visual-cognition-slides) | 83 | 教学留存，不是商业 pitch |
| [zuiho-kai/huawei-style-ppt-skill](https://github.com/zuiho-kai/huawei-style-ppt-skill) | 63 | 华为风高密度战略页 |
| [WayneZhon/KingDee-PPT-Skill](https://github.com/WayneZhon/KingDee-PPT-Skill) | 56 | 金蝶官方模板语言 |
| [codesstar/next-slide](https://github.com/codesstar/next-slide) | 50 | 26+ 设计系统，中英双语 |
| [kaisersong/slide-creator](https://github.com/kaisersong/slide-creator) | 49 | IR 先行 + 16 项内容审查 |
| [FeeiCN/slide-writer](https://github.com/FeeiCN/slide-writer) | 41 | 企业风，自动套国内大厂主题 |
| [Phlegonlabs/Powerpoint-fancy-design](https://github.com/Phlegonlabs/Powerpoint-fancy-design) | 33 | HTML + PNG + PPTX，中英字体 |
| [nghiahsgs/skills-slides](https://github.com/nghiahsgs/skills-slides) | 32 | token 系统 + anti-slop 清单 |
| [xhshow2025/-PPT-sense-deck-skill-](https://github.com/xhshow2025/-PPT-sense-deck-skill-) | 23 | 演讲者 + 可编辑 + 手势 |

## Cursor 安装

Skills 放进项目 `.cursor/skills/<name>/SKILL.md`，或用户目录 `~/.cursor/skills/`。Cursor 也会读 `~/.claude/skills/`。

```bash
# 例子：html-ppt-skill
npx skills add https://github.com/lewislulu/html-ppt-skill

# 或手动
git clone https://github.com/op7418/guizang-ppt-skill.git ~/.cursor/skills/guizang-ppt-skill
```

对话里用 `/skill-name`，或直接说「做一份 HTML PPT」—— agent 会按 description 匹配。

刷新本仓库星标：

```bash
python3 scripts/refresh-stars.py
```

## Related（不是 HTML 优先）

| Repo | ★ | 为什么在这 |
| --- | ---: | --- |
| [likaku/Mck-ppt-design-skill](https://github.com/likaku/Mck-ppt-design-skill) | 274 | 麦肯锡风 python-pptx，源格式不是 HTML |
| [ToseaAI/awesome-html-slide-skills](https://github.com/ToseaAI/awesome-html-slide-skills) | 146 | 更早的公开目录。本列表按使用场景重排 |

## Contributing

见 [CONTRIBUTING.md](CONTRIBUTING.md)。条目必须是公开、HTML 优先、有真实 skill 文件。

## License

本合集的编排与文案是 [CC BY 4.0](LICENSE)。被链仓库保留各自许可证。截图热链到上游 README，版权仍归原作者，仅用于辨认项目。

Screenshots remain copyright of their authors and are shown as identification thumbnails.
