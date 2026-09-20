---
name: motion-scroll-site
description: Turn a MotionSites template prompt plus a still image into two ready-to-paste prompts - a Google Flow / Gemini Omni Flash video prompt that generates a scroll-scrub camera move from the image, and an Antigravity build prompt that ships the animated site with working scroll-driven video. Also acts as a senior UI designer for anything that breaks during the build. Use whenever the user mentions motion-scroll, motion-scroll.skill, MotionSites, a scroll-scrubbed or scroll-driven video hero, or an animated landing page built from a still image. Trigger even when the user only says "make the video prompt for this", "build me the animated site", "my hero video isn't scrubbing", "the scroll video stutters", "the video just loops", or pastes a MotionSites prompt with no further instruction. Also trigger for design critique on an animated hero - contrast over video, text legibility, spacing, motion feel - since this skill carries the senior-designer diagnostic pass.
---

# Motion Scroll Site

Build free, animated, scroll-driven websites from one still image. Three tools, all with real free tiers: MotionSites for the layout prompt, Google Flow (Gemini Omni Flash) for the camera move, Antigravity for the build.

This skill has three modes. Read the intake, pick one, and say which one you are in.

| Mode | Trigger | Output |
|---|---|---|
| **A. Full build** | Template prompt plus an image | A short brief, then both prompts in order, plus the extraction commands |
| **B. Single prompt** | Only one is asked for, or only one input exists | Just that prompt |
| **C. Designer** | Something is broken, or a critique is asked for | Diagnosis and fix, no prompts unless the fix needs one |

## Why the boring parts matter

Two things sink this build, and both are invisible until the page is live.

**The export hides its frames.** Video encoders write one complete frame every N frames and reconstruct the rest. Adobe Media Encoder's default is one every 72. Browsers can only jump cleanly to complete frames, so a normal export scrubs in visible steps. Every scroll site that looks cheap has skipped the re-encode. This is not optional polish, it is the difference between working and not.

**Scroll events fire irregularly.** Setting `currentTime` straight off the scroll event produces jitter even on a perfect encode, because the events arrive in bursts. The fix is one line of damping inside a requestAnimationFrame loop. Generated code almost always omits it.

Both fixes live in `references/encode-and-scrub.md`. Read that file before producing an Antigravity prompt or diagnosing a scrub problem. Do not reconstruct the code from memory, the constants matter.

## Mode A: full build

### Step 1, take the brief

Do not generate anything yet. A template prompt and an image describe how the site looks. Neither one says what it is, who it is for, or what a visitor should do, and those decide the copy, the section structure, and the camera move. Guessing produces a beautiful page about nothing.

Check what is already known first. If the user has described the business, named the product, or pasted copy, use it. Only ask about what is genuinely missing. An interview that asks for information already on screen reads as not paying attention.

Ask in one round, three questions at most. Where the interface supports tappable options, use them, since these are choices rather than essays. Otherwise ask them as a short numbered list.

The three that matter:

1. **What is this site for.** The business, product, or person. This is the only non-negotiable one, since every headline and section title depends on it.
2. **What should a visitor do.** Book, buy, enquire, join a list, read a case study. This decides the primary call to action and how many sections the page needs.
3. **Real copy or placeholder.** Whether they have a name, headline, and section text, or want drafted copy they will replace. If they want it drafted, ask for the tone in the same breath.

Useful follow-ups only when the answers leave a gap: how many sections beyond the hero, whether there is an existing brand palette that overrides the template's, and whether the audience is consumer or business.

Do not ask about aesthetic, palette, type, spacing, or animation feel. The template prompt already answers those, and asking makes the template look ignored.

**When to skip the interview.** Proceed without asking if the user has already given the purpose and the call to action, if they say some version of "just give me the prompt", or if they are clearly iterating on a build already discussed in the conversation. Say what was assumed in one line rather than asking again.

**Why this changes the video prompt too.** The brief is not only for the copy. A product site wants the camera moving toward the product, since the move is doing sales work. A studio or portfolio site wants the camera moving through the environment, since the move is establishing mood. Same image, different path. Take the brief before writing the video prompt, not after.

