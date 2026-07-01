#!/usr/bin/env python3
"""Build 2026-only YouTube transcript files for the cold outreach project."""

from __future__ import annotations

import os
import re
import shutil
import sys
from pathlib import Path

from fetch_supadata_transcript import api_get, get_transcript, ms_to_timestamp


ROOT = Path("research/youtube-transcripts")
MIN_DATE = "2026-01-02"

SOURCES = [
    {
        "expert": "Jason Bay",
        "video": "https://www.youtube.com/watch?v=JX1UNIJwcCY",
        "title": "Cold Email Masterclass: Everything You Need To Book Meetings in 2026",
        "takeaways": [
            "Cold email has to earn attention with a clear reason for reaching out, not volume alone.",
            "Better meetings come from tighter targeting, specific pains, and concise copy.",
            "The offer and CTA should reduce friction instead of forcing an immediate calendar ask.",
            "Pipeline teams should judge campaigns by replies and meetings, not vanity metrics.",
        ],
    },
    {
        "expert": "Armand Farrokh",
        "video": "https://www.youtube.com/watch?v=B6ttjBRnLqY",
        "title": "Armand Farrokh on building an outbound machine + creative ways to build pipeline",
        "takeaways": [
            "Outbound works best as a repeatable operating system, not a collection of one-off tactics.",
            "Pipeline creation needs clear account selection, creative touches, and consistent execution.",
            "Multi-channel outbound gives sellers more ways to create attention than email alone.",
            "Managers should inspect the quality of inputs, not only the final meeting count.",
        ],
    },
    {
        "expert": "Florin Tatulea",
        "video": "https://www.youtube.com/watch?v=Ag-6pB51s5o",
        "title": "Cold Email Showdown: Rookie Sales Rep vs 10-Year Director",
        "takeaways": [
            "Cold email quality improves when the writer names a specific business problem quickly.",
            "Generic personalization is weaker than a relevant trigger or account-level observation.",
            "The best edits remove fluff and make the next step easier to answer.",
            "A teardown format turns abstract copy rules into practical examples.",
        ],
    },
    {
        "expert": "Eric Nowoslawski",
        "video": "https://www.youtube.com/watch?v=UDNdgW5cMw0",
        "title": "Cold Email Follow-Up Strategy for 2026 (Data-Backed)",
        "takeaways": [
            "Follow-up strategy should be based on reply behavior and evidence, not arbitrary bump emails.",
            "Cold email systems need testing across timing, angles, and value propositions.",
            "Data-backed iteration helps separate weak copy from weak targeting or poor deliverability.",
            "A useful sequence keeps adding context instead of repeating the same ask.",
        ],
    },
    {
        "expert": "Nick Abraham",
        "video": "https://www.youtube.com/watch?v=h2j0gFz9RH4",
        "title": "Cold Email Deliverability in 2026: The New Rules (Avoid Spam Folders)",
        "takeaways": [
            "Deliverability is now a core part of cold outreach performance, not a technical afterthought.",
            "Authentication, infrastructure, sending behavior, and list quality all affect inbox placement.",
            "Teams should monitor spam risk before scaling outbound volume.",
            "Avoiding spam folders requires operational discipline across domains, inboxes, and copy.",
        ],
    },
    {
        "expert": "Matt Lucero",
        "video": "https://www.youtube.com/watch?v=BakY-82NYVQ",
        "title": "How To Generate Leads With Cold Email in 2026 (FULL COURSE)",
        "takeaways": [
            "Lead generation starts with a clear offer, a defined audience, and a reason the buyer should care.",
            "Cold email campaigns need list building, infrastructure, copy, and follow-up working together.",
            "A full-course format helps evaluate the whole pipeline rather than isolated email tips.",
            "The system should be measured from prospect selection through booked conversations.",
        ],
    },
    {
        "expert": "Connor Murray",
        "video": "https://www.youtube.com/watch?v=_uvWsGqWxr0",
        "title": "Cold Emailing in 2026: The Only System SDRs and AEs Need",
        "takeaways": [
            "SDRs and AEs need a practical cold email system, not disconnected templates.",
            "Modern cold outreach depends on clear targeting, relevant context, and disciplined sequencing.",
            "A repeatable workflow helps reps avoid random personalization and inconsistent follow-up.",
            "Cold email still works when it is specific enough to feel written for the recipient's situation.",
        ],
    },
    {
        "expert": "Jeremy Miner",
        "video": "https://www.youtube.com/watch?v=il2p-OD4Res",
        "title": "2026 Cold Calling Techniques (He Trained 1 Million Sales Reps)",
        "takeaways": [
            "Cold calling remains useful when the opener lowers resistance instead of forcing a pitch.",
            "Question quality matters more than sounding enthusiastic or overly scripted.",
            "A good call helps the buyer clarify whether a problem is worth discussing.",
            "Cold outreach pipelines are stronger when calls support email and other touchpoints.",
        ],
    },
    {
        "expert": "Aaron Shepherd",
        "video": "https://www.youtube.com/watch?v=L-E2HEtXTjc",
        "title": "Beginner's Guide to Cold Email in 2026 (FULL SETUP)",
        "takeaways": [
            "A working cold email setup requires infrastructure before scale.",
            "Beginners need to connect domains, inboxes, targeting, and copy into one workflow.",
            "Setup quality affects whether later campaign testing produces reliable results.",
            "Cold outreach should be built step by step instead of copied from isolated templates.",
        ],
    },
    {
        "expert": "Adam Robinson",
        "video": "https://www.youtube.com/watch?v=P7dNHG1Xu6E",
        "title": "Cold Email is Dead... Here's What Works in 2026",
        "takeaways": [
            "Generic cold email is losing effectiveness as inboxes become more crowded.",
            "Teams need stronger intent signals and better buyer context to earn attention.",
            "Outbound should adapt toward relevance, timing, and recognizable proof.",
            "The video is useful as a pressure test for traditional cold email tactics.",
        ],
    },
]


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")[:90] or "youtube-transcript"


