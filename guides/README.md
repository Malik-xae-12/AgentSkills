# Skills Hub Documentation & Usage Guides

Welcome to the **Skills Hub**. This directory provides user guides, execution flows, and output breakdowns for all skills available in this repository.

---

## Skills Directory

| Skill | Description | Guide | Package (`.skill`) |
|---|---|---|---|
| **`project-scaffold`** | Production project scaffolding, Vibe Coding methodology (PRD, Architecture, Design, Rules, Tasks, Decisions, Memory, Test Plan, Security), 200% Production Architecture & Azure pricing evaluation, and exact folder trees for Next.js, FastAPI, and React + Vite. | [Read Guide](./project-scaffold-guide.md) | [`../claude-upload/project-scaffold.skill`](../claude-upload/project-scaffold.skill) |
| **`motion-scroll-site`** | Turn a template prompt + still image into Google Flow (Gemini Omni) camera moves, scroll-scrubbed web animations, and senior UI design critique. | [Read Guide](./motion-scroll-site-guide.md) | [`../claude-upload/motion-scroll.skill`](../claude-upload/motion-scroll.skill) |
| **`playwright-mcp`** | Complete global setup, live browser automation, responsive multi-viewport testing (1920px to 375px), scrollytelling tests, and troubleshooting for Microsoft's official `@playwright/mcp` server. | [Read Guide](./playwright-mcp-guide.md) | [`../claude-upload/playwright-mcp.skill`](../claude-upload/playwright-mcp.skill) |

---

## What are Skills?
Skills are modular runbooks and toolsets for AI coding assistants (Google Antigravity, Claude Code, etc.).
- When placed in `.agents/skills/<skill-name>/`, the AI assistant reads the `SKILL.md` frontmatter and automatically triggers the correct behavior when you mention relevant keywords.
- Each skill includes step-by-step procedures, checklists, reference documents, and optional automation scripts.

---

## Quick Navigation
- **[How to Use `project-scaffold`: What Happens & What is the Output](./project-scaffold-guide.md)**
- **[How to Use `motion-scroll-site`: What Happens & What is the Output](./motion-scroll-site-guide.md)**
- **[How to Use `playwright-mcp`: Browser Automation & Testing Guide](./playwright-mcp-guide.md)**
- **[Upload to Claude / Download `.skill` Bundles](../claude-upload/README.md)**
