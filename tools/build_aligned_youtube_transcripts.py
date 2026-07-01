#!/usr/bin/env python3
"""Build YouTube transcript files aligned to the same 10 LinkedIn experts."""

from __future__ import annotations

import os
import re
import shutil
import sys
from pathlib import Path

from fetch_supadata_transcript import api_get, get_transcript, ms_to_timestamp


ROOT = Path("research/youtube-transcripts")

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
        "expert": "Josh Braun",
        "video": "https://www.youtube.com/watch?v=f3EnXR13xxI",
        "title": "Real life examples of cold email follow-ups from Josh Braun",
        "takeaways": [
            "Follow-ups should feel useful and human instead of automated or pushy.",
            "Good cold email copy uses simple language and buyer psychology.",
            "Examples and rewrites make abstract messaging advice easier to apply.",
            "Strong follow-up strategy helps sellers stay top of mind without damaging trust.",
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
        "expert": "Becc Holland",
        "video": "https://www.youtube.com/watch?v=jzyS1KJKUbo",
        "title": "How to Turn Cold Emails into High-Impact Conversations",
        "takeaways": [
            "Cold email should open a business conversation, not force a product pitch.",
            "Deliverability, readability, and subject lines all shape whether the buyer engages.",
            "Strong messages connect the buyer's current problem to a clear next step.",
            "Becc Holland's teardown style is useful because it shows what to remove as well as what to write.",
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
        "expert": "Nick Cegelski",
        "video": "https://www.youtube.com/watch?v=q0B8FB3GMDk",
        "title": "Nick Cegelski's best cold email advice",
        "takeaways": [
            "Cold email performance depends on earning attention before asking for time.",
            "Subject lines, preview text, and first sentences matter because they control whether the email gets read.",
            "Nick's advice supports the broader 30MPC view that outbound should be practical and direct.",
            "The source is older than the strict 2026 set but kept to maintain exact expert alignment.",
        ],
    },
    {
        "expert": "Will Allred",
        "video": "https://www.youtube.com/watch?v=eGibkMf0mes",
        "title": "Episode 197: Cold email breakdowns with Will Allred",
        "takeaways": [
            "A strong cold email is judged by clarity, relevance, and how easy it is for the buyer to respond.",
            "Will Allred's Lavender perspective adds data-backed guidance on sales email quality.",
            "Cold email breakdowns are useful because they show specific weak points in real copy.",
            "The source is older than the strict 2026 set but kept to maintain exact expert alignment.",
        ],
    },
    {
        "expert": "Belal Batrawy",
        "video": "https://www.youtube.com/watch?v=f1FdxGD_aY4",
        "title": "Use This Cold Email Sequence to 3x Your Replies in 2026",
        "takeaways": [
            "Cold outreach should be sequenced deliberately rather than sent as isolated one-off messages.",
            "Belal's no-fluff style is useful for removing weak phrases and vague claims.",
            "Sequence structure should support buyer context, objection handling, and clear next steps.",
            "The source supports the project's cold outreach pipeline theme through practical sequence thinking.",
        ],
    },
    {
        "expert": "Jesse Ouellette",
        "video": "https://www.youtube.com/watch?v=FSc54cRCdJk",
        "title": "How to Build a Bulletproof Email Waterfall with Jesse Ouellette",
        "takeaways": [
            "Bad data can damage outbound performance before copy is even tested.",
            "Email waterfall and verification strategy are core parts of cold email infrastructure.",
            "Deliverability and enrichment decisions affect both reply rates and sender reputation.",
            "Jesse's source strengthens the list-building and infrastructure side of the pipeline.",
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
    if tmp_root.exists():
        print(f"Resuming existing temporary build folder: {tmp_root}", flush=True)
    else:
        tmp_root.mkdir(parents=True, exist_ok=True)

    for source in SOURCES:
        video = str(source["video"])
        folder = tmp_root / slugify(str(source["expert"]))
        folder.mkdir(parents=True, exist_ok=True)
        out_path = folder / f"{slugify(str(source['title']))}.md"
        if out_path.exists():
            print(f"SKIP existing {out_path}", flush=True)
            built.append((out_path, "existing", -1))
            continue

        metadata, _ = api_get("/metadata", {"url": video}, api_key)
        published = format_date(metadata.get("createdAt"))

        transcript = get_transcript(video, "en", api_key)
        lines = transcript_lines(transcript.get("content"))
        if len(lines) < 20:
            raise RuntimeError(f"{video} returned too few transcript lines: {len(lines)}")

        out_path.write_text(build_markdown(source, published, lines), encoding="utf-8")
        built.append((out_path, published, len(lines)))
        print(f"{out_path} | {published} | {len(lines)} transcript lines", flush=True)

    shutil.rmtree(ROOT, ignore_errors=True)
    tmp_root.rename(ROOT)

    print(f"Built {len(built)} aligned YouTube transcript files.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
