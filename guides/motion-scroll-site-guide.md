# Guide: `motion-scroll-site` Skill

> **Skill Identifier**: `motion-scroll-site`  
> **Source Location**: [`.agents/skills/motion-scroll-site/`](../.agents/skills/motion-scroll-site/SKILL.md)  
> **Package Bundle**: [`claude-upload/motion-scroll.skill`](../claude-upload/motion-scroll.skill)

---

## 1. What is this Skill?

The `motion-scroll-site` skill builds animated, scroll-driven websites starting from a **single still image** and an optional design template. It coordinates three tools:
1. **MotionSites**: Layout and styling template prompt.
2. **Google Flow (Gemini Omni Flash)**: Generates a smooth, scroll-scrubbed camera move from the still image.
3. **Google Antigravity / AI Agent**: Builds the interactive website with working scroll-driven video and frame-by-frame scrubbing.

It also doubles as a **Senior UI Designer** to diagnose and fix contrast over video, jittery scroll scrub, text legibility, and reveal timing issues.

---

## 2. How to Use this Skill

Provide the AI with an image and a template description or prompt:

### Mode A: Full Build (Image + Template)
> **You say**:  
> *"Here is an image of an electric mountain bike on a ridge and a minimal tech landing page prompt. Build me the motion-scroll site."*

**What happens:**
1. The AI takes a short 3-question brief (Business/Product purpose, Visitor CTA, Real copy vs placeholder).
2. Deconstructs the image into actual 3D depth planes (e.g. foreground rocks, bike, dust, mountain ridge, sky).
3. Gates the image for AI video suitability (identifying fragile subjects like spokes, fingers, or license plates).
4. Produces the **Google Flow Camera Move Prompt**.
5. Produces the **FFmpeg frame extraction command**.
6. Produces the **Antigravity Build Prompt** with damped scrubbing code.

---

### Mode B: Single Prompt Request
> **You say**:  
> *"Make the Google Flow video prompt for this image."*  
> *OR*  
> *"Write the Antigravity prompt to scrub a video on scroll."*

Produces only the requested prompt without unnecessary conversation.

---

### Mode C: UI Designer Critique & Troubleshooting
> **You say**:  
> *"My scroll video stutters when scrubbing."*  
> *OR*  
> *"The text is unreadable over the video background."*  
> *OR*  
> *"The video just loops instead of scrubbing on scroll."*

The AI diagnoses the issue and provides the surgical CSS or JavaScript fix.

---

## 3. The Two Invisible Traps in Scroll Video Sites

Most AI-generated scroll sites feel cheap or broken due to two technical issues:

1. **Missing Keyframes (Export hides its frames)**:
   - Video codecs normally store complete frames only once every 72 frames and interpolate the rest. Browsers cannot jump smoothly to interpolated frames.
   - **Solution**: The skill instructs extracting a sequence of WebP frames (`public/frames/frame_001.webp` through `frame_XXX.webp`), eliminating codec seeking bugs on Firefox and mobile browsers.

2. **Scroll Event Jitter**:
   - Setting `video.currentTime` directly inside a `window.onscroll` handler causes severe stuttering because scroll events fire irregularly.
   - **Solution**: The skill embeds a **damped requestAnimationFrame loop** that interpolates target position and current progress smoothly:
     ```javascript
     let currentProgress = 0;
     let targetProgress = 0;
     const damping = 0.08;

     function render() {
       currentProgress += (targetProgress - currentProgress) * damping;
       // draw frame corresponding to currentProgress
       requestAnimationFrame(render);
     }
     ```

---

## 4. What is the Exact Output?

When Mode A is run, you receive three exact outputs in order:

### Output 1: Google Flow Video Prompt
A ready-to-paste prompt for Flow with:
- Exact depth planes identified from your image
- Camera motion constraints (slow push-in, orbital, pull-back)
- Motion strength sliders set low to prevent melting fragile subjects
- Explicit instructions to **download the MP4 file** (not copy the expiring CDN link)

### Output 2: FFmpeg Frame Extraction Commands
The terminal commands to convert the downloaded video into an optimized WebP frame sequence:
```powershell
# Extract frames as WebP sequence:
ffmpeg -i input.mp4 -vf "fps=30,scale=1920:-1:flags=lanczos" -q:v 80 public/frames/frame_%03d.webp
```

### Output 3: Antigravity Build Prompt
A complete build specification for Antigravity containing:
- **Pinned Workspace Block**: Prevents Antigravity from scaffolding into random temp directories.
- **Scroll-Scrubbed Canvas Layer**: Working canvas frame-draw code with requestAnimationFrame damping.
- **Layout & Section Spacer**: 80vh scroll spacer to provide timeline travel.
- **Color, Typography & Glass Tokens**: Matching the MotionSites design prompt.
- **Reveals & Stagger Animations**: IntersectionObserver thresholds with explicit CSS properties.
- **Browser Verification Checklist**: 6 real browser checks and 3 responsive viewport screenshots (desktop, tablet, mobile).

