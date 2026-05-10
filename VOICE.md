# Voice

The thing that makes everything feel like Offshore — beyond the palette — is a small set of typographic and copy disciplines. They're the brand's signature.

## The italic-brass rule

The most important rule. **Italic Cormorant Garamond in `--brass` color, used as punctuation.**

It's how a headline gets its emphasis. It's how a stat block earns its texture. It's how copy lands without bolding or color stunts. It runs everywhere on offshore.co and any new project that uses this design system should run it the same way.

**The shape:**

```html
<em class="brass">word.</em>
```

The CSS rule (in `tokens/typography.css`) is:

```css
em.brass {
  font-style: italic;
  font-weight: 400;
  color: var(--brass);
}
```

That's it — no bold, no oversized treatment. The italic + brass combination IS the emphasis.

### When it works

- **Single short word** — usually a verb or noun:
  - "Wear where you're <em>from.</em>"
  - "Built to <em>swim in.</em>"
  - "Quietly <em>considered.</em>"
- **A unit on a number:**
  - "10<em>%</em>" / "$<em>312K</em>" / "<em>4</em>+"
- **A name on a list:**
  - "w/ <em>Friends of the Chicago River</em>"
  - "5% to <em>CRA Caribbean</em>"

### When it doesn't

- **Long phrases** — "We <em>partnered with the Coral Reef Alliance</em>" reads as shouty. Pick the load-bearing word: "We partnered with <em>Coral Reef Alliance</em>".
- **Adjectives stacked together** — "<em>quietly considered</em>" works; "<em>quietly, beautifully, responsibly considered</em>" does not.
- **Sentences** — never italicize a whole sentence in brass. The eye stops being able to read it.
- **More than once per headline** — pick one moment. Two italics in one line cancels the emphasis of both.

### Tone

The italic word is usually the one that makes the whole sentence land. Read the headline aloud: the word you'd lean on with your voice is the one to italicize.

## The split headline

The brand's primary headline shape:

```
[upright lead] [italic-brass middle] [optional upright tail]
```

Examples:
- "Wear where you're <em>from.</em>" — `lead: "Wear where you're"`, `italic: "from."`
- "Eight <em>cities</em> by 2027." — `lead: "Eight"`, `italic: "cities"`, `tail: "by 2027."`
- "A different partner for every <em>city.</em>" — `lead: "A different partner for every"`, `italic: "city."`

Stored in data as a three-key object: `{ lead, italic, tail }`. `tail` is optional; the italic word often takes the period.

## Copy patterns

A few recurring shapes that show up across the offshore site, worth keeping consistent in any new project:

### "Wear where you're from."

The Bayside campaign anchor. The pattern is: a small civic statement, treated as if it's obvious. Not a slogan — a worldview written in three words.

In new projects, find the one-sentence version of "what's true here" and treat it the same way. Not "innovative" or "premium" — something specific. "Built to swim in." "Quietly considered." "Four chapters, one reef."

### "X. Y."

Short, declarative, stacked. Used in lede paragraphs to set the rhythm. "Marine-bronze pilot cases. Hand-stitched flag straps. A capsule per city."

Each sentence is a single artifact named plainly. No adverbs. No "premium" or "luxury" or "crafted" — those words are dead.

### Numbers told plainly

Not "we've donated over $312,000" — "$312K, routed across the line, to date." Specific, precise, tactile. The italic-brass on the number gives it weight without bolding.

### Where the money goes

Cause callouts always answer: who, how much, since when, where to read the report. Don't use "give back" or "make an impact" — name the partner. "10% per sale to Friends of the Chicago River. Public reporting, December."

## What to avoid

These are the things that make a project stop feeling like Offshore:

- **Bold sans-serif headlines.** Use Cormorant Garamond for all editorial display. DM Sans only for functional text.
- **All-caps body copy.** Caps are reserved for eyebrows, microcaps, and small UI labels — never sentences.
- **Hex colors in markup.** Use tokens. If you need a color that isn't in the palette, propose adding it to `tokens/colors.css` first.
- **Drop shadows with hard edges.** Always use the `--shadow-card / --shadow-float` tokens. Custom shadows must use the same soft fall-off.
- **Gradients other than the hero `bone → paper → sand` warm wash.** Solid color regions are the default.
- **The word "premium" or "luxury".** Specific is more persuasive than aspirational.
- **More than one italic-brass per headline.** Pick the moment.
