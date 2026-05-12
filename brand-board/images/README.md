# Brand book photography

Photographs that overlay the colored fallback treatment in `brand-board.html`. Until you drop the corresponding `.jpg` files into this directory, each photo slot in the brand book renders as a tinted block with a small caption inside a dashed outline — the book remains presentable from day one and gets progressively more complete as images land.

## Required images

The brand book references these exact filenames. When present, they render; when absent, the CSS fallback shows. No JavaScript or build step required.

### Chapter I — Offshore Co.

```
07-materials-hero-aluminum-bronze.jpg  Spread 07 hero · 3:2 landscape
07-materials-sailcloth.jpg             Spread 07 satellite · 16:10
07-materials-sapphire.jpg              Spread 07 satellite · 16:10
07-materials-kraft.jpg                 Spread 07 satellite · 16:10
07-materials-cotton.jpg                Spread 07 satellite · 16:10
08-applications-dial.jpg               Spread 08 hero · 4:3 landscape
08-applications-hangtag.jpg            Spread 08 satellite · 16:10
08-applications-card.jpg               Spread 08 satellite · 16:10
08-applications-screen.jpg             Spread 08 satellite · 16:10
```

### Chapter II — Offshore Performance

```
12-materials-titanium.jpg              Spread 12 material · 16:10 · Grade 5 titanium macro
12-materials-vectran.jpg               Spread 12 material · 16:10 · Vectran weave
12-materials-sapphire.jpg              Spread 12 material · 16:10 · 4mm sapphire edge
12-materials-cordura.jpg               Spread 12 material · 16:10 · Cordura ripstop
15-saturation-ref-ps01.jpg             Spread 15 hero · 4:3 landscape · Saturation watch 3/4 view
```

Note: Chapter I and Chapter II both reference a `sapphire` material. They're separate files (`07-materials-sapphire.jpg` and `12-materials-sapphire.jpg`) because they're different shots — Chapter I shows a slimmer 2.5mm AR-coated crystal in soft workshop light, Chapter II shows a thicker 4mm dive-rated crystal with edge profile in studio clarity.

## Optional supporting photography

The brand book works without these. They'd add atmosphere to Spreads 01, 04, and 06 if you want it — but the HTML doesn't currently reference any of these three filenames, so adding them requires a small HTML edit.

```
01-cover-atmospheric.jpg               Spread 01 cover · 16:9
04-typography-letterpress.jpg          Spread 04 typography detail · 3:4
06-pattern-deboss.jpg                  Spread 06 pattern detail · 16:10
```

## How to generate

See the brand-book project's image-generation files:

- `OFFSHORE_NANO_BANANA_PROMPTS.md` — human-readable prompts (Chapter I)
- `generate_brand_images.py` — one-command batch generator (Chapter I)
- `offshore_brand_images.json` — machine-readable config (Chapter I)

The Chapter II prompts will be delivered separately when ready. They follow the same master-style anchor but with a colder photographic register (underwater natural light, instrument clarity, deep navy/black backgrounds, steel as accent rather than brass).

## Image specifications

- **Format**: JPEG, quality 90+ (or PNG if you need transparency, but JPEG recommended for photographs)
- **Resolution**: minimum 1600px on the long edge
- **Color profile**: sRGB
- **Aspect ratios**: as noted above. CSS `background-size: cover` will crop to fit, but matching avoids excessive cropping.

## Replacement workflow

1. Lay all variants of a single shot side by side. Pick the strongest.
2. Rename from `<stem>_v#.jpg` to `<stem>.jpg`. Drop into this directory.
3. Refresh `brand-board.html` in the browser. The photo slot for that image now shows the photograph instead of the colored fallback.
4. Repeat for the other 13 required shots.

No cache to bust, no rebuild step.
