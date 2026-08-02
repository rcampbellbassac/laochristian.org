#!/usr/bin/env python3
"""Generate Lao MkDocs pages with Google Cloud Translation API.

This intentionally preserves front matter, comments, fenced code, URLs,
email addresses, telephone links, and Markdown link destinations. It is a
one-way content-generation tool: English files remain authoritative and Lao
files use mkdocs-static-i18n's ``.<locale>.md`` suffix convention.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import urllib.request
from pathlib import Path


PROTECTED_RE = re.compile(
    r"https?://[^\s)>\]]+|mailto:[^\s)>\]]+|tel:[^\s)>\]]+|"
    r"(?<=\()(?:(?:\.\.?/)*[\w./-]+\.md)(?=\))"
)
COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
FENCE_RE = re.compile(r"^\s*```", re.MULTILINE)


def access_token() -> str:
    return subprocess.check_output(
        ["gcloud", "auth", "print-access-token"], text=True
    ).strip()


def protect(text: str) -> tuple[str, dict[str, str]]:
    values: dict[str, str] = {}

    def replace(match: re.Match[str]) -> str:
        key = f"ZXQTOKEN{len(values):04d}QXZ"
        values[key] = match.group(0)
        return key

    return PROTECTED_RE.sub(replace, text), values


def restore(text: str, values: dict[str, str]) -> str:
    for key, value in values.items():
        text = text.replace(key, value)
    return text


def translate(contents: list[str], project: str, token: str, mime_type: str) -> list[str]:
    if not contents:
        return []
    endpoint = (
        f"https://translation.googleapis.com/v3/projects/{project}/"
        "locations/global:translateText"
    )
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(
            {
                "sourceLanguageCode": "en",
                "targetLanguageCode": "lo",
                "mimeType": mime_type,
                "contents": contents,
            }
        ).encode(),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
            "x-goog-user-project": project,
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        payload = json.load(response)
    return [item["translatedText"] for item in payload["translations"]]


def split_blocks(source: str) -> list[tuple[str, str]]:
    """Return (kind, content) blocks while preserving non-translatable syntax."""
    blocks: list[tuple[str, str]] = []
    cursor = 0

    if source.startswith("---\n"):
        end = source.find("\n---\n", 4)
        if end != -1:
            end += 5
            blocks.append(("keep", source[:end]))
            cursor = end

    body = source[cursor:]
    lines = body.splitlines(keepends=True)
    pending: list[str] = []
    in_comment = False
    in_fence = False

    def flush() -> None:
        if pending:
            text = "".join(pending)
            kind = "html" if re.search(r"</?[A-Za-z][^>]*>", text) else "text"
            blocks.append((kind, text))
            pending.clear()

    for line in lines:
        stripped = line.strip()
        if in_comment:
            blocks.append(("keep", line))
            if "-->" in line:
                in_comment = False
            continue
        if in_fence:
            blocks.append(("keep", line))
            if FENCE_RE.match(line):
                in_fence = False
            continue
        if stripped.startswith("<!--"):
            flush()
            blocks.append(("keep", line))
            in_comment = "-->" not in line
            continue
        if FENCE_RE.match(line):
            flush()
            blocks.append(("keep", line))
            in_fence = True
            continue
        if not stripped:
            flush()
            blocks.append(("keep", line))
            continue
        pending.append(line)
    flush()
    return blocks


def translate_file(path: Path, project: str, token: str) -> str:
    blocks = split_blocks(path.read_text())
    translated = list(blocks)
    for mime_type, kind in (("text/plain", "text"), ("text/html", "html")):
        indexes = [index for index, (block_kind, _) in enumerate(blocks) if block_kind == kind]
        for offset in range(0, len(indexes), 80):
            batch_indexes = indexes[offset : offset + 80]
            protected = [protect(blocks[index][1]) for index in batch_indexes]
            results = translate([text for text, _ in protected], project, token, mime_type)
            for index, result, (_, values) in zip(batch_indexes, results, protected):
                original = blocks[index][1]
                ending = "\n" if original.endswith("\n") and not result.endswith("\n") else ""
                translated[index] = (kind, restore(result, values) + ending)
    return "".join(content for _, content in translated)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--docs", type=Path, default=Path("docs"))
    parser.add_argument("--locale", default="lo")
    parser.add_argument("--source", action="append", type=Path)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    token = access_token()
    sources = args.source or sorted(
        path for path in args.docs.rglob("*.md")
        if not path.name.endswith(f".{args.locale}.md")
    )
    for source in sources:
        target = source.with_name(f"{source.stem}.{args.locale}{source.suffix}")
        if target.exists() and not args.force:
            print(f"skip existing {target}")
            continue
        target.write_text(translate_file(source, args.project, token))
        print(f"{source} -> {target}")


if __name__ == "__main__":
    main()
