# Camera moves, image gate, and retakes

Read this before writing any video prompt. It exists because Flow's free tier is roughly two generations a day, so a wasted take costs a day, not a credit.

## Contents

1. The image suitability gate
2. The camera move library
3. Matching the move to the brief
4. Mobile variants
5. Retake diagnosis

---

## 1. The image suitability gate

Run this before writing the prompt. Two of these failing means the image will not parallax well and the user should hear it before they spend a generation.

| Check | Passes when | Fails when |
|---|---|---|
| Depth layers | Three or more distinct planes at different distances | Flat frontal shot, tight product on seamless, pure sky or texture |
| Edge separation | Subjects have clean silhouettes against what is behind them | Subject and background share tone, heavy haze, motion blur across the boundary |
| Occlusion room | Something is partially hidden that a camera move could reveal | Everything is fully visible from this angle already |
| Resolution | 1500px or wider on the long edge | Upscaled, soft, or heavily compressed source |
| Fragile subjects | None, or few and small in frame | Limbs mid-stride, hands, faces near camera, readable text, thin poles, wire, chain |

**What to say when it fails.** Name the specific failing check and what it will look like: a flat image produces a zoom that reads as a slow crop, not parallax. Then offer the cheaper fix, which is usually regenerating the source still with more depth in it rather than fighting it in the video stage.

**Fragile subjects are a warning, not a block.** They melt at high motion strength and hold at low. Tell the user which elements are at risk and to keep the motion slider low to mid.

---

## 2. The camera move library

Six moves cover almost everything. Each one is linear by construction, because scroll position is the timeline and any easing reads as the page stalling.

Pick one. Do not combine two into a single 8 second scroll, since a move that changes direction mid-scroll feels like a bug when the user controls it.

### Push
`one unbroken dolly forward, straight in, holding the horizon line steady`

Toward a single subject. The most reliable move and the one to choose when the image is borderline. Sells a product because attention narrows onto it.

### Drift
`one unbroken lateral track, right to left, parallel to the frame`

Across a scene with strong layer separation. Reveals depth better than any other move because the parallax is maximal perpendicular to the camera. Good for environments, bad for single subjects.

### Descend
`one unbroken move from a high wide framing down and forward toward [subject]`

Establishes then commits. Best when the wide shot is beautiful on its own and the subject deserves the arrival. Costs the most depth accuracy, so it needs a strong source image.

### Rise
`one unbroken move low near the ground, rising and pulling back to reveal the full scene`

The inverse. Ends wide, which suits a page that opens with a product and expands into context.

### Through
`one unbroken move forward and past [foreground element], continuing toward [subject behind it]`

Passes an object in the foreground. The single most convincing depth cue available, because the foreground element sweeps out of frame at a visibly different rate. Requires genuine occlusion in the source image, so check the gate first.

### Orbit
`one unbroken arc around [subject], holding it centered, revealing the far side`

Around a hero object. The most fragile move, since it demands geometry the model has to invent. Only for clean, well-lit, isolated subjects, and expect to burn a retake.

**The fixed scaffold** every move sits inside:

```
Animate this still image as a single continuous 3D parallax camera move.
The scene is frozen, nothing in the frame moves. Only the camera travels,
with true depth separation between [LAYERS, front to back].

Camera path: [MOVE LINE FROM THE LIBRARY]. The move never stops, never
speeds up, never slows down. Perfectly linear velocity from first frame
to last.

No cuts. No holds. No easing in or out. No zoom pops. No rack focus
changes mid-move.

Style: photoreal, 4K, [lighting and atmosphere read from the image].
[Lens], consistent depth of field throughout.

Motion: camera only. Do not animate [the moving-looking things in this
image]. No morphing or warping of [the fragile subjects]. Preserve
original geometry and color exactly.

Duration 8 seconds, [ASPECT].
```

---

## 3. Matching the move to the brief

The brief from step 1 decides this, not the image. Same photo, different site, different move.

| Site is for | Move | Why |
|---|---|---|
| A product, a car, a single object for sale | Push or Orbit | Attention narrows onto the thing being sold |
| A place, venue, property, restaurant | Drift or Through | Space is the product, so reveal space |
| A studio, agency, portfolio | Descend or Drift | Mood and range matter more than any one subject |
| A service or software | Push | The image is atmosphere, the copy does the work, so keep the move quiet |
| An event or launch | Rise | Ending wide leaves room for the date and the call to action |

When the brief and the image disagree, say so. A portrait-heavy image on a software site usually wants a different still, not a cleverer move.

---

## 4. Mobile variants

A 16:9 move cropped to a phone viewport loses the sides, which is where most parallax lives. The subject also drifts out of the safe area partway through the scroll.

Three options, cheapest first:

1. **Compose for center safety.** Write the move so the subject stays within the middle 60% of frame for the whole path. Costs nothing, works for Push and Rise, fails for Drift.
2. **Re-crop the frame sequence.** Extract a second set at 9:16 with a center-weighted crop: `-vf "fps=15,crop=ih*9/16:ih,scale=900:-2"`. Serve it under `/frames-mobile/` and pick by media query. One extra command, no extra generation.
3. **Generate a second take at 9:16.** Best result, costs a full generation. Only worth it when mobile is the primary surface and the move is Drift or Through.

Default to option 1 at the prompt stage, and mention option 2 so the user knows it exists before they spend a second generation on option 3.

---

## 5. Retake diagnosis

When a generation comes back wrong, change one thing. Changing three means not knowing which one worked.

| What went wrong | Change this |
|---|---|
| Limbs, hands, or thin structures warped | Lower motion strength first. If it persists, add the failing element by name to the do-not-animate list |
| Flat, reads as a slow crop | The image likely failed the depth gate. Name specific foreground and background layers in the prompt, or regenerate the still with more depth |
| Move eased or paused despite the prompt | Remove all direction words that imply gesture: "slowly", "gently", "gradually". They read as easing instructions |
| Background morphs or invents detail | Add `preserve background geometry exactly, no new elements` and shorten the duration to 6 seconds |
| Something in the scene animated on its own | The do-not-animate list missed it. Name it explicitly, including things that only look like they should move: dust, water, cloth, flame, hair |
| Text or a logo scrambled | Expected, no prompt fixes it. Keep the camera off it, or plan to patch it back in post |
| Move ended early or drifted off target | Name the end framing explicitly: "ending with [subject] filling the center third of frame" |
| Colors shifted from the source | Add `match the source image color grade exactly` and drop any style adjectives that imply a look |

**Budget rule.** On a two-generation daily allowance, spend the first take on the safest viable move rather than the most ambitious one. A working Push beats a melted Orbit, and the Push can ship today.
