---
name: knowledge-short-video
description: Create Chinese or bilingual knowledge short videos and explainer videos for product management methods, AI concepts, SaaS product introductions, technical education, and structured thought leadership. Use when turning a topic, document, URL, README, article, outline, or script into a narrated short video with fact-checked script, storyboard, TTS, subtitles, assets, Remotion rendering, and platform-specific outputs for Bilibili, Xiaohongshu, Douyin, WeChat Channels, YouTube Shorts, or Reels.
metadata:
  version: "0.1.0"
  userInvocable: true
---

# Knowledge Short Video

Create knowledge-first short videos for product methodology and AI concept explanation. Optimize for correctness, structure, subtitle readability, and reusable production artifacts, not generic faceless content.

## Core Contract

- Treat every factual claim as grounded content. Anything shown on screen must trace to `facts.json` or be explicitly marked as opinion.
- Build the script before visuals, but generate or import TTS before locking final scene timing.
- Use one dominant idea per scene. Split scenes instead of shrinking text or stacking concepts.
- Reserve a subtitle lane and keep all core content inside platform safe areas.
- Record asset source and license in `assets/manifest.json`; do not silently use unlicensed media.
- Use image generation as a style-frame and asset generator, not as the uncontrolled renderer for Chinese text, UI, charts, subtitles, or final explainers.
- Finish with QA: brief validation, duration estimate, checkpoint-aware stage review, `ffprobe` when a video exists, subtitle/content overlap check, target-frame inspection at caption-active moments, and representative frame inspection.

## Use Cases

| Type | Examples | Default Shape |
|---|---|---|
| PM methodology | MVP, PRD, user stories, prioritization, funnel, north star metric | Hook, context, framework, example, pitfall, recap |
| AI explainer | RAG, Agent, MCP, context engineering, evaluation, multimodal | Hook, mental model, mechanism, use cases, limitations, takeaway |
| Product intro | SaaS, internal tools, open-source projects, AI workflows | Problem, product idea, workflow, proof, CTA |

## Workflow

### 1. Normalize the brief

Create a project folder with:

```bash
python scripts/init_video_project.py --id video-id --root videos --type ai_intro --platform xiaohongshu --language zh-CN
```

If the user gives a loose topic, write `videos/video-id/brief.json` and validate it:

```bash
python scripts/validate_brief.py videos/video-id/brief.json
```

Read `references/workflow.md` for the full artifact chain.
For iterative or expensive runs, read `references/pipeline-and-checkpoints.md` and use `scripts/stage_checkpoint.py` to decide which stages can be reused.

### 2. Build facts

For topic, URL, document, or README inputs, create `facts.json` before writing final script. For AI or current technical topics, use primary sources where practical. For PM methodology, separate common practice, source-backed claims, and author opinion.

Read `references/content-patterns.md` and the relevant domain reference:

- PM topics: `references/pm-methodology-patterns.md`
- AI topics: `references/ai-explainer-patterns.md`

### 3. Write script

Write `script.md` in spoken Chinese or bilingual prose. Avoid throat-clearing intros. Check duration:

```bash
python scripts/estimate_script_duration.py videos/video-id/script.md --language zh-CN
```

Use the estimate to revise before generating TTS.

### 4. Produce TTS and timing

Create `tts-manifest.json` with scene-split narration. Do not create one giant monologue unless the user supplies a single recorded narration.

Preferred backend order:

1. Edge TTS for free MVP runs.
2. Volcengine Doubao or other Chinese TTS for polished Chinese output.
3. Qwen TTS when local or configured runtime exists.
4. ElevenLabs for English or premium marketing voice.
5. User audio with transcript when human narration is available.

Read `references/tts-and-captions.md`.

### 5. Storyboard

Create `storyboard.json` using actual audio duration from `timing.json`. Every scene needs:

- id, start, duration
- beat
- narration or audio ref
- subtitle
- primary message
- visual type
- fact refs
- transition

Read `references/visual-system.md`, `references/motion-craft.md`, and `references/image2-asset-prompts.md` before creating Remotion scenes or generated asset prompts.

### 6. Plan and generate visual assets

Create `assets/image2-prompts.md` before generating images. Separate:

- style frames or first frames
- background texture plates
- isolated decorative elements
- metaphor illustrations
- UI/icon components that will be redrawn or layered in Remotion

When using the Ian Xiaohei illustration style, use it for conceptual static frames or texture-like metaphor illustrations, then rebuild titles, UI copy, captions, and progress with HTML/React components.

### 7. Render

Default renderer is Remotion. Use programmatic diagrams, cards, timelines, comparison panels, and caption lanes before stock B-roll. For quick HTML/GSAP experiments, HyperFrames-style composition is acceptable only when the user asks for faster prototype work.

Platform specs live in `references/platform-specs.md`.

Before an expensive render, check whether upstream stage inputs changed. Do not rerun TTS, asset generation, or full Remotion rendering when the checkpoint says the stage is cached and the artifacts still exist.

### 8. Verify and report

Run `scripts/validate_brief.py`, duration checks, stage checkpoint review, and media QA. When a final MP4 exists, run `scripts/media_qa.py` or equivalent `ffprobe`/`ffmpeg` checks, then inspect representative frames. Write `report.md` with:

- output files
- duration and format
- facts coverage
- known risks
- edit map for future changes

Read `references/qa.md`.

## Output Layout

```text
videos/video-id/
  brief.json
  facts.json
  script.md
  storyboard.json
  tts-manifest.json
  timing.json
  assets/image2-prompts.md
  assets/manifest.json
  pipeline-manifest.json
  .ksv/checkpoint.json
  remotion/
  qa/
  renders/
  report.md
```

## Required References

| Reference | When to read |
|---|---|
| `references/workflow.md` | Always before running the full pipeline |
| `references/content-patterns.md` | Before script and fact shaping |
| `references/pm-methodology-patterns.md` | PM methodology videos |
| `references/ai-explainer-patterns.md` | AI concept videos |
| `references/visual-system.md` | Before storyboard and Remotion layout |
| `references/motion-craft.md` | Before building Remotion animation, transitions, and frame-change density |
| `references/image2-asset-prompts.md` | Before creating image2 prompts, style frames, static frames, or generated visual components |
| `references/pipeline-and-checkpoints.md` | Before iterative runs, rerenders, TTS, asset generation, or render caching |
| `references/platform-specs.md` | Before selecting aspect ratio and safe areas |
| `references/tts-and-captions.md` | Before TTS, subtitles, or timing |
| `references/qa.md` | Before calling a video done |
