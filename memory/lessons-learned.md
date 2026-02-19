## Lessons Learned: Resource & Tool Resilience

### 1. Environment Ambiguity (Bun vs Node)
- **Problem:** `ts-node` fails in certain environments due to missing types (e.g., Bun types) or configuration mismatches.
- **Solution:** Always prefer `bun` for running `.ts` scripts in this environment as it is more self-contained and faster.

### 2. Silent Quota Failures
- **Problem:** Official APIs (Google/OpenAI) often return 429s without the parent agent knowing immediately.
- **Solution:** Build "Wrapper Skills" (like `image-gen-robust`) that explicitly catch 429s and switch backends or execution engines.

### 3. Execution Zombies
- **Problem:** `exec` sessions can hang silently if they wait for network or user input (like a hidden login prompt).
- **Solution:** Always use a `timeout` in `poll` and check for file creation as a "heartbeat" of progress.

### 4. Canvas & Browser Blocking
- **Problem:** Headless environments (SSH/Gateway-only) cannot render `canvas` or `browser` without a paired node.
- **Solution:** Fall back to CLI-based status reports or generate static assets (HTML/Markdown) that can be inspected asynchronously.
