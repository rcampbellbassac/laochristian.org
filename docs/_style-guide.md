# Design tokens — review page

Not linked in navigation. Internal reference for reviewing the palette/type/component
tokens in `docs/assets/stylesheets/extra.css` before they're applied to real pages.

## Type

# Hero heading (H1) — ລາວຄຣິສຕຽນ LaoChristian.org
## Section heading (H2) — Scripture, worship, and Christian resources
### Card heading (H3) — Read the Lao Bible

Body copy in English at 16–18px. Lorem ipsum is banned everywhere else in this repo,
but here it's just measuring line length and font rendering: the quick brown fox jumps
over the lazy dog.

ຂໍ້ຄວາມພາສາລາວ (Lao body text) ໃຊ້ Noto Sans Lao Looped ທີ່ 18–20px ແລະໄລຍະຫ່າງແຖວກວ້າງກວ່າ
ເພື່ອໃຫ້ອ່ານງ່າຍ.

## Lao font bake-off

Use the "文A" picker in the header to preview each candidate Lao font (all 8 offered by
the lao-christian-app project) against the same sample text — headings and body both
switch together so it's a fair side-by-side look. Spelling here intentionally keeps the
traditional ຣ (R) in sacred terms rather than the modern government-simplified spelling
— see `docs/_lao-style-guide.md`.

# ພຣະເຈົ້າ ແລະ ພຣະເຢຊູຄຣິດ

ພຣະເຈົ້າຊົງຮັກໂລກຫຼາຍ ຈົນໄດ້ຊົງໂຜດປະທານພຣະບຸດອົງດຽວຂອງພຣະອົງ ເພື່ອທຸກຄົນທີ່ວາງໃຈໃນພຣະບຸດນັ້ນ
ຈະບໍ່ພິນາດ ແຕ່ມີຊີວິດນິລັນດອນ. ຂໍ້ຄວາມນີ້ໃຊ້ສະລະ, ພະຍັນຊະນະ, ວັນນະຍຸດ ແລະຕົວເລກ (໑໒໓) ທີ່
ຫຼາກຫຼາຍ ເພື່ອທົດສອບການສະແດງຜົນຂອງແຕ່ລະຟອນ.

## Color swatches

<div class="lc-card" style="background:var(--lc-paper); color:var(--lc-ink);">rice-paper #F6F1E7 / ink #173B38</div>
<div class="lc-card" style="background:var(--lc-brand); color:var(--lc-paper); margin-top:.5rem;">forest teal #2E675E (primary brand)</div>
<div class="lc-card" style="background:var(--lc-sage); color:var(--lc-ink); margin-top:.5rem;">muted sage #789B83</div>
<div class="lc-card" style="background:var(--lc-river); color:var(--lc-ink); margin-top:.5rem;">dusty river blue #88A7B0</div>
<div class="lc-card" style="background:var(--lc-gold); color:var(--lc-ink); margin-top:.5rem;">champa gold #E5B957 (accent only)</div>
<div class="lc-card" style="background:var(--lc-clay); color:var(--lc-paper); margin-top:.5rem;">soft clay #B86F50</div>
<div class="lc-card" style="background:var(--lc-dark-bg); color:var(--lc-paper); margin-top:.5rem;">dark mode bg #102B34</div>
<div class="lc-card" style="background:var(--lc-dark-paper); color:var(--lc-paper); margin-top:.5rem;">dark mode surface #172F35</div>

## Components

<div class="lc-card" style="max-width:22rem;" markdown="1">
### Read the Lao Bible
Card component — 15px radius, 1px border, minimal shadow, lifts slightly on hover.

<span class="lc-chip-gold">New</span>
</div>

<div class="lc-adventist-slot" style="color:var(--lc-ink); border-color:color-mix(in srgb, var(--lc-ink), transparent 55%); max-width:22rem; margin-top:1rem;">
Reserved — official Adventist symbol placed here later, unmodified
</div>

Toggle light/dark mode (top right) and switch language (🌐 icon) to check both variants.
