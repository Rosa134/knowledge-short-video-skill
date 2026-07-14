# Image2 Asset Prompts

Use image generation to create controlled visual ingredients, not final text-heavy layouts. Chinese titles, UI labels, subtitles, charts, references, progress bars, and fine copy must be rebuilt in Remotion.

For premium explainers, image2/gpt-image-2 is expected to contribute real visual assets, not just an optional mood board. Use it to create background plates, first-frame direction, texture, isolated decorative or metaphor elements, device shells, icons, cursors, chapter inserts, and other static ingredients that raise production value. Remotion should then assemble, animate, and typeset those ingredients.

Do not deliver a polished run that uses only flat CSS cards unless the design quality still meets the accepted premium baseline.

When image2 outputs should become foreground elements rather than full plates, use `$image2-asset-pipeline` to clean alpha, remove baked white/checkerboard backgrounds, vectorize suitable elements, and record the processing method. A generated element with a visible rectangular canvas is not a finished layered asset.

## Asset Types

| Asset Type | Use | Must Avoid |
|---|---|---|
| `style_frame` | first-frame direction, mood, layout reference | small Chinese text, final subtitles, dense UI labels |
| `background_plate` | paper, grid, soft texture, subtle spatial depth | busy gradients, random symbols, high contrast behind text |
| `metaphor_illustration` | conceptual static frame or chapter opener | explaining the whole scene with generated Chinese copy |
| `isolated_element` | icon, object, character, sticker, cursor, device shell | shadows/crops that prevent clean layering, chroma colors close to foreground palette |
| `transition_plate` | short static texture used under wipes or section changes | replacing semantic animation |

## Minimum Asset Set For Premium Runs

Unless the user explicitly asks for code-only visuals, prepare at least:

- one `style_frame` or first-frame reference for the overall look,
- one or more `background_plate` images for paper/grid/texture/spatial depth,
- 3-8 `isolated_element` or `metaphor_illustration` assets for scene-specific polish,
- one `transition_plate` or decorative texture if the video has multiple chapters.

For RAG-style explainers, good image2 candidates include paper texture, abstract retrieval core surface, document card backing, cursor/citation marker, search light sweep, chapter divider, and subtle evidence-map decorations. Keep all Chinese copy and scores code-rendered.

## Prompt Contract

Every generated asset prompt should declare:

- aspect ratio and target use
- whether text is allowed; default is no text
- exact background expectation: transparent, pure white, or full-canvas plate
- visual style and palette tokens
- composition role in the Remotion scene
- negative constraints

For isolated elements, prefer true transparent output. If transparency is uncertain, request a flat chroma background over a checkerboard preview; checkerboards are pixels unless the file has real alpha.

Choose chroma color against the foreground palette:

- For teal/green/cyan product-design assets, prefer pure magenta `#ff00ff`.
- Use green `#00ff00` only when the object has no green, teal, cyan, green glow, or green shadow.
- If the element will be SVG-like or path-animated, prompt for flat vector-style, crisp edges, no shadows, no glow, no gradients, and no material texture.

## Default Prompt Blocks

### Style Frame

```text
Generate a 9:16 vertical style frame for a Chinese knowledge explainer video.
Subject: {topic}
Purpose: visual reference only, not final text layout.
Style: premium editorial tech explainer, clean white or very light background, structured whitespace, subtle grid, restrained teal/ink accents, crisp layered cards, soft paper-like depth, no stock-photo feeling.
Composition: {main visual metaphor or UI scene}. Leave clear safe areas for a large HTML-rendered Chinese title at top and subtitles at bottom.
Text policy: no readable text, no fake Chinese, no subtitles, no tiny UI copy.
Negative: no purple-blue gradient blob background, no random neon particles, no glassmorphism overload, no corporate stock illustration, no clutter, no watermark.
```

### Background Plate

```text
Generate a 9:16 background texture plate for a Remotion explainer scene.
White or near-white base, subtle paper grain, faint modular grid, minimal teal/gray technical marks, large quiet areas for animated UI components.
No readable text, no icons competing with foreground, no strong vignette, no dark corners, no colorful gradient blobs.
```

### Isolated Component

```text
Generate one isolated visual component for layering in Remotion.
Object: {object}
Style: clean editorial product-sketch or flat vector-style, restrained palette, crisp edges.
Canvas: transparent PNG preferred. If not supported, use pure chroma background selected against the object palette, centered, 12-20% padding, no text.
Negative: no labels, no background scene, no watermark, no cropped edges, no fake UI text, no checkerboard preview, no soft shadow touching the background, no chroma color inside the object.
```

### Ian Xiaohei Metaphor Illustration

Use the `ian-xiaohei-illustrations` skill when the scene needs a memorable conceptual static frame, chapter card, or metaphor insert. Adapt this structure:

```text
Generate one standalone 16:9 horizontal Chinese article illustration.
Pure white background. Minimalist black hand-drawn line art. Lots of empty white space. Sparse red/orange/blue handwritten Chinese annotations.
Recurring IP character: 小黑, a small solid-black absurd creature with white dot eyes and tiny thin legs, must perform the core conceptual action.
Theme: {scene topic}
Core idea: {one idea only}
Composition: {physical metaphor and 小黑 action}
Suggested elements: {3-5 elements}
Chinese handwritten labels: {0-5 short labels, optional; avoid exact subtitles}
Constraints: do not write a title, do not make a PPT infographic, do not create dense UI, do not include long Chinese text.
```

For vertical videos, use Xiaohei images as 16:9 inserts, cards, texture fragments, or chapter stills inside a Remotion layout. Do not stretch them into a full 9:16 poster unless the composition is intentionally designed around the insert.

## Asset Manifest

For every generated image, record in `assets/manifest.json`:

- id
- type
- prompt file or prompt text
- generation model/provider
- output path
- license/usage note
- scene ids
- whether it contains text
- whether it is a reference-only style frame

## Review Rules

- Reject generated images with fake Chinese, unreadable tiny text, watermarks, overly familiar stock metaphors, or cluttered "AI dashboard" visuals.
- Reject foreground element PNGs that still show a white rectangle, gray box, or checkerboard transparency preview after compositing.
- Reject generated cutout sources whose foreground palette is too close to the background/chroma color; regenerate with a different chroma or flatter style.
- Reject processed foreground assets when `$image2-asset-pipeline` reports non-empty `risk_notes`, unless the report explicitly documents a human-approved decorative-only use.
- Reject images that force the subtitle lane or main title into conflict.
- If image2 creates a good concept but bad text, keep the image only as a textless reference and rebuild the text in React.
- For first frames, compare the rendered Remotion first frame against the generated style frame. The final frame may borrow mood and composition but must have stable typography and controlled layers.
- Reject a "premium" render that ignores the generated asset plan and falls back to plain CSS boxes without an intentional art direction.
