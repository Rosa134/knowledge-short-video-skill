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

## Visual Checks

Inspect first frame, hook scene, middle explanatory scene, and final recap or CTA.

Look for blank render, cropped title, subtitle collision, unreadable text, too many simultaneous elements, and irrelevant stock visuals.

Also look for AI-template taste problems:

- the whole video is one generated poster with pan/zoom,
- scenes repeat the same visual structure without a new metaphor or state,
- generic neon/glow/particle/dashboard decoration dominates the explanation,
- image-generated Chinese text replaces frontend-rendered typography,
- generated assets contain fake text, watermarks, or unusable cropped edges.

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
