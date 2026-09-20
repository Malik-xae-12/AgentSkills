# Playwright MCP Troubleshooting & Diagnostic Manual

This manual details recovery steps for common issues encountered when setting up or running `@playwright/mcp`.

---

## 1. Playwright Server Not Appearing in Antigravity or Claude

### Symptoms:
- MCP server list does not show `playwright`.
- Agent responds: *"I don't have access to browser tools"*.

### Resolution:
1. Verify the configuration path:
   - Global: `C:\Users\<YOUR_USERNAME>\.gemini\config\mcp_config.json`
   - Workspace: `.agents/mcp_config.json`
2. Ensure `playwright` is nested inside `"mcpServers"`:
   ```json
   {
     "mcpServers": {
       "playwright": { ... }
     }
   }
   ```
3. Completely restart Antigravity / Claude Code to re-read the configuration file.

---

## 2. JSON Syntax Errors

### Symptoms:
- Antigravity fails to load any MCP servers on startup.
- Error message: *"Unexpected token or trailing comma in mcp_config.json"*.

### Resolution:
- Remove trailing commas:
  ```json
  // BAD:
  "args": ["@playwright/mcp@latest",]
  
  // GOOD:
  "args": ["@playwright/mcp@latest"]
  ```
- Ensure quotation marks around all keys and strings are standard straight quotes (`"`), not curly quotes.

---

## 3. Node.js & NPX Execution Failures

### Symptoms:
- Error: `'npx' is not recognized as an internal or external command`.

### Resolution:
1. Open terminal and run:
   ```powershell
   node --version
   npm --version
   ```
2. If commands fail, download and install Node.js LTS from [nodejs.org](https://nodejs.org).
3. Restart your terminal and IDE so the updated PATH environment variable takes effect.

---

## 4. Browser Startup Timeout on First Run

### Symptoms:
- MCP starts but browser launch hangs or times out on the first test.

### Resolution:
- On its first launch, `@playwright/mcp` may download the Playwright Chromium browser binaries (~150MB).
- Allow 30–60 seconds for the download to complete.
- To pre-install browser binaries manually in your terminal, run:
  ```powershell
  npx playwright install chromium
  ```

---

## 5. Localhost Connection Refused (`ERR_CONNECTION_REFUSED`)

### Symptoms:
- Playwright MCP reports: `net::ERR_CONNECTION_REFUSED at http://localhost:3000`.

### Resolution:
1. Ensure your local dev server is actively running in a terminal:
   ```powershell
   npm run dev
   ```
2. Open a normal browser (Chrome/Edge) and verify `http://localhost:3000` loads manually.
3. If your app is running on a different port (e.g. `5173` for Vite, `8000` for FastAPI), update the URL in your prompt accordingly.