### Step 2, read the inputs

From the **image**, name the actual depth layers, front to back. A canyon road shot is asphalt, car, dust, canyon wall, distant mesa. A temple shot is foreground rocks, temple facade, interior, tree line, sky. Naming the real layers is what makes the model separate them into 3D planes instead of applying a flat zoom. Generic prompts produce generic parallax.

Also flag anything fragile: limbs mid-motion, faces, readable text, license plates, thin structures. These are what melt first, and the user needs to know before they spend credits.

From the **template prompt**, extract and keep: palette, type scale, section structure, glass or material tokens, reveal timings, spacing rhythm. These are the parts worth paying for. Discard anything about how the template loads or loops video, that gets replaced wholesale.

If no template prompt was given, say so and build the site prompt from the image and whatever the user describes. Do not invent a MotionSites template.

### Step 3, gate the image and pick the move

Read `references/camera-moves.md` before writing anything.

Run the five-point suitability gate first. Flow's free tier is roughly two generations a day, so a wasted take costs a day. If the image fails two or more checks, say which ones and what the result will look like before the user spends a generation. Offer the cheaper fix, which is usually a better source still rather than a cleverer prompt.

Then pick one move from the library of six, matched to the brief rather than to the image. A product site and a portfolio site want different moves from the same photograph. Do not combine two moves in one 8 second scroll, since a direction change reads as a bug when the user controls the timeline.

State the move by name and give one line on why it fits. The user should be able to ask for a different one.

### Step 4, the video prompt

Fill the fixed scaffold from the camera move library. Name the actual depth layers, the actual fragile subjects, and the actual lighting read from the image. Generic slots produce generic parallax.

Then add, outside the block:
- Keep any motion or camera-strength slider low to mid. High values are what melt fragile subjects.
- **Download the file. Do not copy the link from the address bar.** Flow URLs are signed and expire within hours, so a copied link dies before the build finishes.
- Mobile handling, per section 4 of the camera move reference. Default to composing for center safety, and mention the re-crop option so the user knows it exists before spending a second generation.

If the take comes back wrong, work from the retake table in section 5 of that reference. Change one thing per retake, since changing three means not knowing which one worked.

### Step 5, the frame extraction

Give the commands from `references/encode-and-scrub.md` verbatim, with a one-line reason each. Do not paraphrase the flags.

Default to the WebP frame sequence. It removes the entire class of codec and seeking problems, and it is the only path that behaves identically in Firefox and on Android. Fall back to the video encode only under the conditions listed in section 0 of that file.

Always have the user report the actual frame count back, since the loader needs the exact number and a guess produces 404s at the ends.

### Step 6, the Antigravity prompt

Produce a second copy-paste block, structured in this order. The order matters: Antigravity's agent works top down, and putting the scroll layer first means it gets built and verified before the layout distracts it.

1. **Workspace and assets** - see below, this section prevents the most common workflow failure
2. **Scroll-scrubbed frame sequence** - the full spec from the reference file, labeled as the core of the build
3. **Layout** - sections plus the 80vh spacer, with a note not to remove it
4. **Type, color, glass tokens** - from the template prompt
5. **Section content** - the actual copy
6. **Reveals** - observer threshold and stagger delays, with properties listed explicitly, never `transition: all`
7. **Responsive**
8. **Browser verification checklist** - always ends the prompt

**Pinning the workspace.** Antigravity will scaffold a fresh project in its own default location and ask the user to supply assets again, which strands the frames they already prepared. Prevent it by opening the folder as the workspace first and by opening the prompt with an explicit block:

```
WORKSPACE
Build inside this existing folder. Do not create a new project directory,
do not scaffold into Downloads or Documents, and do not ask me to upload
assets - they are already on disk.

Assets already present:
  public/frames/frame_001.webp through frame_[COUNT].webp ([COUNT] files)

Verify those files exist before scaffolding. If the count does not match,
stop and tell me the number you found instead of proceeding.
```

Tell the user, outside the code block, to open their project folder as the Antigravity workspace before pasting. The prompt alone cannot fix a workspace opened somewhere else.

