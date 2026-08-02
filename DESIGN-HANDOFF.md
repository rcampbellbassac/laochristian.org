# Design hand-off: laochristian.org → lao-christian-app

**Update before reading further**: when I first drafted this doc, I assumed
`lao-christian-app` hadn't started its own design work yet and wrote it as a
from-scratch port. Checking that repo directly before finalizing, that's
wrong — a parallel Codex/Claude session has already independently rebuilt
large parts of the app's visual system (palette tokens, home hero art,
collection icons, legal-page illustrations), including hitting and fixing
the *exact same* temple-roofline pitfall documented in §3 below
(`217e2b6 Replace temple-like hero building with rural chapel`). So this is
no longer "here's what to port" — it's "here's the reference spec, here's
what's already aligned, and here's the handful of concrete drifts worth a
quick explicit sync." Reflects what's actually live on `www.laochristian.org`
today as of this writing.

Style name: **"Quiet Lao Modernism"** — restrained editorial layout, generous
negative space, layered-paper/gouache illustration, a small fixed palette,
Lao and English typography given equal weight.

## Already aligned — verified, no action needed

Checked `lao-christian-app/src/assets/main.css` directly against this repo's
`docs/assets/stylesheets/extra.css`:

- **Palette tokens match exactly**: `--lc-paper`, `--lc-ink`, `--lc-brand`,
  `--lc-sage`, `--lc-river`, `--lc-gold`, `--lc-clay`, `--lc-dark-bg`,
  `--lc-dark-paper` are the identical hex values in both projects.
- **Dark-mode accent swap** is implemented in both: gold becomes the
  "active/accent" color in dark mode where teal was the accent in light mode
  (see the app's `.dark .lc-nav-link--active { background: var(--lc-gold);
  color: #102b34; }`).
- The app has already moved off the old teal/sky-blue (`#0f766e`/`#0369a1`)
  palette and the fog/autumn stock-photo backgrounds — both superseded.
- The app already regenerated its home hero and collection icons as
  illustrated art in this style (`Replace home hero with responsive Lao
  landscape artwork`, `Replace collection icons with cohesive Lao artwork`,
  `Modernize legal page illustrations`).

## Worth an explicit sync — small drifts found

1. **Paper-grain texture differs in three ways**, unclear if intentional:

   | | laochristian.org | lao-christian-app |
   |---|---|---|
   | technique | procedural SVG `feTurbulence` (`docs/assets/img/paper-grain.svg`, ~300 bytes) | same idea — app also has its own `paper-grain.svg` |
   | blend mode | `overlay` | `multiply` |
   | opacity | `0.09` sitewide, `0.14` on cards | `0.055` |
   | plus | — | app *also* layers a photographic `page-texture-{light,dark}.webp` underneath, which this repo doesn't have |

   Not necessarily a bug — just flagging that "the same texture system"
   isn't quite pixel-identical between the two, and the app's approach
   (grain + photo texture combined) is materially different from this repo's
   (grain only). Worth a quick conversation about which is preferred, or
   whether both are intentionally different for good reasons (e.g. the app's
   longer reading sessions might want more texture, or less).

2. **Lao font default doesn't match, and neither is a final decision**:
   this repo defaults to `noto-sans-lao-looped`; the app's
   `DEFAULT_LAO_FONT_ID` is `noto-sans-lao`. Neither reflects an actual
   decision from the Lao review team — see §2a for the full context. Once
   they pick one, update both.

3. **This repo has no image-generation script or prompt history to compare
   against for the app's newer art** (`home-hero-*-v2.webp`, the collection
   icons, the legal-page illustrations) — I can't verify those against the
   avoid-list in §3 the way I can for laochristian.org's own art, since I
   don't know how they were generated. Worth a quick look together if you
   want the two art libraries to share a single documented prompt style,
   the way laochristian.org's `assets-src/prompts/` does.

## 1. Color tokens (reference — already matches, see above)

```css
/* Light */
--lc-paper:      #f6f1e7;  /* rice-paper background */
--lc-ink:        #173b38;  /* deep Mekong green — primary text/ink */
--lc-brand:      #2e675e;  /* forest teal — primary brand/links/buttons */
--lc-sage:       #789b83;  /* muted sage — secondary accent */
--lc-river:      #88a7b0;  /* dusty blue — tertiary accent */
--lc-gold:       #e5b957;  /* champa gold — highlight only, never a fill */
--lc-clay:       #b86f50;  /* soft clay — earth accent */

/* Dark */
--lc-dark-bg:    #102b34;  /* deep night blue — page background */
--lc-dark-paper: #172f35;  /* blue charcoal — card/surface background */
```

