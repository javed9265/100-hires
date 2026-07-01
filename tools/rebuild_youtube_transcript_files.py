#!/usr/bin/env python3
"""Rewrite collected YouTube notes into the assignment transcript format."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

from fetch_supadata_transcript import api_get, get_transcript, ms_to_timestamp


ROOT = Path("research/youtube-transcripts")


def extract_field(text: str, label: str) -> str | None:
    match = re.search(rf"^- {re.escape(label)}:\s*(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else None


def extract_takeaways(text: str) -> list[str]:
    match = re.search(r"## Key Ideas\s*\n(?P<body>.*?)(?:\n## |\Z)", text, re.DOTALL)
    if not match:
        return []
    bullets = []
    for line in match.group("body").splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            bullets.append(stripped[2:].strip())
    return bullets[:4]


def transcript_lines(content: object) -> list[str]:
    if isinstance(content, str):
        cleaned = content.strip()
        return [cleaned] if cleaned else []

    lines: list[str] = []
    if not isinstance(content, list):
        return lines

    for segment in content:
        if not isinstance(segment, dict):
            continue
        text = (segment.get("text") or "").strip()
        if not text:
            continue
        offset = segment.get("offset", segment.get("start"))
        lines.append(f"[{ms_to_timestamp(offset)}] {text}")
    return lines


def format_date(value: object) -> str:
    if not isinstance(value, str) or not value:
        return "Unknown"
    return value.split("T", 1)[0]


def rebuild_file(path: Path, api_key: str) -> None:
    original = path.read_text(encoding="utf-8")
    video_url = extract_field(original, "Source URL")
    if not video_url:
        raise RuntimeError(f"Missing Source URL in {path}")

    expert = path.parent.name.replace("-", " ").title()
    if expert == "Jesse Ouellette":
        expert = "Jesse Ouellette"

    takeaways = extract_takeaways(original)
    if len(takeaways) < 4:
        raise RuntimeError(f"Need at least 4 key takeaways in {path}")

    metadata, _ = api_get("/metadata", {"url": video_url}, api_key)
    transcript = get_transcript(video_url, "en", api_key)
    title = metadata.get("title") or path.stem.replace("-", " ").title()
    published = format_date(metadata.get("createdAt"))
    lines = transcript_lines(transcript.get("content"))
    if not lines:
        raise RuntimeError(f"No transcript content returned for {video_url}")

    output = [
        f"# {title}",
        f"*Expert:* {expert}",
        f"*YouTube:* {video_url}",
        f"*Published:* {published}",
        "",
        "## Key Takeaways",
        *[f"- {item}" for item in takeaways],
        "",
        "---",
        "",
        "## Full Transcript",
        "",
        *lines,
        "",
    ]
    path.write_text("\n".join(output), encoding="utf-8")


def main() -> int:
    api_key = os.environ.get("SUPADATA_API_KEY")
    if not api_key:
        print("SUPADATA_API_KEY environment variable is required.", file=sys.stderr)
        return 2

    files = sorted(ROOT.glob("*/*.md"))
    if not files:
        print("No YouTube transcript files found.", file=sys.stderr)
        return 1

    for path in files:
        rebuild_file(path, api_key)
        print(path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