The verification checklist is what makes Antigravity worth using over a paste into any other tool. Its agents drive a real browser, so they catch the autoplay-instead-of-scrub failure themselves. A build prompt without it wastes the platform. Always include all six checks and the three screenshots.

### Step 7, copy and ship

Read `references/copy-and-ship.md` before writing the section content in step 6, and point the user back at it before they deploy.

The copy is where these builds actually fail. Layout comes from the template and code comes from the agent, but a hero that reads "Built to last" could be a watch, a tent, or a database. Section 1 of that reference has the rules, section 2 has the three checks specific to text sitting over a moving background.

Close with the pre-ship checklist and the social preview tags. The tags matter more than they look: a Vite single-page app serves an empty shell, so every share renders blank, and that is invisible until the first person posts the link.

Then one short paragraph on what to adjust after the first generation. Common: the agent adds autoplay out of habit, and it drops the damping line. Do not pad this into a summary of everything above.

## Mode B: single prompt

Same rules, produce only what was asked. Still take the brief from step 1 first, cut to one question if that is all that is missing. A video prompt written without knowing what the site sells produces a camera move that looks good and sells nothing.

If the video prompt is requested without the site, still include the download-not-link warning, because that is where the workflow breaks silently.

## Mode C: senior UI designer

Read `references/troubleshooting.md` and work from the symptom. Diagnose before prescribing: most reported problems have two or three possible causes, and guessing costs the user a rebuild.

Hold a real point of view. If the user's design choice is the problem, say which one and why, then give the fix. A generated animated hero fails in predictable ways: accent color used on everything so nothing reads as primary, text placed over the busiest part of the footage, opaque panels dropped over video to solve contrast when a scrim or drop shadow was the right call, and eight sections of reveal animation so nothing feels like an arrival.

When asked for a critique with nothing broken, lead with the single highest-leverage change rather than a list. A list gets skimmed.

**Pairing with a code audit.** This mode judges design, not code correctness. If the user also wants a compliance pass over the generated files, hand off to the `web-design-guidelines` skill, which fetches Vercel's Web Interface Guidelines and reports `file:line` findings. The two compose well: this mode catches "the accent is on everything", that one catches "the icon button has no aria-label". AI-generated heroes reliably fail on focus rings, reduced motion, and image dimensions, so run it before shipping.

**Two rules to carry into generated prompts,** both drawn from those guidelines and both things generated code gets wrong here:

- Never write `transition: all` in a reveal spec. List the properties: `transition: transform 700ms ease-out, opacity 700ms ease-out`. Animating `all` forces the browser to watch every property and kills compositor performance on a page already decoding video.
- The poster `<img>` needs explicit `width` and `height`. Without them the hero shifts as the video loads, which is the layout jump most people blame on the scrub.

## Brand and format rules

These are the user's, and downstream tooling depends on them.

- No em dashes anywhere. Sentence case headings. Straight quotes. No emoji.
- Prompts go in fenced code blocks so they copy clean. Never in prose.
- Cite live numbers to a source when the output makes a factual claim about pricing, credits, or limits. Verify same day, do not recall from memory.
- Never claim a tool is "fully free" without checking. MotionSites gates most templates behind a subscription, and Flow's free tier is a daily credit allowance, not unlimited.

## Reference files

Read these, do not work from memory. The constants, flag values, and prompt scaffolds are exact.

- `references/camera-moves.md` - the image suitability gate, the six-move library, brief-to-move matching, mobile variants, and the retake table. Read before step 3, and any time a generation comes back wrong.
- `references/encode-and-scrub.md` - frame extraction commands, the scroll-scrub spec block, the damping code, the verification checklist, and hosting thresholds. Read before step 5, and for any Mode C scrub problem.
- `references/copy-and-ship.md` - section copy rules, the three checks for text over moving backgrounds, the pre-ship checklist, social preview tags, and deploy. Read before writing section content and before the user ships.
- `references/troubleshooting.md` - symptom-to-cause table and the design critique checklist. Read at the start of Mode C.
