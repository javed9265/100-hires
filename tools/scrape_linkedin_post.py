#!/usr/bin/env python3
"""Scrape public LinkedIn post metadata into a compact Markdown note."""

from __future__ import annotations

import argparse
import html
import re
import urllib.parse
import urllib.request
from pathlib import Path


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")[:80] or "linkedin-post"


def extract_meta(content: str, name: str) -> str:
    patterns = [
        rf'<meta\s+name="{re.escape(name)}"\s+content="([^"]*)"',
        rf'<meta\s+property="{re.escape(name)}"\s+content="([^"]*)"',
    ]
    for pattern in patterns:
        match = re.search(pattern, content, flags=re.IGNORECASE | re.DOTALL)
        if match:
            return html.unescape(match.group(1)).strip()
    return ""


def clean_text(value: str) -> str:
    value = re.sub(r"\s+", " ", html.unescape(value))
    return value.strip()


def word_excerpt(value: str, limit: int = 120) -> str:
    words = value.split()
    if len(words) <= limit:
        return value
    return " ".join(words[:limit]).rstrip(".,;:") + "..."


def fetch(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 100-hires-research/1.0",
            "Accept": "text/html,application/xhtml+xml",
        },
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.read().decode("utf-8", errors="replace")


def build_markdown(url: str, expert: str, title: str, description: str) -> str:
    excerpt = word_excerpt(description, 120)
    return "\n".join(
        [
            f"# LinkedIn Post: {expert}",
            "",
            f"- Source URL: {url}",
            "- Collection method: Public LinkedIn HTML scrape through Codex",
            f"- Extracted title: {title or 'Unavailable'}",
            "",
            "## Source Excerpt",
            "",
            excerpt or "No public description text extracted.",
            "",
            "## Research Notes",
            "",
            "- To be summarized after expert selection is finalized.",
            "",
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--expert", required=True)
    parser.add_argument("--out-dir", default="research/linkedin-posts")
    args = parser.parse_args()

    page = fetch(args.url)
    title_match = re.search(r"<title>(.*?)</title>", page, re.DOTALL)
    html_title = re.sub(r"<.*?>", "", title_match.group(1)) if title_match else ""
    title = clean_text(extract_meta(page, "og:title") or html_title)
    description = clean_text(extract_meta(page, "description") or extract_meta(page, "og:description"))

    expert_dir = Path(args.out_dir) / slugify(args.expert)
    expert_dir.mkdir(parents=True, exist_ok=True)
    path = expert_dir / f"{slugify(title or urllib.parse.urlparse(args.url).path)}.md"
    path.write_text(build_markdown(args.url, args.expert, title, description), encoding="utf-8")
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
