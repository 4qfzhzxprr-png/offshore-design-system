"""Generate the Offshore Co. brand mark at every size we ship.

The mark is a "Co" monogram laid out as a roundel:

    * an OUTER thick navy ring forming the C (a near-full circle with a
      gap on the right-center),
    * a SMALLER navy ring forming the o (sitting inside the C, upper-right).

This file is the source-of-truth. Run it whenever the geometry changes:

    python icons/generate.py

It writes:
    icons/icon.svg               source-of-truth, used directly in manifest.webmanifest
    icons/icon-32.png            favicon size
    icons/icon-180.png           apple-touch-icon
    icons/icon-192.png           PWA manifest 192
    icons/icon-512.png           PWA manifest 512
    icons/icon-maskable-512.png  Android adaptive (10% safe-zone padding)
    favicon.ico (..)             16/32/48 bundle (in the parent dir)

Then run sync.py to push into the pipeline. Storefront is a fork — see README.
"""
from PIL import Image, ImageDraw
from pathlib import Path

NAVY = (29, 45, 68)            # --navy
HERE = Path(__file__).parent

# Geometry, parametrized by canvas size so a 512 render and a 32 render are
# proportionally identical. The percentages below were chosen by eye to
# match the supplied reference logo (a thick-stroked C-roundel with a small
# o nestled inside its upper-right interior).
OUTER_STROKE_PCT = 0.135       # outer C stroke width
OUTER_INSET_PCT = 0.10         # margin from canvas edge to outer C bbox
OUTER_GAP_DEG = 50             # opening on the right of the C (degrees)
INNER_R_PCT = 0.115            # inner o ring radius
INNER_STROKE_PCT = 0.075       # inner o stroke width
INNER_CX_PCT = 0.71            # inner o center, fraction of canvas width
INNER_CY_PCT = 0.34            # inner o center, fraction of canvas height


def render_icon(size: int, padding_ratio: float = 0.0) -> Image.Image:
    """Render the Co monogram at `size` pixels square. `padding_ratio` adds
    a uniform safe-zone for maskable icons (Android adaptive masks crop
    the outer ~10%)."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Apply mask padding by drawing into a smaller logical canvas, then
    # nothing else — Pillow's coordinates aren't transformed, so we just
    # offset+shrink the geometry.
    pad = int(size * padding_ratio)
    canvas = size - 2 * pad

    # ── Outer C ──────────────────────────────────────────────────────
    outer_inset = int(canvas * OUTER_INSET_PCT)
    outer_stroke = int(canvas * OUTER_STROKE_PCT)
    bbox = [
        pad + outer_inset,
        pad + outer_inset,
        pad + canvas - outer_inset,
        pad + canvas - outer_inset,
    ]
    # Pillow's arc(): 0° = 3 o'clock, sweeping clockwise. To leave a gap on
    # the right of width OUTER_GAP_DEG, draw from (gap/2)° clockwise around
    # to (360 - gap/2)°.
    half_gap = OUTER_GAP_DEG / 2
    draw.arc(bbox, start=half_gap, end=360 - half_gap,
             fill=NAVY, width=outer_stroke)

    # ── Inner o ──────────────────────────────────────────────────────
    inner_r = int(canvas * INNER_R_PCT)
    inner_stroke = int(canvas * INNER_STROKE_PCT)
    inner_cx = pad + int(canvas * INNER_CX_PCT)
    inner_cy = pad + int(canvas * INNER_CY_PCT)
    draw.ellipse(
        [inner_cx - inner_r, inner_cy - inner_r,
         inner_cx + inner_r, inner_cy + inner_r],
        outline=NAVY, width=inner_stroke,
    )

    return img


SVG_TEMPLATE = """\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <title>Offshore Co.</title>
  <!-- Outer C: thick navy ring with a {gap}° opening on the right. -->
  <circle cx="256" cy="256" r="{outer_r}"
          fill="none" stroke="#1D2D44" stroke-width="{outer_w}"
          stroke-dasharray="{dash} {gap_arc}"
          transform="rotate(-{rot} 256 256)"/>
  <!-- Inner o: small ring inside the C, upper-right. -->
  <circle cx="{inner_cx}" cy="{inner_cy}" r="{inner_r}"
          fill="none" stroke="#1D2D44" stroke-width="{inner_w}"/>
</svg>
"""


def render_svg() -> str:
    """SVG version of the same geometry. Uses stroke-dasharray to carve the
    gap out of an otherwise-full circle, which keeps the source compact and
    lets the SVG scale crisply at any size browsers will render it at."""
    canvas = 512
    outer_inset = canvas * OUTER_INSET_PCT
    outer_w = canvas * OUTER_STROKE_PCT
    outer_r = (canvas / 2) - outer_inset
    circumference = 2 * 3.141592653589793 * outer_r
    gap_arc = circumference * (OUTER_GAP_DEG / 360)
    dash = circumference - gap_arc
    # Rotate so the gap sits on the right (the dash starts at 3 o'clock by
    # default once we offset by half the gap).
    rot = 90 - OUTER_GAP_DEG / 2
    inner_r = canvas * INNER_R_PCT
    inner_w = canvas * INNER_STROKE_PCT
    inner_cx = canvas * INNER_CX_PCT
    inner_cy = canvas * INNER_CY_PCT
    return SVG_TEMPLATE.format(
        outer_r=round(outer_r, 1),
        outer_w=round(outer_w, 1),
        dash=round(dash, 1),
        gap_arc=round(gap_arc, 1),
        rot=round(rot, 1),
        gap=OUTER_GAP_DEG,
        inner_cx=round(inner_cx, 1),
        inner_cy=round(inner_cy, 1),
        inner_r=round(inner_r, 1),
        inner_w=round(inner_w, 1),
    )


def main() -> None:
    # SVG source-of-truth.
    (HERE / "icon.svg").write_text(render_svg(), encoding="utf-8")
    print("  wrote icon.svg")

    # Standard rasters.
    for size in (32, 180, 192, 512):
        out = HERE / f"icon-{size}.png"
        render_icon(size).save(out, "PNG", optimize=True)
        print(f"  wrote {out.name}")

    # Maskable variant for Android adaptive icons.
    render_icon(512, padding_ratio=0.10).save(
        HERE / "icon-maskable-512.png", "PNG", optimize=True
    )
    print("  wrote icon-maskable-512.png")

    # Favicon ICO bundling 16/32/48.
    favicon_dst = HERE.parent / "favicon.ico"
    render_icon(48).save(favicon_dst, format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
    print(f"  wrote ../{favicon_dst.name}")


if __name__ == "__main__":
    main()
