# Encode and scrub reference

Everything here is load-bearing. Reproduce the commands and constants exactly, do not paraphrase flags or round numbers.

There are two ways to drive a scroll-scrub hero. Read section 0 and pick before doing anything else.

## Contents

0. Choosing the path
1. WebP frame sequence (default)
2. Video encode commands (fallback)
3. File layout
4. The scroll-scrub spec block, for Antigravity prompts
5. The damping code, for hand-fixing
6. The verification checklist block
7. Hosting thresholds

---

## 0. Choosing the path

**WebP frame sequence is the default.** Export the video as numbered WebP stills and draw them to a canvas by scroll index. There is no codec, no keyframe interval, no seeking, and no browser difference. Every frame is a complete image, so scrubbing is exact by construction. This is how the well-known Apple product pages do it.

**Video is the fallback.** Use it when the frame sequence would exceed roughly 8 MB total, when the page needs many separate scroll videos, or when the user already has a working video build and only wants a fix.

**Animated WebP is never the answer.** An `<img>` has no `currentTime`, so the browser plays an animated WebP on its own schedule with no scroll control at all. If a user asks to convert the mp4 to WebP, they want the frame sequence, and it is worth saying plainly that animated WebP cannot scrub. If they said WebP but meant WebM, that is a real video format and belongs in section 2 as a Firefox fallback.

### When the user asks whether MP4 is faster

They are usually comparing against a normal MP4, which is small because video codecs store differences between frames rather than whole frames. That comparison is not available here. A normal MP4 cannot scrub, and forcing a complete frame on every frame with `-g 1` discards the exact compression that made it small.

So the real comparison is all-keyframe MP4 against a WebP sequence, and MP4's size advantage is gone. Rough figures for 8 seconds at 1080p:

| Path | Download | First paint | Scroll cost | Requests |
|---|---|---|---|---|
| Normal MP4 | 2 to 4 MB | fast | cannot scrub | 1 |
| All-keyframe MP4 | 10 to 15 MB | slow | high, decodes on every seek | 1 |
| WebP sequence, 15fps at 1600px | 4 to 8 MB | fastest | near zero | around 120 |

WebP wins on the numbers that drive perceived speed. Largest contentful paint is a single 50 KB image rather than a video that must buffer and decode, and the page can render as soon as the first twenty frames land. During scroll, drawing an already-decoded image to canvas costs almost nothing, while seeking a video forces a fresh decode on every frame change. That decode cost is the actual reason video scroll heroes stutter on phones.

Its one real loss is request count, which has overhead on high-latency mobile connections. HTTP/2 multiplexing absorbs most of it.

**A third path exists.** Ship a normal small MP4 and decode it once into ImageBitmaps on the client at load, giving the smallest download with smooth scrubbing. The cost is a one to three second decode pass that blocks the main thread and behaves unreliably on low-end Android. This is the ImageBitmap cache described in section 4's video spec. Offer it when download size genuinely matters more than time to interactive, which is rare for a hero.

**Tuning order when the payload runs high:** lower the frame rate first, then the resolution, then quality. Dropping 15fps to 12 removes a fifth of the payload and is invisible on a slow camera move. Dropping WebP quality below 70 shows as banding in skies and gradients, which is most of the frame in a typical hero shot.

---

## 1. WebP frame sequence (default)

**Extract the frames.** From the project root, with the source video at `public/hero.mp4`:

```
mkdir -p public/frames
ffmpeg -i public/hero.mp4 -vf "fps=15,scale=1600:-2" \
  -c:v libwebp -quality 80 -compression_level 6 \
  public/frames/frame_%03d.webp
```

- `fps=15` over an 8 second clip gives 120 frames. That is enough resolution for a full viewport of scroll travel, and the eye cannot separate steps at that density when the motion is a slow camera move. Raise to 20 for faster moves, drop to 12 if the total size runs high.
- `scale=1600:-2` is deliberately below 1920. The canvas crops to cover anyway, and 1600 typically halves the payload with no visible loss.
- `-quality 80` is the dial. 70 to 85 is the useful range.
- `%03d` zero-pads to three digits, so the load loop can build paths predictably.

**Count what came out**, because the loader needs the exact number:

```
ls public/frames | wc -l
```

Windows: `dir /b public\frames | find /c /v ""`

**Check the total size:**

```
du -sh public/frames
```

Under 8 MB is comfortable. Over that, lower `fps` before lowering quality, since dropping frames costs less visually than compression artifacts on a slow camera move.

**Poster.** Frame 1 is already the poster. Reference `public/frames/frame_001.webp` directly rather than generating a separate JPG.

**Why this beats the video path:** no keyframe interval to get wrong, identical behavior in Firefox and on Android where video seeking is worst, no decode work on the scroll path, and every frame lands exactly. The cost is 120 requests on first load, which HTTP/2 multiplexing absorbs, and a visible loading state while frames preload.

