# Browser Testing Workflows & Prompt Library

This reference provides copy-paste prompts and testing procedures for verifying rendered web applications using Playwright MCP.

---

## 1. Local Server Verification Prompt

Use this prompt when testing a newly implemented feature on your local machine:

```text
Use Playwright MCP.
Open http://localhost:3000.
Do not modify any source files.

Perform the following checks:
1. Verify page renders with HTTP 200 and no blank screen.
2. Check browser console logs for JavaScript errors, unhandled rejections, or React hydration warnings.
3. Check network panel for failed API calls (4xx / 5xx) or broken asset URLs (images, fonts).
4. Verify primary CTA buttons and links respond properly.
5. Take full-page and hero screenshots.

Report all discovered issues with line numbers or error messages.
```

---

## 2. Responsive Layout Matrix Prompt

Use this prompt to audit responsive styling and mobile usability:

```text
Use Playwright MCP.
Navigate to http://localhost:3000.

Evaluate the layout across these exact viewports:
- Desktop Wide: 1920 × 1080
- Desktop Standard: 1440 × 900
- Tablet Landscape: 1024 × 768
- Tablet Portrait: 768 × 1024
- Mobile Large: 390 × 844 (iPhone 13/14)
- Mobile Compact: 375 × 812 (iPhone Mini / SE)

For each viewport, verify:
- No horizontal scrollbars or element clipping
- Navigation switches cleanly between desktop navbar and mobile drawer
- Text remains legible with high contrast
- Button hit targets are at least 44x44px on mobile

Take screenshots at 1920px, 768px, and 375px.
Do not modify any files.
```

---

## 3. Scrollytelling & Motion Scroll Verification Prompt

Use this prompt to verify scroll-scrubbed websites, canvas animations, and sticky hero sections:

```text
Use Playwright MCP.
Open http://localhost:3000.

Scroll through the page smoothly from top (0px) to bottom:
1. Increment scroll by 100px increments.
2. Verify image frames load sequentially without 404 errors.
3. Verify video/canvas scrubbing does not hitch or stutter.
4. Verify sticky headers and section overlays transition smoothly.
5. Confirm no memory leak warnings or dropped frame errors in console.

Capture screenshot at 0% scroll, 50% scroll, and 100% scroll.
Do not modify any files.
```

