# Patterns

Brand pattern assets. Currently one canonical pattern with more to follow.

## What's in here

```
patterns/
  depth-contours.svg   the brand's primary pattern — concentric arcs
                       suggesting bathymetric depth, anchored bottom-center
  README.md            this file
```

## depth-contours.svg

Seven concentric arcs, opening upward from a bottom-center origin. Reads as: depth contours on a chart, sonar / radar pulse, and tide-swell horizon all at once. The geometric ambiguity is intentional — all three readings are on-brand for an ocean watch.

### Where to use it

- **Hero backdrops** (dark navy) — brass arcs on `--navy-deep`. Hero or section-break.
- **Packaging interiors** — brass-foil-stamped on kraft / sand. Watch box liner, gift sleeve, cause-report sleeve.
- **Paperwork footers** — navy hairlines on bone. Letterhead bottom, invoice footer.
- **Empty states** (internal tools) — `--brass-deep` on paper, centered, half-size. "No data yet" / "no orders found." Pattern softens the empty UI without filling it with copy.
- **Apparel detail** — single-color foil or screen on garment back / hem detail.

### How to use it

The SVG's stroke is `currentColor`, so its color follows the parent's CSS `color` value. Three integration styles, in order of flexibility:

**1. Inline SVG** (recommended for web — full color control)

Copy the SVG markup directly into your HTML. Wrap in `.pattern-depth` and pick a surface modifier:

```html
<div class="pattern-depth on-navy" aria-hidden="true">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 200" ...>
    <!-- contents of patterns/depth-contours.svg -->
  </svg>
</div>
```

The wrapper's CSS (in `components/pattern.css`) sets `color: var(--brass)` for `.on-navy` and `color: var(--brass-deep)` for `.on-bone` / `.on-paper`. Override `color` on the wrapper if you want a different stroke color.

For decorative use (most cases), add `aria-hidden="true"` on the wrapper so screen readers skip the pattern entirely. For standalone use (e.g. as the centerpiece of an empty state), omit `aria-hidden` so the SVG's `<title>` ("Offshore Co. — depth contours") is announced.

**2. `<img>` element** (simple, color-fixed)

```html
<img src="/path/to/patterns/depth-contours.svg" alt="" role="presentation">
```

The stroke renders in whatever `currentColor` resolves to in the image's isolated context — which is the document's text color. To use a fixed color, generate a color-baked variant (see below).

**3. CSS `background-image`** (decorative tile, color-fixed)

```css
.hero { background-image: url('/path/to/patterns/depth-contours.svg'); }
```

Same color limitation as `<img>`. Use a baked variant for predictable color.

### Baked color variants

If you need the pattern in `<img>` or `background-image` form with a fixed color, generate a color-baked SVG by replacing every `currentColor` with the hex you want. Two variants are commonly useful:

- `depth-contours-brass.svg` — stroke `#A78546`
- `depth-contours-navy.svg` — stroke `#1D2D44`

Not yet generated — produce on demand. Keep the canonical `depth-contours.svg` with `currentColor` as the source of truth; baked variants are derivatives.

### Print and merchandise

The SVG scales cleanly to any size; open in Figma / Illustrator and export as PDF / EPS / PNG at the resolution needed.

For foil-stamp packaging: treat the opacity ramp as the visual outcome, not as ink-density variation. The stamp itself is a single solid color of brass foil — the perceived depth-fade comes from the seven-arc count and progression, not from variable foil pressure (which is unreliable on most stamping presses).

For apparel screen-print at small sizes: the innermost arc (radius 20 / opacity 0.12) can be dropped without changing the read. The 6-arc variant registers more cleanly at hem-detail scale.

For paperwork (letterhead, invoice): the navy-on-bone treatment works at the page footer. Width spans the full content area; height clamps to 40–80px.

### Variants to add later

- **swell.svg** — horizontal sine-wave-like lines, tileable, for footer dividers and section breaks where the bottom-anchored composition doesn't fit.
- **chart-grid.svg** — subtle longitude / latitude grid for paperwork backgrounds and internal-tool table empty states.
- **compass-rose.svg** — single-point mark for letterhead and business-card backs. Pairs with the wordmark.

Each is additive — none touches `depth-contours.svg` or `pattern.css`.

### Geometry notes

For anyone tuning the pattern:

- viewBox is `0 0 400 200` (2:1 landscape). All arcs anchor at y=200 (bottom edge).
- Arc radii progress arithmetically: 200, 170, 140, 110, 80, 50, 20 (step = 30).
- Opacity progresses roughly exponentially: 0.78, 0.64, 0.52, 0.40, 0.30, 0.20, 0.12.
- `preserveAspectRatio="xMidYMax slice"` keeps the surface line glued to the bottom and the focal point on the horizontal center, clipping outermost arcs when the container is wider than 2:1.
- `stroke-linecap="round"` softens the arc terminals where they meet the surface line.