---

## 2. Video encode commands (fallback)

Run both from the project root. Requires ffmpeg (`brew install ffmpeg`, `winget install Gyan.FFmpeg`, or apt).

**Poster, pulled from frame 0 so it matches what the video shows before it decodes:**

```
ffmpeg -i public/hero.mp4 -vframes 1 -q:v 3 public/hero-poster.jpg
```

**Re-encode for scrubbing:**

```
ffmpeg -i public/hero.mp4 -vf "fps=30,scale=1920:-2" \
  -c:v libx264 -crf 23 -g 1 -keyint_min 1 -sc_threshold 0 \
  -profile:v high -pix_fmt yuv420p -movflags +faststart \
  -an public/hero-scrub.mp4
```

Flag by flag, because each one is doing a job:

- `-g 1 -keyint_min 1 -sc_threshold 0` forces a complete frame on every frame. This is the whole trick. Browsers can only jump cleanly to complete frames, so without this the scrub moves in visible steps.
- `fps=30` over 8 seconds gives 240 frames, enough resolution for a full viewport of scroll travel.
- `-movflags +faststart` puts the index at the front so the browser can seek before the file finishes downloading.
- `-an` strips audio. It blocks autoplay policies in some browsers and is never heard here anyway.
- `-crf 23` is the quality dial. Lower is better and larger, 18 to 28 is the useful range.

Then swap the files so the app path stays `hero.mp4`:

```
mv public/hero.mp4 public/hero-original.mp4
mv public/hero-scrub.mp4 public/hero.mp4
```

Keep `hero-original.mp4`. It is the only copy at full quality, and it is also the b-roll for showing the stutter side by side.

**WebM fallback, optional.** Skip unless Firefox is showing problems. H.264 covers everything that matters.

```
ffmpeg -i public/hero.mp4 -c:v libvpx-vp9 -crf 32 -b:v 0 -g 1 -an public/hero.webm
```

---

## 3. File layout

**Frame sequence:**

```
project/
  public/
    frames/
      frame_001.webp    served at /frames/frame_001.webp
      ...
      frame_120.webp
  _assets/              outside public, the source mp4 and raw downloads
```

**Video fallback:**

```
project/
  public/
    hero.mp4            served at /hero.mp4, not /public/hero.mp4
    hero-poster.jpg
  _assets/
```

The `/public` prefix is not part of the URL. This trips up nearly every first run.

Keep the source mp4 in `_assets/`. It is the only full-quality copy, it is what you re-extract from if the frame count needs changing, and it is the b-roll for showing a stutter comparison.

If the frames folder or encode runs large, add to `.gitignore`:

```
public/frames/
public/*.mp4
```

---

## 4. The scroll-scrub spec block

Paste one of these into the Antigravity prompt as its own section, right after assets. Adjust the frame count and paths only.

**Frame sequence version (default):**

```
SCROLL-SCRUBBED FRAME SEQUENCE
This is the core of the build. Get it right before anything else.
- Fixed inset-0, z-0, pointer-events-none, bg #0a0a0a, overflow hidden.
- A single full-bleed <canvas>. No <video> element anywhere in this build.
- Frames live at /frames/frame_001.webp through /frames/frame_[COUNT].webp,
  zero-padded to three digits. Total frame count is [COUNT].
- On mount, preload every frame into an Image array. Track how many have
  loaded and show a minimal progress state until at least the first 20 are
  ready, then render and continue loading the rest in the background.
- progress = scrollY / (scrollHeight - innerHeight), clamped 0 to 1.
- Smooth inside requestAnimationFrame:
    smoothed += (target - smoothed) * 0.12
- frameIndex = Math.round(smoothed * (COUNT - 1)), clamped to the array.
  Only redraw when the index actually changes.
- Draw with object-cover math: scale to max, center crop.
- Canvas backing store sized to min(devicePixelRatio, 2), reset on resize.
- Scroll listener passive. Under prefers-reduced-motion, draw frame 1 once
  and skip the rAF loop entirely.
```

**Video version (fallback only):**

```
SCROLL-SCRUBBED VIDEO BACKGROUND
This is the core of the build. Get it right before anything else.
- Fixed inset-0, z-0, pointer-events-none, bg #0a0a0a, overflow hidden.
- Layers bottom to top: poster img (object-cover, fades out over 500ms
  once the video has a decoded frame), then the video (muted, playsInline,
  preload auto, object-cover), then a canvas that draws scrubbed frames.
- The video NEVER autoplays and never loops. Motion is scroll-driven only.
- progress = scrollY / (scrollHeight - innerHeight), clamped 0 to 1.
- Smooth inside requestAnimationFrame:
    smoothed += (target - smoothed) * 0.12
- Fallback path: seek the video to smoothed * (duration - 0.05), only when
  the delta exceeds 0.04s.
- Preferred path: an offscreen video extracts up to 90 frames (or
  duration * 12, min 24) at max 960px wide into ImageBitmaps, starting
  after loadeddata plus a 300ms yield. Once cached, the canvas draws by
  smoothed index and the video element fades out.
- Canvas DPR capped at min(devicePixelRatio, 2). Draw with object-cover
  math, scale to max, center crop.
- Scroll listener passive. Under prefers-reduced-motion, skip the video and
  canvas entirely, show only the poster.
```

