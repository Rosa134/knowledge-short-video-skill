# Motion Craft

Use motion to create visible reasoning progress, not decoration. A knowledge short video should feel like a small animated system being assembled in front of the viewer.

## Borrowable Open-Source Patterns

- Remotion remains the default renderer for Chinese explainers because React components keep text, UI, charts, captions, and timing editable.
- Use Remotion template ideas such as character text reveal, SVG line draw, progress steps, counters, chart reveal, lower thirds, push/iris/clock wipes, subtle grain, and controlled transitions as component patterns.
- Borrow product-demo craft from cinematic Remotion templates: scene-relative camera, geometry-aware cursor, prop-driven component layout, audio ducking, and UI states from JSON.
- Borrow GSAP craft for timing ideas: labeled timelines, staggered entrances, path drawing, FLIP-style reordering, MorphSVG-like shape transitions, motion-path cursors, and premium easing. If the final renderer is Remotion, port the timing into frame ranges and `Easing.bezier()` instead of adding GSAP just for simple fades.
- Borrow HyperFrames craft when the piece benefits from HTML-native composition, GSAP/Lottie/Three.js adapters, or quick title-card prototyping, but keep Chinese text-heavy final explainers in deterministic components unless the user explicitly chooses HyperFrames.
- Use CapCut/JianYing automation for real footage, talking-head cleanup, subtitles, and editable draft handoff. Do not make it the primary engine for generated UI choreography.
- Borrow agentic-video QA patterns from projects such as video-use, Kinocut, and OpenMontage: plan first, render receipts, ffprobe checks, representative frame extraction, and self-review before delivery.
- Borrow storyboard discipline from AI-video storyboard tools: shared visual theme, shot purpose, camera or motion language, audio direction, and post-production checklist.

Do not import a large external framework just because it exists. Copy small MIT-compatible component ideas only after checking license fit, or reimplement the pattern locally.

## Timeline Density

At every 2-3 seconds of a 9:16 knowledge video, one semantic element should change:

- title word or emphasis appears
- one card enters, is selected, or leaves
- a path segment draws
- a node lights up
- result order changes
- answer text generates
- citation/source chip appears
- warning or limitation is revealed
- recap item locks into place

If the only change is global pan, zoom, drift, or floating motion, the scene fails.

## Entrances And Exits

- Animate 2-3 properties together: opacity plus y/scale, path length plus glow, card y plus shadow, counter value plus accent.
- Stagger related items by 3-8 frames so they feel choreographed rather than dumped on screen.
- Exits should exist when the next idea needs space; use faster exits than entrances.
- Use springs or bezier easing with clamped interpolation. Avoid linear motion except for intentionally mechanical scan lines or progress bars.

## Scene Camera

Use camera movement only to guide attention inside a built scene:

- slow push when a system core becomes important
- quick push or snap when selecting a result
- slight focus shift between card groups
- no whole-poster pan/zoom as the main animation

Still images can receive mild Ken Burns treatment only when they are B-roll or texture plates, never as a substitute for component animation.

## Audio And Motion Sync

- Align major reveals to narration pause points, beat hits, or subtitle chunks.
- Use BGM as a restrained bed; duck under narration.
- Use short UI sounds or soft whooshes only for meaningful state changes.
- Avoid constant whoosh/sparkle sound design; it makes the video feel template-generated.

## Premium Feel Rules

- Premium quality has priority over merely passing layout safety. A safe but stiff render should be revised before delivery.
- Fewer bigger decisions beat many small generic effects.
- Prefer structured whitespace, strong type hierarchy, and consistent tokens over glow-heavy "tech" decoration.
- Keep color accents deliberate. Avoid default blue-purple gradients, random neon particles, glassmorphism everywhere, fake holograms, and stock SaaS blobs.
- Make every decorative layer earn its place: grain, paper texture, grid, or light sweep must support the scene mood and remain behind content.
- Do not let safety checks degrade the design into a low-density whiteboard. Empty space is good only when it increases focus; if it removes hierarchy, visual tension, or semantic relationships, the scene is under-designed.
- If a previous version has stronger composition, use it as a quality floor. Rebuild with safer layout and cleaner motion, but preserve or improve its density, rhythm, and component relationships.
- Prefer one strong diagram per scene over several weak placeholders. Line geometry, spacing, shadows, and card scale should look intentionally designed at full resolution, not just non-overlapping.
- Use advanced motion sparingly but decisively: staggered card choreography, path drawing, FLIP-like reordering, masked text reveals, material shadow changes, and focus transitions should map to meaning rather than decoration.