**Balance target from the original brief:** ~60% paper/neutral, 25%
green/teal, 10% sage/blue, 5% gold/clay. Gold is a moment of light (chips,
active states, one accent line), never a background fill or dominant color.

## 2. Typography

| Role | Font stack | Notes |
|---|---|---|
| English body/UI | `"Noto Sans", sans-serif` | |
| Lao body/UI | `"Noto Sans Lao Looped", sans-serif` (this repo) / `"Noto Sans Lao Variable"` (app) | see §2a — no final pick yet, and the two projects currently disagree |
| English headings | `"Noto Serif", serif` | |
| Lao headings | `"Noto Serif Lao", serif` | mixed in the same heading as English is fine — this repo's homepage sets `"Noto Serif", "Noto Serif Lao", serif` as one stack; the app does the same for `.app-section-title` |

Weight: prefer 600/700 over heavy 800 for Lao headings — the brief notes Lao
type reads more elegant at moderate weight.

Type scale (in **absolute px**, not rem):

```
hero heading:    clamp(38px, 30px + 2.8vw, 72px)
section heading: clamp(32px, 28px + 1.2vw, 42px)
card heading:    clamp(21px, 19px + 0.4vw, 26px)
Lao body:        19px, line-height 1.7
English body:    16px
interface text:  clamp(16px, 15px + 0.3vw, 18px)
```

⚠️ **Gotcha we hit**: if your base font-size isn't exactly 16px (Material for
MkDocs' root is 20px), `rem`-based clamps silently overshoot these targets.
Use `px` in the clamp min/max, or verify your root font-size first.

### 2a. Lao font picker — still an open decision on both sides

Both projects offer the same 8 Lao font presets (Noto Sans Lao, Noto Sans
Lao Looped, Noto Serif Lao, Phetsarath, plus self-hosted Saysettha,
SengBuhan, Saysettha Mai, SengPathom — all SIL OFL). laochristian.org built a
site-wide preview picker (header dropdown, `docs/assets/javascripts/lao-font-picker.js`,
plus the `/_style-guide/` page) specifically so the Lao review team could
compare candidates live. **No final choice has been recorded on either
project** — see the drift noted above. Once the team decides, update both
defaults together, and the laochristian.org preview picker can then be
removed (it was a review tool, not meant to ship long-term).

## 3. Imagery style — the avoid-list that actually mattered

All art on laochristian.org was generated via `scripts/generate_image.py`
(OpenAI `gpt-image-2`, `1792x1024`, quality `high`) using a shared style
preamble (`assets-src/prompts/_style-preamble.md`). Every prompt is saved
(`assets-src/prompts/lc-NN-*.txt`) for reproducibility.

**Every piece of art has a light and dark variant**, swapped via a
`data-md-color-scheme` (or equivalent) attribute selector — never one image
reused across both modes.

**Allowed motifs** (max 2–3 per image): limestone karst mountains, a
river/water ribbon, rice-terrace contours, dok champa flowers, khaen-reed
vertical rhythms, mist/dawn/twilight light.

**Hard avoid-list** — confirmed to matter in practice, independently, on
both projects:
- Temples, stupas, monks, Buddha imagery, the Lao national flag, elephants/
  tourism imagery, oversized crosses, "glowing supernatural" effects.
- **Upturned/curved temple-style roof finials ("chofah")** — the image model
  defaults toward these on *any* Lao pavilion/gate/structure unless
  explicitly told not to. This repo hit it on the Events page art
  (`assets-src/prompts/lc-05-events.md` has the incident notes); the app
  independently hit the same thing on its home hero
  (`217e2b6 Replace temple-like hero building with rural chapel`). If either
  project generates new art with any building/structure in it, include an
  explicit exclusion for this — it's not a one-off fluke, it's a reliable
  model default worth guarding against every time.
- The official Adventist symbol (see §5) is never drawn, redrawn, or
  approximated by the image model.

**Composition convention**: subject positioned in the lower-left third,
generous sky/negative-space in the upper area, mountains/river filling the
right two-thirds. This isn't cosmetic — it's why the full-bleed hero pattern
in §4 works without cropping the subject.

