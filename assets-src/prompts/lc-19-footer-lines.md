# LC-19 — Footer painted lines

Not a from-scratch generation: an img2img (`images.edit`) pass over our own
hand-built SVG line art, per the user's suggested workflow (SVG → raster
guide → model repaints it in the established gouache style).

Process:
1. Built a bold, high-contrast guide SVG at the target canvas size
   (1792x1024, matching the model's native output size to avoid letterboxing
   -- an earlier attempt at 1792x320 got padded with black bars) with three
   wavy lines in the brand colors, centered vertically with generous plain
   margin above/below.
2. Rasterized with Inkscape, then ran through `client.images.edit()` with a
   prompt asking for the same paper-cut gouache style as the rest of the
   site, explicit instructions to preserve the exact line paths/positions/
   colors, and to keep the background solid to all four edges (no vignette).
3. Cropped a ~420px-tall band from the result and re-exported as WebP.

Separate light and dark passes (dark used gold/sage/teal on deep-night-blue
instead of green/teal/sage on rice-paper).

Used for: sitewide footer background. Only the dark variant actually ships
(`footer-lines-dark.webp`) -- the footer background is always the dark ink
color in both site color schemes, so the light variant
(`footer-lines-light.webp`) is unused for now but kept as a candidate for a
light-background section divider elsewhere.
