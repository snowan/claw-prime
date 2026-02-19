---
name: ai-article-curator
description: Extracts, filters, and summarizes the top 5 most valuable AI-related articles from a specific Hacker News blog list. Use when asked to find or summarize AI news from the emschwartz Hacker News blog OPML/gist, or when the user runs the "/curate-ai" command.
---

# AI Article Curator

Find and summarize the best AI articles from the Hacker News 2025 popular blog list.

## Commands

- `/curate-ai`: Triggers the full curation workflow to find the top 5 AI articles from the HN blog list.

## Workflow

1. **Extract Feeds**: Run `python3 scripts/extract_opml.py <opml_file>` using the content from the Hacker News blog gist (https://gist.github.com/emschwartz/e6d2bf860ccc367fe37ff953ba6de66b).
2. **Search & Filter**: Fetch entries from these feeds (using `web_fetch` or `blogwatcher`). **Always filter for articles published within the last 7 days from today's date.** Filter for AI/LLM topics.
3. **Select Top 5**: Choose the most "valuable" articles based on technical insight or impact from the last week.
4. **Summarize**: Provide a human-readable summary for each, including metadata (Title, **Date**, Source, etc.).

See [references/curation-guide.md](references/curation-guide.md) for detailed selection criteria and summary format.
