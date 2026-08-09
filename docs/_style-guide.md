# ໂທເຄັນອອກແບບ — ໜ້າທົບທວນຄືນ

ບໍ່ໄດ້ເຊື່ອມໂຍງໃນການນຳທາງ. ເອກະສານອ້າງອີງພາຍໃນສຳລັບການທົບທວນໂທເຄັນ palette/type/component ໃນ `docs/assets/stylesheets/extra.css` ກ່ອນທີ່ພວກມັນຈະຖືກນຳໃຊ້ກັບໜ້າເວັບຕົວຈິງ.

## ປະເພດ

# ຫົວບົດວິລະຊົນ (H1) — ລາວ​ເປັນ​ກຸ່ມ LaoChristian.org
## ຫົວຂໍ້ພາກ (H2) — ພຣະຄໍາພີ, ການໄຫວ້, ແລະຊັບພະຍາກອນຂອງຄຣິສຕຽນ
### ຫົວຂໍ້ບັດ (H3) — ອ່ານພະຄໍາພີພາສາລາວ

ສຳເນົາເນື້ອຫາເປັນພາສາອັງກິດຢູ່ທີ່ 16–18px. Lorem ipsum ຖືກຫ້າມທຸກບ່ອນໃນ repo ນີ້,
ແຕ່ຢູ່ທີ່ນີ້ມັນເປັນພຽງການວັດແທກຄວາມຍາວຂອງເສັ້ນ ແລະ ການສະແດງຕົວອັກສອນ: ໝາຈອກສີນ້ຳຕານທີ່ວ່ອງໄວໂດດ
ຂ້າມໝາຂີ້ຄ້ານ.

ຄູ່ໃຫຍ່ (Lao body text) ໃຊ້ Noto Sans Lao Looped ທີ່ 18–20px ແລະ ໄລຍະຫ່າງລະຫວ່າງ
ນາຍຊ່າງ.

## ຟອນຕ໌ພາສາລາວອົບແຫ້ງ

ໃຊ້ຕົວເລືອກ "文A" ໃນຫົວຂໍ້ເພື່ອເບິ່ງຕົວຢ່າງຕົວອັກສອນລາວແຕ່ລະຕົວ (ທັງ 8 ຕົວອັກສອນທີ່ສະເໜີໂດຍ
ໂຄງການ lao-christian-app) ທຽບກັບຕົວຢ່າງຂໍ້ຄວາມດຽວກັນ — ຫົວຂໍ້ ແລະ ເນື້ອໃນທັງສອງ
ສະຫຼັບກັນເພື່ອໃຫ້ມັນເບິ່ງຄຽງຄູ່ກັນຢ່າງຍຸດຕິທຳ. ການສະກົດຄຳຢູ່ທີ່ນີ້ໂດຍເຈດຕະນາຮັກສາ
ຕົວອັກສອນແບບດັ້ງເດີມ (R) ໃນຄຳສັບທີ່ສັກສິດແທນທີ່ຈະເປັນການສະກົດຄຳແບບງ່າຍດາຍຂອງລັດຖະບານສະໄໝໃໝ່
— ເບິ່ງ `docs/_lao-style-guide.md`.

# ບົດຮຽນ ແລະ ວິຊາສະເພາະ

ຮັກສາຄວາມຊົງຈຳອັນຍິ່ງໃຫຍ່ຂອງພະອົງ ຜູດ ູ້ດ ູ້ ູ້ ູ້ ່ ້ ່ ້ ່ ້ ່ ່ ້ ່ ້ ່ ້ ່ ້ ່ ້ ່ ້ ່ ້ ່ ້ ່ ້ ່ ່ ່ ່ ່ ່ ່ ່ ່ ່ ່ ່ ່ ່ ່ ່
ບໍລິຫານທຸລະກິດແຕ່ມີນິລັນດອນ. ແນະນຳນີ້ສະລະ, ພະຍັນຊະນະ, ຈັບປາ ແລະ (ເດືອນສາມ) ທີ່
ລາຍງານກ່ຽວກັບຈຸດໝາຍຂອງບົດສະຫຼຸບ.

