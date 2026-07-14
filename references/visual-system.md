# Visual System

Default visual language: clear, modern, information-first, restrained motion.

## Layout Primitives

- Title area
- Main content area
- Caption lane
- Metadata strip
- Progress or chapter indicator

## Components

- `TitleCard`
- `ComparePanel`
- `FrameworkSteps`
- `FlowDiagram`
- `Timeline`
- `MetricTree`
- `QuoteCard`
- `CodeOrPromptBlock`
- `CaptionLane`
- `RecapCard`

## Visual Asset Roles

- `style_frame`: generated or designed reference for mood and composition; not the final rendered scene unless explicitly a standalone still.
- `background_plate`: fixed paper, grid, texture, or spatial plate behind all semantic content.
- `component_asset`: isolated generated object, icon, cursor, character, document, device shell, or decoration layered in Remotion.
- `semantic_component`: title, card, UI copy, chart, line, node, citation, subtitle, or progress element rendered in HTML/React/SVG.

`semantic_component` should almost always be code-rendered, not image-rendered.

## Layered Animation Rules

- Do not use a single generated poster as the whole video with only pan, zoom, or floating motion.
- Treat generated style frames as visual reference only unless the frame is explicitly a standalone title/still frame.
- Use image generation for background texture, first-frame direction, icons, decorative motifs, illustration fragments, and other static components.
- Render Chinese titles, UI cards, flow lines, subtitles, scores, references, and progress indicators with HTML/React/Remotion components so text stays stable and editable.
- Build explainer scenes as layers: fixed background, animated title, cards, SVG path drawing, stateful diagram core, result/result-order changes, generated answer panel, independent subtitle lane, and progress.
- Bind every meaningful component to the timeline. At 2-3 second frame checks, at least one semantic element should have changed: new card, highlighted node, drawn path, sorted result, generated text, citation, warning, or recap item.
- Do not reuse the same main visual system for every chapter. A mechanism chapter may show the full pipeline, but hook, analogy, use case, limitation, and takeaway chapters need distinct visual metaphors or information structures.
- During storyboard review, add a `scene_visual_signature` for each scene. Adjacent scenes fail QA if their main components, layout, and semantic objects are materially the same.
- For generated first frames, separate the reference image from the final Remotion frame. The rendered first frame should match the mood, spacing, and hierarchy, but use stable frontend text and timeline-ready layers.

## Hierarchy

Each scene can contain one `primary` message, up to two `secondary` supports, small labels or icons as `support`, and decorative elements only when they do not compete with meaning.

## Text Rules

- Chinese subtitles: prefer no more than 18 Han characters per line.
- English subtitles: prefer no more than 42 characters per line.
- Caption lane should not exceed 2 lines.
- If a caption or label needs to shrink below readability, split the scene.
- Do not show the full narration sentence as both body text and subtitle.
- Do not place chart labels, icon labels, callouts, or decorative annotations in the same reserved area as explanatory copy. If both are needed, use separate rows or hide the secondary label.
- For every representative frame, inspect text boxes against diagrams, card content, subtitles, and progress bars. Any text crossing another semantic element is a QA failure.

## Subtitle Safe Area

- Treat subtitles, progress bars, and metadata as a global reserved layer, not as decoration added after the scene is built.
- Keep main scene components out of the subtitle lane even when the subtitle lane is empty at the start of a scene.
- Leave visible whitespace between the lowest semantic scene component and the caption lane; avoid "just touching" layouts.
- If a component should not appear in the final video, remove it from the React/Remotion render tree. Do not rely only on `display: none`, opacity, or off-screen CSS.
- Check CSS conflicts when hiding or moving components. A later declaration such as `display: grid` after `display: none` means the component is still rendered.
- Inspect the frame where late-entering components are fully visible while subtitles are active. Contact sheets can miss the exact collision moment.

## Motion Rules

- Use motion to reveal structure or guide attention.
- Prefer simple position, opacity, scale, and line-draw animations.
- Avoid visual noise in knowledge videos.
- Use transitions at thought boundaries, not mid-sentence.
- Use staggered entrances, path drawing, state changes, result sorting, answer typing, and citation reveals as primary motion. Do not rely on global poster pan, zoom, drift, or floating as the scene's main animation.
- Inspect whether each scene has a real semantic change every 2-3 seconds. Repeated idle breathing is not enough.

## Anti-AI Taste Rules

- Avoid generic AI-dashboard cliches: glowing brain, random circuit sphere, neon particles, fake hologram panels, blue-purple gradient blobs, and unreadable pseudo-code.
- Avoid "template professionalism": every scene using the same card stack, the same floating motion, the same underline, or the same icon row.
- Use fewer, stronger visual metaphors. A clean document card selected by a search core is better than ten unrelated tech icons.
- Let whitespace, typography scale, timing, and evidence structure create the premium feel before adding decorative effects.
