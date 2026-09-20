# Claude Upload Packages (`.skill`)

This folder contains packaged `.skill` distribution files ready for upload or extraction into Claude (Claude.ai Projects, Claude Code, or custom AI coding environments).

---

## Files in this Directory

| File | Skill Identifier | Size | Purpose |
|---|---|---|---|
| [`project-scaffold.skill`](./project-scaffold.skill) | `project-scaffold` | ~40 KB | Enterprise project scaffolding, Vibe Coding beginner-to-production guide, 200% Production Architecture & Azure pricing evaluation, Next.js, FastAPI, and React + Vite architecture generators |
| [`motion-scroll.skill`](./motion-scroll.skill) | `motion-scroll-site` | ~23 KB | Turn template prompts + still images into Google Flow camera moves & Antigravity scroll-scrubbed websites |
| [`playwright-mcp.skill`](./playwright-mcp.skill) | `playwright-mcp` | ~7 KB | Microsoft official Playwright MCP server setup, automated browser testing, multi-viewport verification, and diagnostics |

---

## How to Upload and Use in Claude

### Option A: Upload Directly to Claude.ai Projects
1. Open [Claude.ai](https://claude.ai) and go to your **Project** (or create a new Project).
2. Click **Project Knowledge** $\rightarrow$ **Add Content** / **Upload files**.
3. Upload either:
   - The `.skill` file directly (if your interface supports zip/skill file parsing), **OR**
   - Rename `.skill` to `.zip`, extract the folder, and upload the `SKILL.md` and `references/` markdown files directly into Project Knowledge.
4. In the Project Instructions, paste:
   ```text
   You are equipped with the skills uploaded in Project Knowledge:
   - For project creation and architecture evaluation: refer to project-scaffold/SKILL.md.
   - For scroll-driven video and animation design: refer to motion-scroll-site/SKILL.md.
   - For browser automation and end-to-end testing: refer to playwright-mcp/SKILL.md.
   ```

---

### Option B: Use with Claude Code (Terminal Agent)
If you are using Claude Code in your command line:
1. Extract or place the skill into your project's `.agents/skills/` or `.claude/skills/` directory:
   ```powershell
   # Unzip the skill bundle:
   tar -xf project-scaffold.skill
   tar -xf playwright-mcp.skill
   ```
2. Claude Code will read the `SKILL.md` runbook and references when planning and executing tasks in your codebase.

---

### Option C: Manual Unzip / Inspection
Each `.skill` file is a standard zip archive containing:
- `SKILL.md` (Main instructions & YAML metadata)
- `references/` (Architecture guides and workflows)
- `templates/` (Markdown templates)
- `scripts/` (Automated generation scripts)

To extract manually in PowerShell:
```powershell
Expand-Archive -Path "playwright-mcp.skill" -DestinationPath "playwright-mcp"
```