## ຮູບພາບ hero ໜ້າເວັບ

ທຸກໆໜ້າຈະໄດ້ຮັບປ້າຍໂຄສະນາ hero ທີ່ມີຄວາມກວ້າງເຕັມ, ຄືກັບໜ້າຫຼັກ. ຕັ້ງໜຶ່ງແຖວຂອງຫົວຂໍ້ທາງໜ້າໄວ້ເທິງສຸດຂອງໜ້າ - ບໍ່ຕ້ອງການ HTML:

```yaml
---
hero_image: give
---
```

ອັນນີ້ຈະເລືອກເອົາ `docs/assets/img/give-light.webp` / `give-dark.webp` ໂດຍອັດຕະໂນມັດ (ເບິ່ງບລັອກ `tabs` ຂອງ `overrides/main.html`), ສະຫຼັບດ້ວຍໂຄງສີ. ໄຟລ໌ທັງສອງຕ້ອງມີຢູ່. ຢ່າຕັ້ງຄ່ານີ້ໃນ `index.md` — ໜ້າຫຼັກ
ຈະສ້າງ hero ຂອງມັນເອງໃນ `overrides/home.html`.

## ຕົວຢ່າງສີ

<div class="lc-card" style="background:var(--lc-paper); color:var(--lc-ink);">ເຈ້ຍເຂົ້າ #F6F1E7 / ນໍ້າມຶກ #173B38 </div><div class="lc-card" style="background:var(--lc-brand); color:var(--lc-paper); margin-top:.5rem;"> ສີຟ້າອ່ອນປ່າ #2E675E (ຍີ່ຫໍ້ຫຼັກ) </div><div class="lc-card" style="background:var(--lc-sage); color:var(--lc-ink); margin-top:.5rem;"> ສີຂຽວອ່ອນ #789B83 </div><div class="lc-card" style="background:var(--lc-river); color:var(--lc-ink); margin-top:.5rem;"> ສີຟ້າເຂັ້ມຄືກັບແມ່ນ້ຳ #88A7B0 </div><div class="lc-card" style="background:var(--lc-gold); color:var(--lc-ink); margin-top:.5rem;"> ຄຳຈຳປາ #E5B957 (ສະເພາະສີເຂັ້ມ) </div><div class="lc-card" style="background:var(--lc-clay); color:var(--lc-paper); margin-top:.5rem;"> ດິນເຜົາອ່ອນ #B86F50 </div><div class="lc-card" style="background:var(--lc-dark-bg); color:var(--lc-paper); margin-top:.5rem;">bg ໂໝດມືດ #102B34 </div><div class="lc-card" style="background:var(--lc-dark-paper); color:var(--lc-paper); margin-top:.5rem;"> ພື້ນຜິວໂໝດມືດ #172F35</div>

## ສ່ວນປະກອບຕ່າງໆ

<div class="lc-card" style="max-width:22rem;" markdown="1">### ອ່ານອົງປະກອບບັດຄຳພີໄບເບິນພາສາລາວ — ລັດສະໝີ 15px, ຂອບ 1px, ເງົາໜ້ອຍທີ່ສຸດ, ຍົກຂຶ້ນເລັກນ້ອຍເມື່ອເອົາໄປໃສ່ໃນເມົ້າ.

<span class="lc-chip-gold">ໃໝ່</span></div>

<div class="lc-adventist-slot" style="justify-content:flex-start; max-width:22rem; margin-top:1rem;"><img src="/assets/img/adventist-symbol.svg" alt="ໂບດເຊເວັນເດແອດເວນຕິສ" loading="lazy"> <span style="margin-left:0.6rem;">ສັນຍະລັກທາງການ, ໃຊ້ໂດຍບໍ່ໄດ້ດັດແປງຕາມຄຳແນະນຳຂອງຍີ່ຫໍ້ NAD</span></div>

ສະຫຼັບໂໝດສະຫວ່າງ/ມືດ (ເບື້ອງຂວາເທິງ) ແລະສະຫຼັບພາສາ (ໄອຄອນ 🌐) ເພື່ອກວດສອບທັງສອງຮຸ່ນ.
