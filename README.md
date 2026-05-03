# Offshore Design System

The design system for Offshore Co. and adjacent projects. Plain CSS files plus a small JS module — no build step, no package, no framework lock-in.

## What's in here

```
tokens/
  colors.css         palette + ink scale + shadows
  dark.css           dark-mode token overrides
  typography.css     font families, tracking, em.brass rule
  spacing.css        sections, radii, easing, basic reset

components/
  buttons.css        .btn pill + .btn.brass / .ghost / .danger utility
  forms.css          .edit-form pattern, variant rows, group sections
  tables.css         .panel data tables, sticky thead, expand rows
  cards.css          .card, .bento-card, doppelrand frame
  headlines.css      .display-headline split-pattern (lead + italic + tail)
  status-pills.css   .status.featured / .upcoming / .live
  stat-blocks.css    numerical readouts with italic-brass texture
  modals.css         .modal-scrim + .modal shell
  empty-loader.css   .empty / .loader / .skeleton
  nav.css            .nav-pill floating glass nav

js/
  theme.js           light/dark toggle, no-flash, auto-injecting

preview/
  index.html         every component on one page — open this first

VOICE.md             italic-brass discipline, headline shape, copy rules
TOKENS.md            palette + ink + shadows + radii reference
README.md            this file
```

## Quickest possible setup

Drop the `tokens/`, `components/`, and `js/` folders into a static directory in your project. In your HTML `<head>`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Theme toggle — load synchronously to avoid flash -->
  <script src="/path/to/js/theme.js"></script>

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,300;1,9..144,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">

  <!-- Tokens (always load all three) -->
  <link rel="stylesheet" href="/path/to/tokens/colors.css">
  <link rel="stylesheet" href="/path/to/tokens/typography.css">
  <link rel="stylesheet" href="/path/to/tokens/spacing.css">

  <!-- Components — pick the ones you need -->
  <link rel="stylesheet" href="/path/to/components/buttons.css">
  <link rel="stylesheet" href="/path/to/components/forms.css">
  <link rel="stylesheet" href="/path/to/components/tables.css">
  <!-- ...etc -->
</head>
```

You don't need to load `tokens/dark.css` separately — `theme.js` injects the same overrides at runtime. Load it only if you want dark-mode support without the JS (e.g. server-rendered with `<html data-theme="dark">`).

## Open the preview first

Before writing a single line of CSS in your new project, open `preview/index.html` in a browser. Click the theme toggle in the top-right and watch every component flip from light to dark. That's the entire surface area of the system on one page — way faster than reading code.

## What's intentionally not here

- **No build step.** Plain CSS, plain JS, no SCSS, no PostCSS, no Tailwind. Open the files in any editor, they look like CSS, they ARE CSS.
- **No NPM package.** Copy-paste or git submodule. Two consumers don't need a package registry.
- **No React/Vue/Solid components.** The system is at the markup + CSS level. Wrap pieces in whatever UI framework your project uses.
- **No icons.** Bring your own. Nav and button icons in offshore are inline SVG — see `js/theme.js` for the sun/moon SVG strings as a reference.

## Brand voice

Read `VOICE.md`. Specifically the italic-brass rule. **It's the single most important thing in this repo** — copy the components verbatim and ignore VOICE.md, and you'll have a project that LOOKS like Offshore but doesn't feel like it.

## Versioning

This is v0. Conventions:

- Token names (`--navy`, `--bone`, `--brass`) are stable. They will not be renamed.
- Component class names (`.btn`, `.edit-form`, `.panel > table`) are stable.
- New tokens / classes can be added at any time.
- Breaking changes require a major bump and migration notes in this README.

## Where this came from

Built originally for [offshore-revamp](../offshore-revamp/) — a small-batch watch + apparel ecommerce site. The design system was extracted to its own repo so adjacent projects (an internal watch design tool, future capsules, future ventures) could share the same visual language without fork-drifting.

## Consumers

- `offshore-revamp/` — the customer-facing ecommerce site + admin portal. Currently uses inline CSS that mirrors these tokens; migration to consume this system directly is a future cleanup, not a blocker.
- `offshore-watch-design/` — internal watch design tool. Uses this system from day one.
