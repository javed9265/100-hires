# Collection Method

Topic: Cold outreach pipeline for B2B SaaS

Collection date: 2026-07-01

## Tools Used

- Codex for expert research, repo organization, scripting, and source review.
- Supadata YouTube transcript API for video transcript collection.
- Public LinkedIn HTML scraping for accessible LinkedIn post metadata and excerpts.
- Manual review for expert quality, source relevance, and playbook usefulness.

## YouTube Workflow

1. Find expert videos that directly discuss cold outreach, outbound sales, cold email, deliverability, or pipeline building.
2. Run `tools/fetch_supadata_transcript.py` with `SUPADATA_API_KEY` stored in the local environment.
3. Capture source metadata, transcript language, and collection method.
4. Convert raw transcript output into curated research notes with source links, key ideas, and playbook implications.

## LinkedIn Workflow

1. Find public LinkedIn posts from the selected experts.
2. Run `tools/scrape_linkedin_post.py` to extract public metadata and a short source excerpt.
3. Add research notes that explain why the post matters for a B2B SaaS cold outreach playbook.
4. Use manual browser review later if a high-value LinkedIn post is blocked or incomplete.

## Copyright And Quality Handling

- Full third-party transcripts and full LinkedIn posts were not committed as raw dumps.
- The repository keeps source URLs, collection method, short excerpts, and original research notes.
- This keeps the material useful for future playbook writing while still showing the technical collection workflow.
