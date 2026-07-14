# Workflow

Use this pipeline for product methodology, AI concept, and product intro short videos.

## Artifact Chain

```text
brief.json -> facts.json -> script.md -> tts-manifest.json -> timing.json -> storyboard.json -> assets/image2-prompts.md -> assets/manifest.json -> render -> qa -> report.md
```

Do not skip `facts.json` for AI, technical, or source-sensitive videos. Do not lock scene durations before audio or transcript timing exists.

For iterative work, maintain `pipeline-manifest.json` and `.ksv/checkpoint.json`. Read `pipeline-and-checkpoints.md` before rerunning TTS, asset generation, or rendering.

## Modes

| Mode | Use When | Renderer |
|---|---|---|
| `remotion-template` | Default for polished PM, AI, and product explainers | Remotion |
| `html-prototype` | Fast visual prototype or animated HTML cards | HyperFrames-style HTML |
| `document-explainer` | Input is PDF, Markdown, URL, README, or article | Remotion after fact extraction |
| `quick-social` | Short platform variant from an existing script | Remotion or FFmpeg |

## Gates

### Brief Gate

`brief.json` must include `id`, `type`, `platform`, `language`, `duration_s`, `audience`, and `source`.

Run:

```bash
python scripts/validate_brief.py videos/video-id/brief.json
```

### Facts Gate

Every on-screen fact, number, date, tool name, model name, company claim, or framework attribution must reference `facts.json`.

### Script Gate

The script must be speakable:

- no throat-clearing intro
- short sentences
- deliberate pause points
- one main point per scene
- no dense list without a visual structure

### Timing Gate

Generate or import audio before final storyboard timing. `timing.json` is the master clock.

### Render Gate

Before rendering, confirm generated assets are role-separated:

- style frames and first frames are references or standalone stills,
- background plates contain no readable text,
- component images are isolated and layerable,
- Chinese text, UI, subtitles, charts, and citations are rendered in Remotion.

Before rendering, state renderer, aspect ratio, expected duration, TTS backend, subtitle method, output path, and skipped checks.

Check stage cache status for expensive upstream work:

```bash
python scripts/stage_checkpoint.py status videos/video-id --stage visual_render --inputs storyboard.json remotion assets/manifest.json
```

### Delivery Gate

Before saying the video is done, write `report.md` and run QA from `qa.md`. Use `scripts/media_qa.py` for rendered MP4s when practical:

```bash
python scripts/media_qa.py videos/video-id/renders/final.mp4 --report videos/video-id/qa/final.qa.json --contact-sheet videos/video-id/qa/contact-sheet.jpg
```

## Resume Rules

| Changed | Regenerate |
|---|---|
| `brief.json` | everything downstream |
| `facts.json` | script, TTS, storyboard, render |
| `script.md` | TTS, timing, storyboard, render |
| `tts-manifest.json` | audio, timing, storyboard, render |
| `storyboard.json` | assets, render |
| `assets/image2-prompts.md` | generated visual assets, render |
| Remotion component only | render and QA |
| BGM only | audio mix and QA |

When a stage is reused from cache, still verify its declared artifacts exist before depending on it.