## 4. Full-bleed hero pattern

Every content page on laochristian.org uses this technique for its hero
image:

```css
.hero {
  width: 100%;
  aspect-ratio: 1792 / 1024;  /* matches the source art's native ratio */
  max-height: 70vh;
  overflow: hidden;
}
.hero img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
}
```

**Why `aspect-ratio` and not a fixed height**: a fixed
`clamp(220px, 30vw, 420px)` height was tried first and forced a crop box
that didn't match the art's proportions — since compositions deliberately
put the subject low in the frame (§3), that crop cut off the actual subject.
Matching the container to the source image's real aspect ratio fixed it
completely.

**No fade-to-background gradient** on the bottom edge of plain content-page
heroes — just a 1px border. A fade was tried and rejected for obscuring
otherwise-fully-visible art.

**If hero art sits behind text** (like this repo's homepage hero — unlike
the plain content-page heroes above, which never have text over them): use
a soft *directional* scrim — a linear gradient from the paper/ink color at
the text edge fading to fully transparent by ~55% width — as the first
(topmost) `background-image` layer, photo as the second layer. Only the
portion behind the text column is scrimmed; the rest of the artwork stays
fully visible. This was a real bug shipped and then fixed here — the
original homepage hero had no scrim, and text legibility depended entirely
on where it landed on a brightness-varying image.

## 5. Official Adventist symbol — handle with care

Downloaded from the North American Division's official brand guidelines
(`https://www.nadadventist.org/about/brand-guidelines/logo/`), used
completely unmodified. Full usage rules and provenance:
`assets-src/vendor/README.md` in this repo.

Key rule, straight from NAD's own guidelines, not a style preference:
**never redraw, recolor, restyle, or combine it with our own logo/identity.**
If the app needs to show Adventist affiliation anywhere, copy
`docs/assets/img/adventist-symbol.svg` as-is.

## 6. Components

**Cards**: 15px border-radius, 1px border at 12% ink opacity, minimal
shadow, lifts 2px on hover, paper-grain texture overlay (see the drift note
above re: exact opacity/blend-mode differences).

**Buttons**: pill-shaped (`border-radius: 999px`), 600 weight, 17px, two
variants — primary (solid brand-teal in light mode / solid gold in dark
mode) and secondary (outline only).

**Small icons**: hand-drawn flat SVGs (not photographic/generated) in the
same restrained paper-cut style, used at small sizes next to list items and
contact info. See `overrides/home.html` and `docs/about.md` for example
markup.

**Footer divider pattern**: see §7 below — worth reading even though it's
framed as a bug-fix story, because the lesson generalizes.

## 7. Footer divider — a cautionary tale worth repeating here

This repo's footer originally used a large painted (AI-generated) wavy-line
image as a **full-bleed background behind all footer text**. That was
legitimately broken: the lines were bold/saturated enough that wherever text
landed on top of them, contrast became unreliable — a gold line ran directly
through a sentence and made it hard to read.

**Fix, worth copying as a general pattern**: decorative line/wave motifs
belong in their **own thin strip, never behind body text**. Rebuilt as
`docs/assets/img/footer-ribbon.svg` — a small (200×120 viewBox) **exact-period
sine-wave tile** built from sampled trigonometry (not a bezier
approximation), so the left/right edges match pixel-for-pixel and it tiles
via `background-repeat: repeat-x` with zero visible seam at any width. An
AI-repainted "textured" version of this same tile was tried first — a
pixel-diff check showed the image-edit model doesn't preserve edge-to-edge
continuity precisely enough for seamless tiling, so that version was
discarded for the plain vector tile instead. If the app wants a similar
accent anywhere, this SVG is directly reusable, or regenerate using the same
method (`assets-src/prompts/lc-19-footer-lines.md` has it written up in
full) rather than asking an image model for a seamless raster tile.

## Reference

- Live site: https://www.laochristian.org/
- Design tokens: `docs/assets/stylesheets/extra.css` in this repo — single
  source of truth; this doc summarizes it, but the CSS is authoritative if
  they ever diverge
- Image generation script + all prompts: `scripts/generate_image.py`,
  `assets-src/prompts/`
- Style/component preview page: `/_style-guide/` on the live site (not in
  nav, but publicly reachable) — palette swatches, type scale, card
  component, Adventist-symbol usage note, and the Lao font bake-off tool
