#!/usr/bin/env bash
# One-off batch: generate the 10 remaining page-hero pairs at high quality.
set -euo pipefail
cd "$(dirname "$0")/.."
source .venv/bin/activate

declare -A PAIRS=(
  [lc-09-resources]=resources-hub
  [lc-10-audio]=audio
  [lc-11-sermons]=sermons
  [lc-12-studies]=studies
  [lc-13-books]=books
  [lc-14-contact]=contact
  [lc-15-apps]=apps
  [lc-16-live]=live
  [lc-17-privacy]=privacy
  [lc-18-cookies]=cookies
)

for base in "${!PAIRS[@]}"; do
  final="${PAIRS[$base]}"
  for variant in light dark; do
    prompt="assets-src/prompts/${base}-${variant}.txt"
    raw="assets-src/raw/${base}-${variant}.png"
    webp="docs/assets/img/${final}-${variant}.webp"
    echo "=== ${base} ${variant} ==="
    python3 scripts/generate_image.py --provider openai \
      --prompt-file "$prompt" --out "$raw" --size 1792x1024 --quality high
    magick "$raw" -quality 82 "$webp"
    echo "wrote $webp ($(du -h "$webp" | cut -f1))"
  done
done

echo "BATCH_DONE"
