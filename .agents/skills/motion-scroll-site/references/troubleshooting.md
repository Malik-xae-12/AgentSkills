# Troubleshooting and design critique

Read this at the start of Mode C. Work from the symptom, and check the cheap causes before the expensive ones. Telling someone to re-encode when their file path is wrong costs them twenty minutes.

## Contents

1. Diagnostic order
2. Symptom table
3. Platform-specific problems
4. Design critique checklist
5. What to say when the build is fine

---

## 1. Diagnostic order

Ask for one thing before diagnosing: what happens on screen, in their words, and on which device. "It doesn't work" covers six different failures with different fixes.

Then check in this order, cheapest first:

1. Is the file where the code thinks it is (`/hero.mp4`, not `/public/hero.mp4`)
2. Is autoplay on when it should be off
3. Was the re-encode actually run, or was the original file kept
4. Is the damping loop present
5. Is the spacer tall enough
6. Is it device-specific

---

## 2. Symptom table

| Symptom | Likely cause | Fix |
|---|---|---|
| Antigravity asks for the video and scaffolds into Downloads | Workspace not opened on the project folder, so the agent created its own | Open the project folder as the workspace first, then paste. Add the WORKSPACE block from the skill's step 6 to the top of the prompt |
| Blank frame at the very start or very end of the scroll | Off-by-one in zero-padding or frame count, so `frame_000` or `frame_121` is requested | Check the network tab for 404s. Frames are 1-indexed, `frameIndex = Math.round(p * (COUNT - 1))` then add 1 when building the filename |
| Hero blank until fully scrolled once | Frames not preloaded, each one fetches on first display | Preload all frames into an Image array on mount, show progress until the first 20 are ready |
| Converted to animated WebP, nothing scrubs | Animated WebP renders in an `<img>`, which has no `currentTime` and no frame control | Not fixable as animated WebP. Re-extract as a numbered frame sequence per section 1 of the encode reference |
| Video plays by itself, scroll does nothing | Agent added `autoplay` and `loop`, ignored the scrub spec | Remove both attributes, confirm `currentTime` is driven by the rAF loop |
| Frames advance in visible steps (video path) | Original export still in place, sparse complete frames | Re-encode with `-g 1`. Check with `ffprobe -select_streams v -show_frames -show_entries frame=key_frame hero.mp4 \| head -40`, every entry should read 1 |
| Motion lags behind the thumb | Damping factor too low, or the index set inside the scroll event | Raise toward 0.18, and move the assignment into requestAnimationFrame |
| Jittery, twitchy motion | No damping at all, index assigned straight off scroll | Add the rAF loop from the scrub reference |
| Canvas redraws constantly, battery drains | No guard against redrawing the same frame | Track `lastDrawn` and skip the draw when the index has not changed |
| Black hero, nothing renders | Wrong path, or files never copied into `public` | Serve path is `/frames/...`, not `/public/frames/...`. Check the network tab for 404s |
| Video finishes halfway down the page | Spacer too short for the scroll distance | Raise the wrapper height, 300vh desktop and 200vh mobile is the starting point |
| Sequence never reaches the last frame | Progress clamped wrong, or index math uses `COUNT` instead of `COUNT - 1` | Clamp 0 to 1, and index against `COUNT - 1` |
| Smooth on desktop, stutters on phone (video path) | Encode too large to seek on every frame on mobile hardware | Switch to the frame sequence, which removes the decode path entirely |
| Nothing renders until first tap on iPhone (video path) | iOS Safari will not seek a paused video before first play in some versions | Switch to the frame sequence. If staying on video, ensure `muted`, `playsinline`, `preload="auto"`, and a poster |
| Layout jumps as the page loads | No reserved space, or poster/video missing explicit dimensions | Fix the hero container height, add `width` and `height` to any `<img>` or `<video>` |
| Slow first paint | Large payload served from static hosting | Lower the frame rate before lowering quality. Over 8 MB, move `frames/` to a CDN |
| Video link is dead | Flow URLs are signed and expire | Regenerate, download the file, never reference the address bar link |
| Scroll feels dead near the top or bottom | Progress calculated against the wrong element | Measure against the sticky wrapper's bounding rect, not `document.body` |

---

## 3. Platform-specific problems

**Firefox** is the strictest about keyframe spacing and will look choppy where Chrome and Safari look fine. If it is choppy only in Firefox, the encode is the cause even when other browsers pass.

**Android Chrome** handles native-scroll seeking poorly regardless of encode. The frame cache is not optional here.

**Antigravity generation quirks.** Two things it reliably gets wrong on a first pass: it adds autoplay because that is what background video normally means, and it drops the damping line because the code looks correct without it. Check both before assuming a deeper problem. If the frame cache logic comes out shaky, switch the model and re-run only the video-layer section rather than rebuilding the page.

---

## 4. Design critique checklist

Run these as a senior designer would, and lead with the single biggest problem rather than the full list.

**Legibility over motion.** Text over video needs a scrim or a drop shadow, not an opaque panel. An opaque panel solves contrast by deleting the reason the video is there. If contrast still fails, grade the video darker rather than making the text heavier.

**Where the text sits.** Check the copy against the busiest part of the frame across the whole scroll range, not just frame 0. Text that reads at the start and dissolves into detail at 60% is the most common miss, and it is invisible in a single screenshot.

**Accent discipline.** One accent color, used on almost nothing. If the accent appears on badges, buttons, links, and borders, nothing is primary. Pull it back to the primary action and one structural mark.

**Type scale.** Animated heroes need genuinely large headlines, 6rem and up on desktop. A 3rem headline over full-bleed video reads as a caption.

**Reveal restraint.** If everything animates in, nothing arrives. Reserve reveals for section entries, keep them at 700ms and roughly 20 to 30px of travel, and let small elements appear without their own animation.

**Motion honesty.** The scroll move should serve the content. A camera push toward the product is direction. A camera wandering the scene is a screensaver.

**Reduced motion.** A path that shows the poster with no video work, not just a paused video. This is an accessibility requirement, and it is also the fallback for low-end devices.

---

## 5. What to say when the build is fine

If nothing is broken and the user wants a review, resist listing. Name the one change with the highest leverage, say why, and stop. Offer the rest if they want it.

Useful things to check that people miss: social preview tags, since a Vite single-page app serves an empty shell and shares render blank; the mobile scroll feel, which is a different experience from desktop and is where most traffic lands; and whether the hero actually says what the product is, which full-bleed video has a habit of hiding.