The frame sequence version is shorter because the hard parts disappear. There is no decode path, no seek tolerance, no poster crossfade, and no browser variation to defend against.

---

## 5. The damping code

For hand-fixes or when explaining what generated code got wrong.

**Frame sequence:**

```js
const COUNT = 120;
const canvas = document.querySelector('#hero-canvas');
const ctx = canvas.getContext('2d');
const wrap = document.querySelector('#hero-wrap'); // tall, e.g. 300vh

const frames = Array.from({ length: COUNT }, (_, i) => {
  const img = new Image();
  img.src = `/frames/frame_${String(i + 1).padStart(3, '0')}.webp`;
  return img;
});

let target = 0, current = 0, lastDrawn = -1;

window.addEventListener('scroll', () => {
  const r = wrap.getBoundingClientRect();
  target = Math.min(Math.max(-r.top / (r.height - innerHeight), 0), 1);
}, { passive: true });

function draw(img) {
  const dpr = Math.min(devicePixelRatio, 2);
  const w = canvas.clientWidth, h = canvas.clientHeight;
  canvas.width = w * dpr; canvas.height = h * dpr;
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  const s = Math.max(w / img.width, h / img.height);
  const dw = img.width * s, dh = img.height * s;
  ctx.drawImage(img, (w - dw) / 2, (h - dh) / 2, dw, dh);
}

(function tick() {
  current += (target - current) * 0.12;
  const i = Math.round(current * (COUNT - 1));
  if (i !== lastDrawn && frames[i]?.complete) { draw(frames[i]); lastDrawn = i; }
  requestAnimationFrame(tick);
})();
```

The `lastDrawn` guard matters. Without it the canvas redraws sixty times a second even when the frame has not changed, which burns battery for nothing.

The `0.12` is the damping factor. Lower feels heavier and lags behind the thumb, higher feels sharper and starts to jitter. 0.08 to 0.18 is the usable range.

Markup: a `<canvas>` inside a `position: sticky; top: 0` container, wrapper at 300vh desktop and 200vh mobile.

**Video fallback:**

```js
const vid = document.querySelector('#hero-vid');
const wrap = document.querySelector('#hero-wrap');
let dur = 0;

vid.addEventListener('loadedmetadata', () => { dur = vid.duration; });

let target = 0, current = 0;

window.addEventListener('scroll', () => {
  const r = wrap.getBoundingClientRect();
  const p = Math.min(Math.max(-r.top / (r.height - innerHeight), 0), 1);
  target = p * dur;
}, { passive: true });

(function tick() {
  current += (target - current) * 0.12;
  if (dur) vid.currentTime = current;
  requestAnimationFrame(tick);
})();
```

Markup: `<video muted playsinline preload="auto" poster="/hero-poster.jpg" width="1920" height="1080">` inside the same sticky container. The explicit dimensions prevent the hero from jumping as the file loads.

---

## 6. The verification checklist block

Always the last section of an Antigravity prompt. Antigravity's agents drive a real browser, which is the reason to use it over a paste into an editor. A prompt without this throws that away.

```
VERIFY IN THE BROWSER BEFORE YOU REPORT DONE
1. Open the page, scroll slowly top to bottom, confirm the frame advances
   with scroll and stops when scroll stops.
2. Confirm nothing animates on its own with the page static.
3. Scroll back up and confirm the sequence runs backward.
4. Scrub fast and confirm no stutter, tearing, or blank frames.
5. Check the network tab and confirm every frame returns 200, no 404s.
6. Toggle prefers-reduced-motion and confirm a single static frame renders
   with no animation loop running.
Screenshot the hero at scroll 0, 0.5 and 1.0 and show me the three.
```

Check 2 catches the most common failure on the video path. Check 5 catches the most common failure on the frame path, which is an off-by-one in the zero-padding, producing a 404 on the first or last frame.

---

## 7. Hosting thresholds

**Frame sequence:** typically 4 to 8 MB total for 120 WebP frames at 1600px. Serve from `/public` up to about 8 MB. Beyond that, move the `frames/` folder to a CDN and change the path prefix in the loader.

**Video:** all-keyframe encodes run large, typically 10 to 15 MB at 1080p for 8 seconds. That is expected and cannot be engineered away without dropping resolution or frame rate. Under 6 MB serve locally, over 6 MB use a CDN (Cloudflare R2, Bunny, Vercel Blob).

To check: `du -sh public/frames` or `ls -lh public/hero.mp4`.
