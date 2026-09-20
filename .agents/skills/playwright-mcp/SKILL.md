---
name: playwright-mcp
description: Complete global setup, browser automation, and verification guide for Microsoft's official Playwright MCP server (@playwright/mcp) in Google Antigravity and Claude. Use whenever the user wants to configure Playwright MCP globally or in a workspace, run automated browser tests, verify local development servers (http://localhost:3000, http://localhost:5173), test responsive UI across breakpoints (1440x900, 1920x1080, 1024x768, 768x1024, 390x844, 375x812), test scroll-driven/scrollytelling animations, inspect console errors, or troubleshoot MCP connection and browser launch issues.
---

# Playwright MCP + Google Antigravity

Complete global setup, browser automation, responsive testing, and troubleshooting guide for Microsoft's official **Playwright MCP** server (`@playwright/mcp`).

```
BUILD → RUN → TEST → FIX → REPEAT
```

Playwright MCP transforms the AI agent from a code reader into an active end-to-end tester by providing live browser control (navigating, clicking, filling forms, taking screenshots, evaluating viewport layout, and capturing console/network errors).

---

## Operating Modes

| Mode | Trigger | Output |
|---|---|---|
| **Mode 1: Setup & Health Check** | Configure or verify Playwright MCP server | Adds server to `mcp_config.json`, tests `npx @playwright/mcp@latest`, confirms server availability |
| **Mode 2: Local Project Testing** | App running on `localhost:3000` / `localhost:5173` | Checks page load, console errors, broken images, failed API calls, navigation, buttons |
| **Mode 3: Responsive Multi-Viewport Matrix** | User asks to test mobile/tablet/desktop layout | Tests at 1440×900, 1920×1080, 1024×768, 768×1024, 390×844, 375×812; captures screenshots; reports clipping/overflow |
| **Mode 4: Scroll-Driven / Scrollytelling Hero** | Testing scroll-scrubbed sites or video heroes | Slow-scroll test checking frame loading, animation progression, lag, and console warnings |
| **Mode 5: Diagnostics & Troubleshooting** | MCP server fails to connect or launch | Resolves JSON syntax errors, npx path issues, browser binary downloads, or localhost reachability |

---

## Mode 1: Setup & Configuration

### Global vs. Workspace Scope
- **Global Configuration** (Applies across all projects on your machine):  
  `C:\Users\<YOUR_USERNAME>\.gemini\config\mcp_config.json`
- **Workspace Configuration** (Project-specific):  
  `.agents/mcp_config.json`

### Official Configuration JSON
Add the Playwright MCP server under the `mcpServers` object in `mcp_config.json`:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
    }
  }
}
```

*Note: If you have existing servers (like `context7`), keep them intact and add `playwright` as an additional entry separated by a comma.*

### Browser Choice (Optional)
By default, Playwright uses its bundled Chromium. To specify Chrome:
```json
"playwright": {
  "command": "npx",
  "args": [
    "@playwright/mcp@latest",
    "--browser=chrome"
  ]
}
```
*(Recommendation: Do not add browser options until basic setup is verified working).*

### Reload & Verification
1. Save `mcp_config.json`.
2. In Antigravity: Go to Agent side panel $\rightarrow$ `...` $\rightarrow$ **MCP Servers** $\rightarrow$ **Refresh/Reload** (or run `/mcp` in CLI).
3. Confirm `playwright` shows as connected.

---

## Mode 2: Functional Browser Testing

### Initial Smoke Test (Harmless Public Demo)
Always run this verification before testing a real project:

```markdown
Use Playwright MCP.
Navigate to: https://demo.playwright.dev/todomvc
Verify that Playwright MCP can control the browser.
Add a todo called "Test Playwright MCP".
Mark it completed and take a screenshot.
Do not modify any files in my project.
```

### Testing a Running Local Project
When your local server is running (`npm run dev`):

```markdown
Open http://localhost:3000. Do not modify files.
Check page loading, console errors, failed network requests, broken images,
navigation, buttons, and responsive behavior.
Report issues and take screenshots of important failures.
```

---

## Mode 3: Responsive Multi-Viewport Matrix

Execute the 6-point responsive viewport inspection:

```markdown
Test http://localhost:3000 at the following resolutions:
- Desktop Large: 1920×1080
- Desktop Standard: 1440×900
- Tablet Landscape: 1024×768
- Tablet Portrait: 768×1024
- Mobile Standard: 390×844
- Mobile Compact: 375×812

Check:
1. Horizontal overflow or unintended scrolling
2. Text clipping or unreadable contrast over backgrounds
3. Navigation drawer / hamburger behavior
4. Button touch target accessibility
5. Spacing and typography collapse

Capture screenshots at each breakpoint. Do not modify code.
```

---

## Mode 4: Scroll-Driven & Scrollytelling Hero Testing

For sites with motion scroll, video heroes, or timeline animations:

```markdown
Open http://localhost:3000 and slowly scroll through the entire hero section.
Verify:
1. Frame sequence loads without 404s or visible stutter
2. Canvas/video updates smoothly in sync with scroll position
3. No console errors or memory warnings during rapid scroll
4. Transition and reveal animations trigger at correct scroll thresholds
5. Mobile touch-scroll behavior

Capture screenshots of the start, midpoint, and end of the hero timeline.
Do not modify code.
```

---

## Mode 5: Troubleshooting & Error Diagnostics

| Problem | Root Cause | Solution |
|---|---|---|
| **Playwright does not appear** | Entry missing or misnamed in `mcp_config.json` | Verify `playwright` is nested inside `"mcpServers"`. Save and restart Antigravity. |
| **JSON syntax error** | Trailing comma or missing bracket in `mcp_config.json` | Validate JSON with a linter. Ensure the last entry does not have a trailing comma. |
| **NPX / Package not found** | Node.js not installed or PATH missing | Run `node --version` and `npm --version`. Install Node.js LTS and restart Antigravity. |
| **Browser does not start** | First-time browser binary download in progress | Allow 30–60s on first run for Playwright to download Chromium. Check MCP log output. |
| **Localhost cannot be reached** | Dev server is not running or wrong port | Verify `npm run dev` is running in terminal and test URL manually in normal browser first. |

---

## Recommended Development Workflow

```
1. Build / Modify Feature
   ↓
2. Consult docs / context
   ↓
3. Run project locally (npm run dev)
   ↓
4. Test with Playwright MCP
   ↓
5. Capture screenshots & console errors
   ↓
6. Apply smallest surgical fix
   ↓
7. Re-test with Playwright MCP
   ↓
8. Commit & Deploy
```

---

## Reference Guides
- Detailed Setup & Config: [playwright-mcp-setup.md](./references/playwright-mcp-setup.md)
- Testing Workflows & Prompts: [browser-testing-workflows.md](./references/browser-testing-workflows.md)
- Troubleshooting Diagnostics: [mcp-troubleshooting.md](./references/mcp-troubleshooting.md)

