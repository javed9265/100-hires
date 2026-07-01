# Collection Method

Topic: Cold outreach pipeline for B2B SaaS

Initial collection date: 2026-07-01
Latest audit/depth update: 2026-07-02

## Tools Used

- Codex for expert research, repo organization, scripting, and source review.
- Supadata YouTube transcript API for video transcript collection.
- Public LinkedIn HTML scraping for accessible LinkedIn post metadata and excerpts.
- Manual review for expert quality, source relevance, and playbook usefulness.

## YouTube Workflow

1. Find expert videos that directly discuss cold outreach, outbound sales, cold email, deliverability, or pipeline building.
2. Apply the strict recency rule: selected YouTube videos must be published on or after 2026-01-02.
3. Run `tools/build_recent_youtube_transcripts.py` with `SUPADATA_API_KEY` stored in the local environment.
4. Capture source metadata and fail the build if any selected video is older than the recency cutoff.
5. Save each YouTube file with title, expert, YouTube URL, published date, key takeaways, and full timestamped transcript.
6. Document the recency and relevance decision in `research/other/youtube-source-audit.md`.

## LinkedIn Workflow

1. Review logged-in LinkedIn recent activity pages for the selected experts.
2. Capture 3-4 latest or recently visible items per expert in each author's `latest-visible-posts.md` file.
3. Add compact content notes in `research/other/linkedin-expanded-notes.md`.
4. Mark low-relevance recent posts honestly instead of replacing them with older topic-relevant posts.
5. Remove older scraped LinkedIn post files after tightening the recency standard.

## Other Supporting Resources Workflow

1. Search for non-LinkedIn and non-YouTube resources that could strengthen a future cold outreach playbook.
2. Prioritize benchmark reports, official sender guidance, case studies, practitioner frameworks, templates, and company guides.
3. Reject generic low-signal articles that repeat basic cold email advice without data, operator credibility, or practical structure.
4. Record source links, date signals where available, why each source was included, and how it could be used later.
5. Summarize in original notes instead of copying full article text.

## Copyright And Quality Handling

- Full YouTube transcript sections are included because the assignment requested YouTube transcripts collected through an API.
- Full LinkedIn posts were not committed as raw dumps.
- The repository keeps source URLs, collection method, YouTube transcript sections, short LinkedIn excerpts, and original research notes.
- Supporting resources in `/research/other/` are curated notes and source annotations, not scraped article dumps.
- This keeps the material useful for future playbook writing while still showing the technical collection workflow.
