#!/usr/bin/env python3
"""Fetch a YouTube transcript through Supadata and save it as Markdown."""

from __future__ import annotations

import argparse
import json
import os
import re
import time
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


BASE_URL = "https://api.supadata.ai/v1"


def extract_video_id(value: str) -> str:
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", value):
        return value

    parsed = urllib.parse.urlparse(value)
    if parsed.netloc in {"youtu.be", "www.youtu.be"}:
        return parsed.path.strip("/").split("/")[0]

    query = urllib.parse.parse_qs(parsed.query)
    if "v" in query:
        return query["v"][0]

    match = re.search(r"/(?:shorts|embed)/([A-Za-z0-9_-]{11})", parsed.path)
    if match:
        return match.group(1)

    raise ValueError(f"Could not extract YouTube video id from: {value}")


def api_get(path: str, params: dict[str, str], api_key: str) -> tuple[dict, int]:
    url = f"{BASE_URL}{path}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(
        url,
        headers={
            "x-api-key": api_key,
            "User-Agent": "100-hires-research/1.0 (+https://github.com/javed9265/100-hires)",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            return json.loads(response.read().decode("utf-8")), response.status
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Supadata API error {error.code}: {body}") from error


def ms_to_timestamp(ms: int | float | None) -> str:
    total_seconds = int((ms or 0) / 1000)
    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return f"{minutes:02d}:{seconds:02d}"


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")[:80] or "youtube-transcript"


def build_markdown(video_url: str, metadata: dict, transcript: dict) -> str:
    title = metadata.get("title") or "Untitled YouTube video"
    author = metadata.get("author", {})
    channel_name = author.get("displayName") if isinstance(author, dict) else None
    upload_date = metadata.get("createdAt") or "Unknown"
    transcript_lang = transcript.get("lang") or "Unknown"
    content = transcript.get("content") or []

    lines = [
        f"# {title}",
        "",
        f"- Source URL: {video_url}",
        f"- Channel: {channel_name or 'Unknown'}",
        f"- Upload date: {upload_date}",
        f"- Transcript language: {transcript_lang}",
        f"- Collection method: Supadata YouTube transcript API",
        "",
        "## Transcript",
        "",
    ]

    if isinstance(content, str):
        lines.append(content.strip())
    else:
        for segment in content:
            text = (segment.get("text") or "").strip()
            if not text:
                continue
            offset = segment.get("offset", segment.get("start"))
            lines.append(f"[{ms_to_timestamp(offset)}] {text}")

    lines.append("")
    return "\n".join(lines)


def get_transcript(video_url: str, lang: str, api_key: str) -> dict:
    result, status = api_get(
        "/transcript",
        {"url": video_url, "lang": lang, "text": "false", "mode": "native"},
        api_key,
    )
    if status != 202:
        return result

    job_id = result.get("jobId")
    if not job_id:
        raise RuntimeError(f"Supadata returned HTTP 202 without a jobId: {result}")

    for _ in range(90):
        time.sleep(1)
        job_result, _ = api_get(f"/transcript/{job_id}", {}, api_key)
        if job_result.get("status") == "completed":
            return job_result
        if job_result.get("status") == "failed":
            raise RuntimeError(f"Supadata transcript job failed: {job_result}")

    raise RuntimeError(f"Timed out waiting for Supadata transcript job: {job_id}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("video", help="YouTube URL or 11-character video id")
    parser.add_argument("--expert", required=True, help="Expert name for folder naming")
    parser.add_argument("--out-dir", default="research/youtube-transcripts")
    parser.add_argument("--lang", default="en")
    args = parser.parse_args()

    api_key = os.environ.get("SUPADATA_API_KEY")
    if not api_key:
        print("SUPADATA_API_KEY environment variable is required.", file=sys.stderr)
        return 2

    video_id = extract_video_id(args.video)
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    metadata, _ = api_get("/metadata", {"url": video_url}, api_key)
    transcript = get_transcript(video_url, args.lang, api_key)

    title = metadata.get("title") or video_id
    expert_dir = Path(args.out_dir) / slugify(args.expert)
    expert_dir.mkdir(parents=True, exist_ok=True)
    output_path = expert_dir / f"{slugify(title)}.md"
    output_path.write_text(build_markdown(video_url, metadata, transcript), encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
