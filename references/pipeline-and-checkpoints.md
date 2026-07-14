# Pipeline And Checkpoints

Use this layer when a video task has expensive or iterative stages such as TTS, image generation, Remotion rendering, audio mixing, or QA reruns.

## Capability Stages

Model the workflow as capabilities instead of one large script:

| Stage | Inputs | Outputs | Regenerate When |
|---|---|---|---|
| `brief` | prompt, source files | `brief.json` | user goal, platform, audience, duration changes |
| `facts` | `brief.json`, source material | `facts.json` | source or claims change |
| `script` | `brief.json`, `facts.json` | `script.md` | facts, structure, tone, duration changes |
| `tts` | `script.md`, `tts-manifest.json` | audio files | narration text, voice, speed, backend changes |
| `timing` | audio files, transcript | `timing.json` | audio changes |
| `storyboard` | `script.md`, `timing.json`, `facts.json` | `storyboard.json` | scene order, duration, visual message changes |
| `assets` | `storyboard.json`, prompts, source media | `assets/manifest.json`, generated assets | visual direction or asset prompts change |
| `visual_render` | storyboard, Remotion code, assets | silent or muxed scene video | scene code, assets, layout, animation changes |
| `audio_mix` | narration, BGM, SFX, rendered video | mixed MP4 | BGM/SFX/voice levels change |
| `frame_qa` | final MP4, target frames | QA frames/contact sheet/report | render, subtitles, layout, or timing changes |
| `publish_render` | final render, QA report | platform deliverable | export settings change |

## Checkpoint Rules

- Create `.ksv/checkpoint.json` in each video project.
- Hash resolved stage inputs, not just stage names.
- Include script, storyboard, asset manifests, Remotion source files, audio manifests, and important environment/config values in the input list.
- Mark a stage complete only after its artifacts exist and the strongest practical verification for that stage has passed.
- Reuse a completed stage only when the input hash is identical.
- Do not skip QA just because render was cached; run quick media checks on the final file before delivery.

Use:

```bash
python scripts/stage_checkpoint.py status videos/video-id --stage tts --inputs script.md tts-manifest.json
python scripts/stage_checkpoint.py mark videos/video-id --stage tts --inputs script.md tts-manifest.json --artifacts audio/narration.m4a timing.json
```

## Stage Gates

Use these gates before advancing:

- `script`: duration estimate is within target and every on-screen claim maps to `facts.json`.
- `tts`: output audio exists, duration is plausible, and backend/voice are recorded.
- `storyboard`: every scene has one dominant idea and an explicit visual signature.
- `visual_render`: target frames show semantic changes and no text overlap.
- `audio_mix`: `volumedetect` mean volume is not silent and max volume is not clipping.
- `frame_qa`: inspect target frames where subtitles and densest components are visible together.

## ChatCut-Inspired Boundaries

Borrow from ChatCut-style pipelines:

- capability registry thinking
- resumable checkpoints
- explicit production-correctness rules
- media verification by evidence

Do not borrow talking-head assumptions blindly. Product methodology and AI explainer videos usually need Remotion component scenes, stable Chinese text, and scene-specific layouts more than raw footage cleanup.
