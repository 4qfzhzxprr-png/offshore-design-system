# Tokens

The atoms of the Offshore design system. Everything else is built from these.

## Palette

| Token | Hex | Use for |
|---|---|---|
| `--navy` | `#1D2D44` | Primary ink. Body text, headlines on light surfaces, primary buttons. |
| `--navy-deep` | `#0D1321` | Darkest navy. Reserved for deep sections (footer, dark hero). Stays the same hex in dark mode — its character is "deep" in both. |
| `--navy-rich` | `#3E5C76` | Intermediate navy. Hover states, compact UI accents on light surfaces. |
| `--sand` | `#E5DEC4` | Warmest cream. Tertiary background, image placeholder, frame liner. |
| `--bone` | `#F0EBD8` | Primary background. The default canvas color. |
| `--paper` | `#FAF7E8` | Lightest cream. Lifted surfaces — cards, inputs, panels. |
| `--brass` | `#748CAB` | The accent. Italic-brass display punctuation (`em.brass` in headlines), the brass dot in `.status` pills, focus rings. **The only color besides navy/cream that ever shows up at full saturation.** Sub-AA contrast on bone (~2.89:1) is an intentional brand exception for the headline signature — for small UI text use `--brass-deep`. |
| `--brass-deep` | `#455E92` | AA-compliant brass for small-UI text — `.eyebrow`, `.status.featured` text, `.btn.brass` background, "library" chips, status pills. ~5:1 on bone. **Dark mode redefines this to a LIGHTER blue (`#a3b5cc`)** so contrast holds against dark surfaces too. |
| `--brass-soft` | `rgba(116, 140, 171, 0.18)` | Brass tinted background — used on `.status.featured` pills. |
| `--terracotta` | `#c97650` | Warm cause-aligned accent. Used sparingly for visual signal — `.btn.danger` border, "removal" / "rejected" indicators, the Bleached Edition narrative. Use `--terracotta-deep` for any small text usage. |
| `--terracotta-deep` | `#99502E` | AA-compliant terracotta for `.btn.danger` text and inline warnings. ~5:1 on bone. **Dark mode redefines this to a LIGHTER warm (`#d68966`).** |

## Ink scale

The opacity ramp on `--navy` for light-mode text + borders. **Always use these tokens — never hardcode `rgba(29, 45, 68, ...)`.**

| Token | Opacity | Use for |
|---|---|---|
| `--ink` | 1.0 | Primary text. |
| `--ink-soft` | 0.72 | Secondary text. Lede paragraphs. |
| `--ink-faint` | 0.7 | Tertiary text. Caption text, table column headers, micro-caps labels. (Was 0.48 — bumped to clear WCAG AA 4.5:1 contrast.) |
| `--ink-quiet` | 0.28 | Active hover borders. Quiet UI accents. |
| `--ink-hairline` | 0.10 | Default 1px borders. Section dividers. |
| `--ink-whisper` | 0.05 | Hover background tints. The lightest stop. |

## Inverse ink scale

Same idea, flipped — opacity ramp on `--bone` for use on dark surfaces.

| Token | Opacity |
|---|---|
| `--bone-soft` | 0.78 |
| `--bone-faint` | 0.55 |
| `--bone-hairline` | 0.14 |

## Typography

| Token | Stack | Use |
|---|---|---|
| `--serif` | Fraunces → Iowan Old Style → Georgia | Editorial display. Headlines, statement quotes. |
| `--sans` | Inter → -apple-system → Segoe UI | Everything functional. Body, labels, button text. |
| `--mono` | Geist Mono → SF Mono → Menlo → Consolas | Slugs, IDs, technical readouts. |

| Token | Value | Use |
|---|---|---|
| `--display-track` | `-0.03em` | Negative tracking on large display serif. |
| `--caps-track` | `0.22em` | Uppercase eyebrows + microcaps. |
| `--caps-tight` | `0.14em` | Smaller uppercase UI (nav, status pills). |

## Shadows

All ambient — no harsh elevation.

| Token | Use |
|---|---|
| `--shadow-card` | Default card resting state. |
| `--shadow-card-hover` | Card on hover (paired with `translateY(-2px)`). |
| `--shadow-float` | Floating elements — nav pill, modals. |

In dark mode, all three are stronger (rgba(0,0,0,0.35) → 0.55) since the soft fall-off needs more contrast against dark surfaces.

## Radii

| Token | Value | Use |
|---|---|---|
| `--r-pill` | `999px` | Buttons, nav, tags, status pills. |
| `--r-card` | `18px` | Product cards, panels, primary surfaces. |
| `--r-card-inner` | `12px` | Inner radius nested inside `--r-card`. |
| `--r-frame` | `24px` | Outer hero/image frames (the doppelrand pattern). |
| `--r-frame-inner` | `16px` | Inner radius nested inside `--r-frame`. |

## Easing

**Always use one of these custom curves — never the weak built-ins (`ease`, `ease-out`).**

| Token | Curve | Use |
|---|---|---|
| `--ease-out-strong` | `cubic-bezier(0.23, 1, 0.32, 1)` | Default. Most UI motion. |
| `--ease-in-out-strong` | `cubic-bezier(0.77, 0, 0.175, 1)` | Major page transitions. |
| `--ease-drawer` | `cubic-bezier(0.32, 0.72, 0, 1)` | Slide-out panels, sheets. |
| `--ease-button` | `cubic-bezier(0.4, 0, 0.2, 1)` | Color transitions on hover. |

## Sections

| Class | Padding (vertical) |
|---|---|
| `.section` | 120px |
| `.section.compact` | 80px |
| `.section.tall` | 160px |

Horizontal padding adapts: 32px desktop, 16px mobile.

`.section-inner` caps width at 1240px.
