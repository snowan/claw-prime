# The Multi-Agent Hierarchy: Learning from Hightouch and LangGraph

In early 2026, the industry is moving away from single-agent systems in favor of **Hierarchical Orchestration**.

## Dynamic Subagents
Used by production systems like Hightouch's AMP, this pattern involves a "Supervisor" agent spawning specialized, isolated workers. 
- **The "Scratchpad" Effect**: A subagent performs a messy, data-heavy task (like writing complex SQL or analyzing 500 images) in its own thread. 
- **Summary Injection**: Once finished, it returns only a concise summary to the Supervisor. 
- **Clean State**: The "mess" of the sub-task is discarded, keeping the Supervisor's context window high-fidelity and focused on the big picture.

## Graph-Based Persistence
LangChain/LangGraph have standardized the "Checkpointer" architecture. Every turn of the agent is a node in a graph. Because the state is saved at every node, humans can:
1. **Audit**: See exactly where an agent deviated from the plan.
2. **Intervene**: Edit the state (memory) mid-run.
3. **Resume**: Allow the agent to continue from the edited state.

This level of control is essential for any assistant that manages real financial or business assets.
