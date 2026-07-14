# TTS and Captions

Audio is the master clock. Generate or import narration before locking scene timing.

## Backend Priority

| Backend | Use When |
|---|---|
| Edge TTS | MVP, free Chinese or English drafts |
| Volcengine Doubao | polished Chinese voice when configured |
| Qwen TTS | local or controlled workflow when available |
| ElevenLabs | English or premium marketing voice |
| User audio | highest authenticity; requires transcript timing |

## TTS Manifest

Use scene-split audio:

```json
{
  "language": "zh-CN",
  "backend": "edge",
  "scenes": [
    {
      "id": "s01-hook",
      "speaker": "narrator",
      "text": "MVP 不是低配版产品。",
      "subtitle": "MVP 不是低配版产品。",
      "output": "audio/s01-hook.wav"
    }
  ]
}
```

## Caption Rules

- Captions show spoken words.
- Body text shows key phrases, not full caption sentences.
- Caption lane must be dedicated.
- Split subtitles by phrase, not arbitrary character count alone.
- If word-level timestamps exist, use them for karaoke or highlighted captions.

## Reused Audio Rules

Before reusing any old audio file, classify it as one of:

- `narration_only`: voice track only, safe to mix with BGM.
- `bgm_only`: music bed only, safe to mix under narration.
- `mixed_master`: already contains narration plus BGM or sound design.
- `unknown`: must be inspected before mixing.

Do not layer BGM onto `mixed_master` or `unknown` audio. If the user says "reuse TTS and BGM", locate the actual voice-only and music-only assets. If only a prior MP4 or mixed `.m4a` exists, either extract the mixed master as the final audio or regenerate/export a clean narration track before adding BGM.

## BGM Loop Rules

- Do not loop a short BGM preview with a raw Remotion `Loop` unless the file is known to be seamless.
- If BGM is shorter than the video, create a full-length music bed with FFmpeg `aloop` plus `acrossfade`, or generate/export a BGM file at final duration.
- Inspect loop boundaries, especially around `bgm_duration`, `2 * bgm_duration`, and the final fade-out. For a 20s BGM in a 48s video, explicitly check around 19-22s and 39-42s.
- Duck BGM under narration and fade out the final 1-2 seconds. A good media QA report must include both global volume and any known loop-boundary checks.

## Pacing

- Chinese draft: 250-280 Han characters per minute.
- Dense Chinese technical content: 220-250 Han characters per minute.
- English draft: 140-160 words per minute.
- Dense English technical content: 120-145 words per minute.
