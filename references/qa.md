# QA Checklist

Do not call a video complete until the strongest practical checks pass or the skipped checks are disclosed.

## Required Checks

- `brief.json` validates.
- `script.md` duration estimate is within target range.
- `facts.json` covers on-screen claims.
- Each scene has one dominant idea.
- `tts-manifest.json` has scene-split narration.
- `timing.json` comes from real audio or transcript timing.
- Captions do not overlap core content.
- Text stays inside safe area.
- Asset manifest records source and license.
- Generated images have declared roles and do not carry final Chinese text unless explicitly approved as a static insert.
- Foreground image2 elements have `$image2-asset-pipeline` reports when they are used as transparent PNGs, SVGs, or path-animated motifs.

## Media Checks

When MP4 exists:

```bash
ffprobe -hide_banner -show_streams -show_format final.mp4
```

Verify duration, resolution, video stream, audio stream when expected, and non-empty file size.

Preferred helper:

```bash
python scripts/media_qa.py final.mp4 --report qa/final.qa.json --contact-sheet qa/contact-sheet.jpg
```

The report must include stream info and audio level. A correct-duration audio track can still be silent, so check `mean_volume` rather than duration alone.

Flag these conditions:

- missing video stream
- missing audio stream when narration or BGM is expected
- mean volume below about `-60 dB`
- max volume at or above `0 dB`
- unexpected duration, resolution, or frame rate
- BGM loop clicks, seams, sudden restarts, or level jumps at loop boundaries
- accidental double music caused by adding BGM over an already mixed narration track

## Visual Checks

Inspect first frame, hook scene, middle explanatory scene, and final recap or CTA.

Look for blank render, cropped title, subtitle collision, unreadable text, too many simultaneous elements, irrelevant stock visuals, and any frame that feels visually cheaper than the accepted reference.

Premium QA is mandatory:

- Does the first frame feel art-directed within one second?
- Are typography scale, spacing, strokes, shadows, and textures consistent across scenes?
- Is there at least one signature motion or diagram moment that feels custom to this topic?
- Did any overlap fix reduce density, contrast, or rhythm without replacing it with a better composition?
- Would this pass as a polished product/team explainer rather than an AI-generated template?
- For premium runs, did image2/gpt-image-2 contribute real background, texture, first-frame, or isolated element assets, while Remotion still owns all semantic text and UI state?

Also look for AI-template taste problems:

- the whole video is one generated poster with pan/zoom,
- scenes repeat the same visual structure without a new metaphor or state,
- generic neon/glow/particle/dashboard decoration dominates the explanation,
- image-generated Chinese text replaces frontend-rendered typography,
- generated assets contain fake text, watermarks, or unusable cropped edges.
- foreground generated assets show residual checkerboard/white box/chroma rim, or were accepted despite non-empty `risk_notes` without a documented decorative-only rationale.

For image2 foreground assets, inspect:

- the light/dark QA composite from `$image2-asset-pipeline`,
- `foreground_background_overlap_ratio`,
- `risk_notes`,
- `chroma_soften_ratio` when chroma cleanup was used,
- whether rejected generated assets are marked as reference-only or rejected in `assets/manifest.json`.

## Baseline Regression Checks

When the user references an earlier version, screenshot, product-design style frame, or "this one is better" example, treat it as a baseline. The new render must be compared against it before delivery.

Compare:

- visual hierarchy: title scale, density, whitespace, card depth, and contrast
- semantic clarity: whether relationships between elements are easier to understand
- motion craft: whether elements change because the idea progresses, not because a template animates
- production polish: typography, shadows, line quality, spacing, transition rhythm, and caption treatment
- audio continuity: narration/BGM mix quality and loop-boundary behavior

A new version fails QA if it is merely safer but visually flatter than the accepted baseline. Fix the render or report the regression explicitly; do not call it an improvement just because overlap checks pass.

If the user says "high-end", "premium", "高级感", or points to a better-looking baseline, visual polish outranks optional feature additions. Prioritize improving design density, hierarchy, motion craft, and audio finish before adding new scenes or effects.

For every scene with a caption lane, inspect at least one target frame where:

- the subtitle is visible,
- the lowest main component is fully entered,
- animated cards, labels, callouts, or panels are at their densest state,
- progress and metadata strips are visible.

If a component was hidden or removed to fix overlap, verify the JSX/render tree or source markup no longer renders it. Do not accept CSS-only hiding without checking for conflicting declarations such as a later `display` rule.

## Checkpoint Checks

When a stage is skipped because it is cached:

- inspect `.ksv/checkpoint.json`,
- confirm the current input hash matches,
- confirm declared artifacts still exist,
- rerun final media QA even if render artifacts were reused.

## Report

`report.md` should include final output path, duration and format, TTS backend, facts coverage, assets used, checkpoint/cached stages, checks run, skipped checks, remaining risk, and edit map.