def format_date(value: object) -> str:
    if not isinstance(value, str) or not value:
        return "Unknown"
    return value.split("T", 1)[0]


def transcript_lines(content: object) -> list[str]:
    if isinstance(content, str):
        return [line.strip() for line in content.splitlines() if line.strip()]

    if not isinstance(content, list):
        return []

    lines: list[str] = []
    for segment in content:
        if not isinstance(segment, dict):
            continue
        text = " ".join((segment.get("text") or "").split())
        if not text:
            continue
        offset = segment.get("offset", segment.get("start"))
        lines.append(f"[{ms_to_timestamp(offset)}] {text}")
    return lines


def build_markdown(source: dict[str, object], published: str, lines: list[str]) -> str:
    return "\n".join(
        [
            f"# {source['title']}",
            f"*Expert:* {source['expert']}",
            f"*YouTube:* {source['video']}",
            f"*Published:* {published}",
            "",
            "## Key Takeaways",
            *[f"- {item}" for item in source["takeaways"]],
            "",
            "---",
            "",
            "## Full Transcript",
            "",
            *lines,
            "",
        ]
    )


def main() -> int:
    api_key = os.environ.get("SUPADATA_API_KEY")
    if not api_key:
        print("SUPADATA_API_KEY environment variable is required.", file=sys.stderr)
        return 2

    built: list[tuple[Path, str, int]] = []
    tmp_root = ROOT.with_name("youtube-transcripts-tmp")
    shutil.rmtree(tmp_root, ignore_errors=True)
    tmp_root.mkdir(parents=True, exist_ok=True)

    for source in SOURCES:
        video = str(source["video"])
        metadata, _ = api_get("/metadata", {"url": video}, api_key)
        published = format_date(metadata.get("createdAt"))
        if published < MIN_DATE:
            raise RuntimeError(f"{video} is older than {MIN_DATE}: {published}")

        transcript = get_transcript(video, "en", api_key)
        lines = transcript_lines(transcript.get("content"))
        if len(lines) < 20:
            raise RuntimeError(f"{video} returned too few transcript lines: {len(lines)}")

        folder = tmp_root / slugify(str(source["expert"]))
        folder.mkdir(parents=True, exist_ok=True)
        out_path = folder / f"{slugify(str(source['title']))}.md"
        out_path.write_text(build_markdown(source, published, lines), encoding="utf-8")
        built.append((out_path, published, len(lines)))

    shutil.rmtree(ROOT, ignore_errors=True)
    tmp_root.rename(ROOT)

    for path, published, line_count in built:
        print(f"{path} | {published} | {line_count} transcript lines")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
