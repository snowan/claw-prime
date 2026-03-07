# The Ralph Wiggum Loop: How Frontier Labs Build Without Humans

OpenAI recently shared a radical experiment: shipping a million-line product with **zero lines of code manually written by humans**. 

## The Core Loop
The secret is the "Ralph Wiggum Loop." Instead of a human coder, a "Codex" agent implements a feature, then:
1. **Self-Reviews**: It checks its own changes against repository invariants.
2. **Peer Review**: It triggers a second, cloud-based agent to review the Pull Request.
3. **Automated Feedback**: If the reviewer finds a bug, the original agent fixes it and pushes a new commit.

## Progressive Disclosure
Instead of stuffing 1,000 pages of documentation into every request, the OpenAI harness uses a "Map" strategy. The agent starts with a 100-line `AGENTS.md` and only "fetches" specific docs when it hits a problem. This "just-in-time" context management is what allows agents to run for 6+ hours on a single task without hallucinating.

## Lessons Learned
- **Boring Tech wins**: Agents handle "stable" libraries better than cutting-edge, experimental ones.
- **Scaffolding over Code**: The engineering discipline has shifted from writing logic to building the *environment* that enforces logic.
