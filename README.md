# Knowledge Short Video Skill

Create Chinese or bilingual knowledge short videos and explainer videos for product management methods, AI concepts, SaaS product introductions, technical education, and structured thought leadership.

This skill is designed for a script-first, fact-checked, Remotion-first production workflow:

- normalize a video brief
- build grounded facts
- write spoken scripts
- produce TTS and timing
- create storyboards
- plan image2 assets as style frames, background plates, components, or inserts
- render with Remotion
- run media QA and representative frame checks

## Contents

- [`SKILL.md`](SKILL.md): main skill contract and workflow
- [`references/`](references): visual system, motion craft, QA, platform specs, AI/PM content patterns
- [`scripts/`](scripts): project initialization, duration estimation, checkpointing, media QA, brief validation
- [`assets/schemas/`](assets/schemas): project artifact schemas

## Quick Start

```bash
python scripts/init_video_project.py --id rag-demo --root videos --type ai_intro --platform xiaohongshu --language zh-CN --topic "RAG 不是万能知识库"
python scripts/validate_brief.py videos/rag-demo/brief.json
```

Before rendering a video, read:

- [`references/workflow.md`](references/workflow.md)
- [`references/visual-system.md`](references/visual-system.md)
- [`references/motion-craft.md`](references/motion-craft.md)
- [`references/image2-asset-prompts.md`](references/image2-asset-prompts.md)
- [`references/qa.md`](references/qa.md)

## Design Principle

Use image generation for style frames and visual ingredients. Keep Chinese titles, UI labels, subtitles, diagrams, scores, citations, and progress indicators in Remotion/React so the video remains stable, editable, and frame-checkable.
