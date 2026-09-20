# Playwright MCP Setup & Configuration Reference

This guide provides technical specifications for configuring Microsoft's official Playwright MCP server across Antigravity and Claude.

---

## 1. What is Playwright MCP?

Playwright MCP (`@playwright/mcp`) implements the **Model Context Protocol (MCP)** to expose browser automation capabilities directly to AI agents.

Key capabilities exposed to the model:
- `page_navigate`: Load arbitrary URLs or local dev servers (`http://localhost:3000`).
- `page_screenshot`: Capture visual state of rendered layouts across specific viewports.
- `page_click` / `page_fill`: Simulate user interactions (forms, navigation, toggles).
- `page_evaluate`: Run JavaScript in browser context to inspect layout metrics, bounding boxes, or computed styles.
- Console and network error capture.

---

## 2. Configuration Files & Locations

### Windows Global Path:
```
C:\Users\<YOUR_USERNAME>\.gemini\config\mcp_config.json
```

### Workspace Project Path:
```
<PROJECT_ROOT>\.agents\mcp_config.json
```

---

## 3. JSON Configuration Examples

### Minimal Standard Setup (Chromium default)
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

### Multiple MCP Servers (e.g. Preserving Context7)
```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["@upstash/context7-mcp@latest"]
    },
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
    }
  }
}
```

### Custom Browser Option (Chrome)
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest",
        "--browser=chrome"
      ]
    }
  }
}
```

---

## 4. Verification Checklist

- [ ] Node.js LTS installed (`node -v` $\ge$ 18.0.0)
- [ ] npm installed (`npm -v` $\ge$ 9.0.0)
- [ ] `mcp_config.json` contains valid JSON without trailing commas
- [ ] Antigravity / Claude MCP Manager displays `playwright` status as connected
- [ ] First smoke test passes on `https://demo.playwright.dev/todomvc`

