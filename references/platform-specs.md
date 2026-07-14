# Platform Specs

## Defaults

| Platform | Aspect | Resolution | Duration |
|---|---|---:|---:|
| Douyin | 9:16 | 1080x1920 | 30-90s |
| Xiaohongshu | 9:16 | 1080x1920 | 30-90s |
| WeChat Channels | 9:16 | 1080x1920 | 30-120s |
| YouTube Shorts | 9:16 | 1080x1920 | under 60s preferred |
| Bilibili | 16:9 | 1920x1080 or 3840x2160 | 2-10min |
| Product embed | 16:9 | 1920x1080 | 45-160s |

## Vertical Safe Area

For 1080x1920, use conservative defaults:

```json
{
  "top": 220,
  "bottom": 360,
  "left": 80,
  "right": 120
}
```

## Horizontal Safe Area

For 1920x1080:

```json
{
  "top": 60,
  "bottom": 80,
  "left": 90,
  "right": 90
}
```

## Platform Copy

| Platform | Publishing Copy |
|---|---|
| Xiaohongshu | short title, 5-10 tags, knowledge-sharing tone |
| Douyin | casual title, 3-8 tags, strong first 2 seconds |
| WeChat Channels | forwardable summary, practical takeaway |
| Bilibili | chapters, longer title, source links when useful |
| YouTube Shorts | concise title, description with source links |
