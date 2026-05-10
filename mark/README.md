# Mark

The Offshore Co. mark and its lockups. The mark is the single most-deployed brand asset — it appears on every watch case, every box, every page, every garment. This document is the authoritative source for its construction, color variants, lockups, clear-space rules, minimum sizes, and what not to do.

## What's in here

```
mark/
  mark.svg                   canonical; stroke uses currentColor
  mark-navy.svg              baked navy (#1D2D44) for img / background-image / vendor delivery
  mark-brass.svg             baked brass (#A78546) for foil stamps and brass-on-navy lockups
  lockup-horizontal.svg      mark + wordmark side-by-side, the primary lockup
  README.md                  this file
```

The canonical source is `mark.svg`. The baked variants exist for contexts where `currentColor` isn't viable (img elements, CSS background-image, print delivery to vendors). The lockup is a reference file — see "Production protocol" for how it's actually delivered to vendors.

## Construction

The mark is built on a 512×512 grid (the `viewBox` in `mark.svg`). All geometry is referenced from the center point (256, 256).

| Element | Value | Notes |
|---|---|---|
| ViewBox | 512×512 | The mark's geometric universe. |
| Center | (256, 256) | All geometry pivots around this point. |
| Outer C — radius | 215.04 | Stroke center radius. Outer edge at 244.48, inner edge at 185.6. |
| Outer C — stroke | 58.88 | About 11.5% of viewBox. |
| Outer C — opening | 50° | Centered on the right (3 o'clock position). Arc start at (450.89, 346.88), end at (450.89, 165.12). |
| Inner o — radius | 92.16 | Stroke center radius. Outer edge at 116.48, inner edge at 67.84. |
| Inner o — stroke | 48.64 | About 9.5% of viewBox. |
| Gap (outer-inner) | 69.12 | Distance between outer C's inner edge and inner o's outer edge. About 13.5% of viewBox. |
| Inner o — closure | Complete circle | The inner o has no gap. Only the outer C is gapped. |

The geometry is intentionally specified — these are not approximations. Don't redraw the mark by eye; reproduce these values exactly if a new format is ever needed.

## Anatomy

The mark has two parts. Naming them helps every later conversation.

**The outer C.** A thick ring with a 50° opening on the right side. Reads simultaneously as:
- The O of *Offshore* (with the opening implying motion, currents, water passing through)
- The c of *Co.* in larger form
- The © glyph (literally a "Co." mark — visually rhyming with what Offshore IS)
- A porthole on a ship's hull
- The bezel of a dive watch

Four readings in one shape. The ambiguity is intentional.

**The inner o.** A smaller, fully closed ring at the center. Reads as:
- The o of *Co.*
- A dial face inside the bezel
- A smaller porthole nested inside the larger one
- A target or aperture

Together they encode "Offshore Co." in a single ownable shape that works at every size and on every surface.

## Color variants

The mark ships in three colors corresponding to brand-system tokens:

| File | Color | Use |
|---|---|---|
| `mark.svg` | `currentColor` | Canonical source. Inline web embedding where color follows the parent's CSS `color`. |
| `mark-navy.svg` | `#1D2D44` (`--navy`) | Default on bone, paper, sand, and other light surfaces. The everyday variant. |
| `mark-brass.svg` | `#A78546` (`--brass`) | Foil stamps on navy or kraft. Embroidery brass-thread on apparel. Featured / premium / cause-edition contexts. |

A bone variant (`#F0EBD8`) for inverse use (mark on navy without foil) is not shipped — see "Production protocol" below for how to produce it on demand. The same applies to any other on-palette color (`--brass-deep`, `--coral`, etc.) — produce as needed from the canonical source.

## Lockups

There is one canonical lockup:

**Horizontal lockup** (`lockup-horizontal.svg`): mark on the left, the wordmark `OFFSHORE CO.` in DM Sans 500 tracked uppercase to the right. The cap-height of the wordmark centers vertically on the mark. Spec:

| Element | Value |
|---|---|
| ViewBox | 1760×320 |
| Mark area | 256×256 at (32, 32) |
| Gap (mark right edge to wordmark first glyph) | 80 |
| Wordmark | DM Sans 500, font-size 140, letter-spacing 30 |
| Wordmark baseline | y = 210 (places cap-height center at y = 160, matching the mark's vertical center) |
| Both elements | `currentColor` |

Other lockups (stacked, mark-only, wordmark-only) are not formally specified yet. Mark-only is just `mark.svg`. Wordmark-only is the wordmark spec above, dropped into HTML/CSS with `font-family: var(--sans); font-weight: 500; letter-spacing: 0.22em;`. Don't invent new lockup compositions without checking back here.

## Clear space

**One inner-ring diameter** in every direction. The inner o has a diameter of about 184 in the source viewBox; on a rendered mark, use the rendered inner-ring diameter as the clear-space unit on all four sides.

Why the inner ring as the unit (instead of "half the mark height" or similar): the inner o is the smallest visually distinctive element. Tying clear space to the smallest distinctive element ensures the mark's *internal* legibility (the gap between the rings, the 50° opening) is matched by *external* breathing room. The mark earns its compactness by being honored when it appears.

Inside that clear-space zone: nothing. No text, no other elements, no edge of an image. The zone is invisible but absolute.

## Minimum size

| Medium | Minimum width | Notes |
|---|---|---|
| **Digital screen** | 24 px | Below this, the 50° gap and the inner-ring stroke can disappear at typical screen DPIs. |
| **Print — offset, screen** | 8 mm | Standard for thin-stroke marks. |
| **Print — foil stamp** | 12 mm | Foil registration at small sizes is unreliable; the inner ring can fill in. |
| **Embroidery** | 20 mm | Thread width and stitch density limit detail. The 50° gap may need to be enlarged at this size; let the embroiderer adjust. |
| **Watch case engraving (laser)** | 8 mm | Depends on the engraving house. |
| **Watch case engraving (CNC)** | 4 mm | Higher fidelity, but slower. |
| **Apparel screen-print at chest** | 60 mm | Recommended, not strict — at this size the mark reads clearly without dominating the garment. |
| **Apparel screen-print at hem detail** | 25 mm | Smallest size for screen-print where the gap stays legible. |

For embroidery at the minimum size, the embroiderer may need to redigitize the mark with a slightly wider gap and slightly thicker strokes; that's expected. Defer to the embroidery house.

## Production protocol

For print and merch production, vendors typically need a vector file in a specific spot color (not `currentColor`). The protocol:

1. Open `mark.svg` in Figma or Illustrator. This is the canonical source.
2. Replace `currentColor` with the spot color of the production (e.g., brass for foil, navy for inkjet print). Or open one of the pre-baked variants (`mark-navy.svg`, `mark-brass.svg`) directly.
3. Export as PDF (preserves vector) or SVG, depending on the vendor's preference.
4. **For foil stamps**: deliver the file as 1-color spot, not 4-color process. Foil is single-pull — no halftones, no opacity, no gradient. Specify the foil's Pantone code (or the vendor's house brass) in the order.
5. **For embroidery**: deliver `mark-brass.svg` at the production size, plus a sample rendering at the intended size. Most embroiderers will redigitize from the source — give them the SVG, not a rasterized version.
6. **For PDF business cards or letterhead**: export from Figma/Illustrator as PDF/X-1a if the vendor requires print-ready output.

The `mark-navy.svg` and `mark-brass.svg` files are pre-baked for the two most common production cases (default print, foil). The canonical remains `mark.svg`.

## Lockup production

The horizontal lockup includes a `<text>` element using DM Sans. For high-volume print delivery, the wordmark text **must be converted to outlined paths** before sending to vendors — production houses can't be relied on to have DM Sans installed.

The protocol:

1. Open `lockup-horizontal.svg` in Figma or Illustrator.
2. Select the `OFFSHORE CO.` text element.
3. Convert to outlines (Illustrator: *Type > Create Outlines*; Figma: *Outline Stroke* / *Flatten*).
4. Save as a new file (e.g., `lockup-horizontal-outlined.pdf`) — keep `lockup-horizontal.svg` as the editable source.
5. Send the outlined version to the vendor.

For web inline use, the lockup is typically composed in markup using inline `<svg>` for the mark plus an HTML element for the wordmark, styled via the design-system tokens. The SVG lockup file is for vendor delivery and design tool reference, not for runtime markup.

## Misuse — never do these

- Don't tilt, skew, rotate, or warp the mark.
- Don't apply gradients, shadows, glows, drop-shadows, bevels, embossing-as-CSS-effect, or any 3D treatment. (Physical emboss / deboss / foil are different — those are material treatments, not effects added to the digital file.)
- Don't recolor outside the navy / bone / brass / brass-deep / coral / coral-deep / navy-deep palette. The mark stays on-brand by staying on-palette.
- Don't crop the mark or partially obscure it. It earns its compactness; let it be whole.
- Don't combine the mark with another logo (co-brand) without a formal lockup spec — and there is no co-brand lockup spec yet, so don't.
- Don't add a tagline below the wordmark in the lockup. The tagline ("Made for the water" or whichever line is current) lives in headline copy, not as a permanent attachment to the mark.
- Don't stretch the lockup horizontally or vertically — DM Sans's tracking and the mark's geometry are already balanced in the lockup file. Scale uniformly.
- Don't break the mark into its parts (using just the outer C, or just the inner o, as an isolated graphic). They earn their meaning together.
- Don't render the mark in a different typeface's `C` and `o` (e.g., using Cormorant Garamond glyphs). The mark is geometric, not typographic.

## File formats

- `.svg` — primary delivery format. Open in any modern tool. The canonical (`mark.svg`) uses `currentColor`; the baked variants use hex.
- `.pdf` — produce on demand from the SVG for print vendors who require PDF.
- `.eps` — produce on demand for legacy print workflows. Rare; PDF has largely replaced EPS.
- `.png` — never use as the source of truth. Raster files are derivatives, not authoritative.

If a vendor asks for a "high-resolution PNG," send the SVG first with a note that any resolution can be rendered. If they insist on PNG, render at 4096×4096 from the SVG and deliver that; never go lower.

## Relationship to `icons/`

`icons/icon.svg` is the PWA / favicon source. It uses the same geometry as `mark/mark.svg` but with navy color baked in (since favicons can't dynamically pick up CSS variables). The two files serve different purposes:

- `icons/icon.svg` — runtime favicon, PNG variants in `icons/icon-{32,180,192,512}.png`.
- `mark/mark.svg` — design-system canonical, source for vendor delivery and inline web embedding with `currentColor` color control.

If the mark's geometry ever changes, both `mark/mark.svg` and `icons/icon.svg` need to be updated in lockstep. `icons/generate.py` regenerates the rasterized PNGs from `icons/icon.svg`.

## See also

- `VOICE.md` — when to use the mark alone, the lockup, or the wordmark
- `MATERIALS.md` — foils, threads, paper stocks, and other physical substrates for the mark
- `TOKENS.md` — the palette tokens the mark draws from
- `patterns/README.md` — pattern assets that frame the mark in deck and packaging contexts
