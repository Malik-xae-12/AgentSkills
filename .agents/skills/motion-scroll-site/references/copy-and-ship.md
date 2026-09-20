# Copy and ship

Read this before writing section content into an Antigravity prompt, and again before the user deploys.

The layout is the easy part. A generated animated site fails on copy far more often than on code, because the template supplies structure and the model fills it with words that describe nothing.

## Contents

1. Writing the section copy
2. The scroll-hero copy problem
3. Pre-ship checklist
4. Social preview tags
5. Deploy

---

## 1. Writing the section copy

Copy comes from the brief in step 1. If the brief was thin, the copy will be thin, and no amount of prompt engineering fixes that. Go back and ask rather than inventing a business.

**Rules that survive contact with a real audience:**

Say what it is before saying why it is good. A hero that reads "Built to last" could be a watch, a tent, or a database. One concrete noun fixes it.

Numbers beat adjectives. "40 cars delivered" outperforms "trusted by many" because it can be checked. If the user has no numbers, use specifics instead: a year, a material, a process step.

Every section earns its scroll. If a section could be deleted without the visitor losing anything, delete it. Three strong sections beat six padded ones, and on a scroll-driven page each extra section stretches the video thinner.

Write the call to action as the thing the visitor does, not the thing you want. "Book a build slot" over "Get started". Specific verbs convert because they set expectations.

Avoid the generated-site tells: rule-of-three headlines, "elevate your", "seamlessly", "we don't just X, we Y", and any sentence that would fit on a competitor's page unchanged.

**Structure that works with a scroll hero:**

| Section | Job | Length |
|---|---|---|
| Hero | Name the thing, one claim, one action | Headline plus one line |
| Proof | Numbers, names, or credentials | Four stats or three logos |
| Substance | What they actually get, in specifics | Three items, one line each |
| Close | Repeat the action with less friction | One line plus the button |

Anything beyond this is optional and usually costs more than it adds.

## 2. The scroll-hero copy problem

Full-bleed video hides the message. It is the single most common failure of this whole format, and it does not show up in a screenshot of frame 0.

Three checks:

**Does the hero say what the product is?** Read the headline with the video removed. If a stranger could not name the business from it, the video is carrying meaning the copy should carry.

**Does the copy survive the whole scroll?** Text that reads cleanly at frame 1 can land on the busiest part of frame 80. Check the copy against the frame at 30%, 60%, and 100%, not just the opening.

**Does the video compete with the copy?** If the camera move ends on visual chaos exactly where the call to action sits, move the copy or shorten the move. The move serves the message, not the other way round.

## 3. Pre-ship checklist

Run before deploying, in this order.

- Every frame returns 200, no 404 at the first or last index
- Video or poster elements carry explicit `width` and `height`
- No `transition: all` anywhere in the reveal code
- Reduced-motion path renders a single static frame with no loop running
- Icon-only buttons have `aria-label`, form inputs have labels
- Focus rings visible on every interactive element, no bare `outline: none`
- Headline reads as the business with the video hidden
- Tested on a real phone, not a desktop browser resized
- Total payload under 8 MB, or frames moved to a CDN
- Social preview tags present, see below

For a full code-level pass, hand off to the `web-design-guidelines` skill, which fetches Vercel's Web Interface Guidelines and reports `file:line` findings.

## 4. Social preview tags

A Vite single-page app serves an empty HTML shell, so every share on WhatsApp, Slack, LinkedIn, or X renders blank. This is invisible in local testing and it is the most common reason a good site gets no traction from the first share.

Add to `index.html`, in `<head>`:

```html
<meta property="og:title" content="[headline]" />
<meta property="og:description" content="[one line, under 155 chars]" />
<meta property="og:image" content="https://[domain]/frames/frame_001.webp" />
<meta property="og:url" content="https://[domain]/" />
<meta name="twitter:card" content="summary_large_image" />
```

The og:image must be an absolute URL on the live domain. Relative paths fail silently in every scraper. Frame 1 is already the right image and costs nothing extra.

Test the result by pasting the live URL into a private message to yourself before announcing it anywhere.

## 5. Deploy

Vercel is the shortest path from a Vite project:

```
npm i -g vercel
vercel
```

Accept the defaults. The build command and output directory are detected. First deploy gives a preview URL, `vercel --prod` promotes it.

**Two things to check on the live URL, not locally:**

Frames load from the deployed origin. A path that worked in dev can 404 in production if the frames folder was gitignored and never uploaded. If they are gitignored deliberately, they need to be on a CDN with the loader pointing there.

Scroll feel on a real phone over mobile data. Local testing runs off disk with no latency, which hides the loading state entirely.

**Trademark note.** If the site uses a real brand name, logo, or trademarked model designation, that is fine for portfolio and concept work and a problem for anything published as advertising or run as a paid campaign. Say this once, plainly, when a brand name appears in the copy. Do not repeat it.
