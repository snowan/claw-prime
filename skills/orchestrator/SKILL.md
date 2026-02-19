# Orchestrator

The "Central Nervous System" for automated content-to-revenue pipelines. Uses the `skill-graph.json` to chain multiple Baoyu skills into a single high-leverage workflow.

## Tools

### `orchestrate --pipeline <name> --input <value> [--target <platform>]`
Executes a pre-defined pipeline from the skill graph.

**Available Pipelines:**
- `article_to_social`: URL -> Markdown -> Illustrations -> Compression -> WeChat/X.
- `thread_to_infographic`: X URL -> Markdown -> Infographic -> XHS/X.

## Logic
1. Reads `/Users/xiaowei.wan/clawd/memory/skill-graph.json`.
2. Spawns sub-agents for heavy lifting (e.g., image generation).
3. Monitors context and token usage via `mission-control`.
