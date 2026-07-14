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

## Pacing

- Chinese draft: 250-280 Han characters per minute.
- Dense Chinese technical content: 220-250 Han characters per minute.
- English draft: 140-160 words per minute.
- Dense English technical content: 120-145 words per minute.
