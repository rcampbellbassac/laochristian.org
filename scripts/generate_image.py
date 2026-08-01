#!/usr/bin/env python3
"""Generate LaoChristian.org art via OpenAI or Gemini image models.

Usage:
    python scripts/generate_image.py --provider openai \
        --prompt-file assets-src/prompts/lc-04-study-light.txt \
        --out assets-src/raw/lc-04-study-light.png

    python scripts/generate_image.py --provider gemini \
        --prompt-file assets-src/prompts/lc-04-study-dark.txt \
        --out assets-src/raw/lc-04-study-dark.png \
        --model gemini-3-pro-image

Requires OPENAI_API_KEY and/or GEMINI_API_KEY in the environment. Install
dependencies with `pip install -r scripts/requirements.txt` (kept separate
from the site's own requirements.txt -- these aren't needed to build or
serve the site, only to generate art for it).
"""
from __future__ import annotations

import argparse
import base64
import sys
from pathlib import Path

DEFAULT_OPENAI_MODEL = "gpt-image-2"  # chatgpt-image-latest needs org verification we don't have
DEFAULT_GEMINI_MODEL = "gemini-2.5-flash-image"


def generate_openai(prompt: str, model: str, size: str, quality: str) -> bytes:
    from openai import OpenAI

    client = OpenAI()
    response = client.images.generate(
        model=model,
        prompt=prompt,
        size=size,
        quality=quality,
        n=1,
    )
    return base64.b64decode(response.data[0].b64_json)


def generate_gemini(prompt: str, model: str) -> bytes:
    from google import genai

    client = genai.Client()
    response = client.models.generate_content(model=model, contents=prompt)
    for candidate in response.candidates:
        for part in candidate.content.parts:
            if getattr(part, "inline_data", None) is not None:
                return part.inline_data.data
    raise RuntimeError("Gemini response contained no image data")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider", choices=["openai", "gemini"], required=True)
    parser.add_argument("--prompt-file", type=Path, help="Plain-text prompt file")
    parser.add_argument("--prompt", type=str, help="Inline prompt (overrides --prompt-file)")
    parser.add_argument("--out", type=Path, required=True, help="Output PNG path")
    parser.add_argument("--model", type=str, default=None)
    parser.add_argument("--size", type=str, default="1536x1024", help="OpenAI only")
    parser.add_argument(
        "--quality",
        type=str,
        default="medium",
        choices=["low", "medium", "high", "auto"],
        help="OpenAI only -- use 'low' or 'medium' for drafts, 'high' once approved",
    )
    args = parser.parse_args()

    if args.prompt:
        prompt = args.prompt
    elif args.prompt_file:
        prompt = args.prompt_file.read_text().strip()
    else:
        parser.error("Provide --prompt or --prompt-file")
        return 2

    args.out.parent.mkdir(parents=True, exist_ok=True)

    if args.provider == "openai":
        model = args.model or DEFAULT_OPENAI_MODEL
        print(f"Generating with OpenAI {model} ({args.size}, {args.quality} quality)...")
        image_bytes = generate_openai(prompt, model, args.size, args.quality)
    else:
        model = args.model or DEFAULT_GEMINI_MODEL
        print(f"Generating with Gemini {model}...")
        image_bytes = generate_gemini(prompt, model)

    args.out.write_bytes(image_bytes)
    print(f"Wrote {args.out} ({len(image_bytes) / 1024:.0f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
