# Research Report: The State of Agent Harnesses (March 2026)

## 📌 Executive Summary
In early 2026, the AI industry has shifted from "Prompt Engineering" to **"Harness Engineering"**. A harness is no longer just a wrapper for an API call; it is a specialized execution environment that manages context, provides observability, and enforces architectural invariants.

---

## 🏢 Frontier Lab Architectures

### 1. OpenAI (Codex/Harness Engineering)
OpenAI's internal engineering teams have moved to a "Zero Human Code" philosophy for certain projects.
- **The Ralph Wiggum Loop**: An autonomous development cycle:
  1. Agent implements a feature/fix.
  2. Agent self-reviews locally.
  3. Agent requests a second-opinion review from a cloud-based agent.
  4. Human only intervenes for high-level judgment.
- **Ephemeral Observability**: Every "worktree" (agent task) gets its own isolated observability stack (LogQL, PromQL). Agents use this to verify performance goals (e.g., "startup must be < 800ms") autonomously.
- **Progressive Disclosure**: Agents are given a "Map" (`AGENTS.md`) rather than an exhaustive manual. They fetch specific documentation only when the task requires it.

### 2. Anthropic (Computer Use & Model-Native Tools)
Anthropic's focus is on making agents interact with software as humans do.
- **Computer Use (OSWorld)**: The model interacts with a GUI via a virtual mouse/keyboard rather than brittle APIs.
- **Context Compaction (Beta)**: The harness automatically summarizes older parts of a thread to maintain coherence without hitting token limits.
- **MCP (Model Context Protocol)**: Standardized hub for tool connectors, allowing for a plug-and-play harness architecture.

### 3. LangChain / LangGraph (State-Machine Harness)
- **Checkpointers**: Robust persistence that allows humans to "time travel" to any prior state of an agent's reasoning, edit the state, and resume.
- **Multi-Agent Hierarchies**: Shift toward a "Supervisor" model where a high-level agent delegates to specialized, ephemeral sub-agents.

---

### 4. Google (Vertex AI Agent Builder)
- **Enterprise Grounding**: Focus on "Extension" harnesses that tightly couple model output to live data in BigQuery/Databases to eliminate hallucination.

---

## 🛠️ Leading Frameworks (2025-2026)

### 🚀 Gambit (Bolt Foundry)
- **Concept**: An "OS for building reliable AI agents."
- **Innovation**: Uses "Decks" (typed, model-powered workflows) with built-in simulators for real-time trace debugging.
- **Grading**: Includes "Grader Decks" to automatically evaluate the quality of conversation turns.

### 🧥 Poncho AI
- **Concept**: "Agent Harness for the Web."
- **Innovation**: Git-native agents where behavior is versioned. Deployable as standard web endpoints (serverless/edge friendly).

### 🏛️ Hightouch (Agentic Marketing Platform)
- **Pattern**: **Dynamic Subagents**.
- **Execution**: The main agent spawns an isolated thread for messy sub-tasks (like complex SQL exploration). Only the *result* is returned to the main context; the messy history is discarded to keep the main context window clean.

---

## 📋 Implications for $10k/month Goal
To build a high-revenue personal assistant, our harness should implement:
1. **Self-Review Loop**: High quality output without human QA.
2. **Context Compaction**: Keep long-running task costs manageable.
3. **File-Based Memory**: Allow the agent to manage its own "hard drive" for large datasets.

*Ref: researches/agent-harness-2026/ (screenshots saved)*
