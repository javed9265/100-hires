#!/usr/bin/env python3
"""Check same-expert YouTube candidate metadata and transcript availability."""

from __future__ import annotations

import os
import sys

from fetch_supadata_transcript import api_get, get_transcript


CANDIDATES = {
    "Jason Bay": ["JX1UNIJwcCY"],
    "Josh Braun": ["f3EnXR13xxI", "cANfDSKS_ps", "sV2z1hTyC4M"],
    "Eric Nowoslawski": ["UDNdgW5cMw0"],
    "Florin Tatulea": ["Ag-6pB51s5o"],
    "Becc Holland": ["jzyS1KJKUbo", "Hgp3WEA494Y", "VeiQFhr-1Oc"],
    "Armand Farrokh": ["B6ttjBRnLqY"],
    "Nick Cegelski": ["q0B8FB3GMDk", "qM47Gz94-gE"],
    "Will Allred": ["sVURh0OkNzM", "eGibkMf0mes", "uIggePpCHzc"],
    "Belal Batrawy": ["f1FdxGD_aY4", "ZQzX4uTV87Y", "2aK8YyUR4Rw"],
    "Jesse Ouellette": ["FSc54cRCdJk", "pQRfa86Qf3k", "EJuF0uGn_xo", "M5VS1GT20EU"],
}


def count_segments(content: object) -> int:
    if isinstance(content, str):
        return len([line for line in content.splitlines() if line.strip()])
    if isinstance(content, list):
        return len(content)
    return 0


def main() -> int:
    api_key = os.environ.get("SUPADATA_API_KEY")
    if not api_key:
        print("SUPADATA_API_KEY environment variable is required.", file=sys.stderr)
        return 2

    for expert, video_ids in CANDIDATES.items():
        print(f"\n## {expert}")
        for video_id in video_ids:
            url = f"https://www.youtube.com/watch?v={video_id}"
            try:
                metadata, _ = api_get("/metadata", {"url": url}, api_key)
                transcript = get_transcript(url, "en", api_key)
                print(
                    "OK | "
                    f"{video_id} | "
                    f"{(metadata.get('createdAt') or 'Unknown').split('T', 1)[0]} | "
                    f"{metadata.get('title') or 'Untitled'} | "
                    f"{count_segments(transcript.get('content'))} segments"
                )
            except Exception as error:  # noqa: BLE001 - diagnostic script
                print(f"FAIL | {video_id} | {error}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
