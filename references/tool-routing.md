# Tool Routing And Motion Stack

Use this reference before choosing the renderer, animation library, AI video model, or editing tool. The goal is to keep knowledge explainers controlled, readable, and editable while borrowing the best parts of newer video skills.

## Default Decision

For Chinese PM, AI, SaaS, or methodology explainers, default to:

```text
facts/script -> TTS/timing -> storyboard -> Remotion components -> ffmpeg mix -> QA
```

Use generated images for style frames, texture plates, first-frame references, metaphor illustrations, and isolated decorative assets. Do not ask an image or video generator to carry Chinese titles, dense UI text, subtitles, citations, or final layout.

## Tool Matrix

| Tool or Skill | Best For | Use In This Skill As | Avoid When |
|---|---|---|---|
| Remotion | Deterministic React/TypeScript video, subtitles, charts, UI cards, timed scenes, product explainers | Default production renderer | The user needs a quick throwaway HTML-only prototype |
| HyperFrames | HTML/CSS/JS video composition, title cards, GSAP/Lottie/Three.js adapters, quick agent-authored video prototypes | Prototype renderer or alternate final renderer for HTML-native motion pieces | Long knowledge explainers with many Chinese text states unless QA budget covers it |
| GSAP | Premium DOM/SVG timeline craft: text splitting, stagger, path drawing, FLIP, MorphSVG, motion paths, easing studies | Motion reference and optional HTML prototype engine; port timings/easing back into Remotion when final render stays React | Simple fades or data-driven Remotion scenes where `interpolate()` is enough |
| CapCut / JianYing automation | Real footage editing, talking-head cleanup, subtitles, draft files a human editor can refine | Export or handoff target after automated cut planning, or for social post polishing | Core renderer for programmatic knowledge explainers with many stable UI layers |
| FFmpeg / Editly style editing | Deterministic trims, concatenation, audio mix, BGM ducking, overlays | Final assembly, media QA, or quick social variants | Complex component animation or text-heavy layouts |
| Sora / AI video generation | Short generated b-roll, cinematic inserts, concept shots when available | Optional asset generator only, never the source of truth | Any workflow requiring long-term API reliability, stable Chinese text, citations, or deterministic rerendering |

## Routing Rules

### Remotion First

Use Remotion when the video contains any of:

- Chinese titles, subtitles, callouts, citations, or UI labels.
- Ordered reasoning, comparison panels, charts, cards, timelines, or process diagrams.
- Need to rerender after script, TTS, BGM, or layout changes.
- QA requirements such as frame extraction, overlap checks, and deterministic fixes.

### HyperFrames When HTML Is The Product

Use HyperFrames-style composition when:

- The user explicitly asks for HTML/CSS/JS video synthesis.
- The piece is a title card, motion poster, launch bumper, kinetic typography study, or quick visual prototype.
- GSAP, Lottie, Three.js, shader, or browser-native effects are central to the style.

If HyperFrames is used for a final deliverable, still keep the same artifact chain: `facts.json`, `script.md`, `storyboard.json`, `assets/manifest.json`, rendered MP4, and QA report.

### GSAP As Motion Craft, Not A Replacement For Story

Borrow these GSAP patterns:

- Timeline labels for narration beats.
- `stagger` for card and chip entrances.
- SplitText-like title reveals, rebuilt with stable text components if needed.
- SVG path draw for reasoning flow lines.
- FLIP-style reordering for result cards and ranking changes.
- MotionPath for cursors, traces, and guided attention.
- MorphSVG or shape interpolation for abstract transitions.

When the final renderer is Remotion, translate GSAP references into frame-based timing: labels become frame ranges, eases become `Easing.bezier()`, and timeline states become component props.

### CapCut / JianYing As Editable Handoff

Use CapCut or JianYing automation when the input includes real footage, talking-head material, long videos, or the user wants a draft they can keep editing manually.

Good handoff targets:

- silence and filler removal
- duplicate take detection
- subtitle draft generation
- BGM and sound-effect rough placement
- social platform packaging
- editable draft JSON/project files

Do not rely on CapCut draft automation for fine-grained generated UI choreography. It is better as a finishing or human-review surface.

### AI Video Generation And Image2

Use image2 or AI video generation only for assets:

- opening style frame
- background plate
- decorative illustration
- object cutout
- short b-roll insert
- texture or material reference

For generated first frames, rebuild text and UI in the renderer. The first frame is visual direction, not the source file to animate as a poster.

## Research Notes

- HyperFrames presents itself as an HTML-to-video agent workflow with a router skill, core composition contract, GSAP/Lottie/Three.js adapters, captions, voiceovers, preview, and render loop.
- Remotion's official skill centers on React/TypeScript videos rendered to MP4, with guidance for `useCurrentFrame()`, `interpolate()`, scene sequencing, captions, audio, dynamic duration, Lottie/3D, and rendering.
- GreenSock's official `gsap-skills` package teaches agents GSAP core APIs, timelines, ScrollTrigger, plugins, React integration, performance, and framework-specific patterns.
- Current CapCut/JianYing agent projects mostly automate draft JSON, MCP/API editing, subtitles, and talking-head cleanup. Treat them as editing/handoff tools, not the knowledge-video source of truth.
- OpenAI's Sora 2 video generation models and Videos API are deprecated and scheduled for shutdown on 2026-09-24, so Sora-style skills should not be required for this pipeline.
