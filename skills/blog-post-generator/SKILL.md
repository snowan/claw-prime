---
name: blog-post-generator
description: Takes an article URL, summarizes it, performs deep research on related topics, writes a new blog post in a specified style, and creates a GitHub pull request for approval. Use when the user wants to write a blog post based on an existing article.
---

# Blog Post Generator

This skill automates the creation of a new blog post from an existing article link.

## Workflow

1.  **Summarize & Analyze**:
    *   Accept a URL as input.
    *   Use the `summarize` skill to get the main points of the article.
    *   Identify 2-3 key topics from the summary for deeper research.

2.  **Deep Research**:
    *   Use `web_search` to find additional high-quality articles on the key topics.
    *   Summarize these new articles to gather more context and depth.

3.  **Write Post**:
    *   Synthesize all gathered information.
    *   Accept a `style_guide` parameter (text or file path) to define the writing tone and format.
    *   Generate a new, original blog post based on the research and style guide.

4.  **Create Pull Request**:
    *   The main script `scripts/run.sh` will handle this.
    *   It will clone the specified repository, create a new branch, commit the post, and push.
    *   It will then use the `gh` CLI to create a pull request.
    *   The script will output the PR link.

5.  **Notify**:
    *   The agent will present the PR link to the user for review and approval.

## Parameters for `scripts/run.sh`

*   `--url <URL>`: (Required) The URL of the source article.
*   `--repo <user/repo>`: (Required) The target GitHub repository.
*   `--file-path <path/to/post.md>`: (Required) The destination path for the post inside the repo.
*   `--style-guide <"text"|path/to/file.md>`: (Optional) A string or file path describing the desired writing style.
*   `--branch-name <branch-name>`: (Optional) The name of the new git branch. Defaults to `blog-post-` + timestamp.
