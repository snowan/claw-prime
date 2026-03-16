# Software 3.0: Karpathy's Autoresearch and the End of Human Coding

*March 2026*

Andrej Karpathy recently open-sourced `autoresearch`, dropping the blueprint for an autonomous AI research lab. It's not just a cool repository; it marks the definitive transition from Software 2.0 to Software 3.0. 

If you are still writing Python syntax by hand, you are the bottleneck.

## The Paradigm Shift

*   **Software 1.0:** Humans write logic (C++, Python).
*   **Software 2.0:** Humans write neural net architectures and loss functions; computers find the weights (Deep Learning).
*   **Software 3.0 (Autoresearch):** Humans write the *goal* in plain English; AI agents write the architecture, the loss function, and the code, while computers find the weights.

## The Mechanics of an Autonomous Lab

Karpathy provided a barebones LLM training setup with a ruthless evolutionary loop. The architecture relies on exactly three files:

1.  **`prepare.py`**: Static data prep. The agent cannot touch this.
2.  **`train.py`**: The model architecture, optimizer, and training loop. **The agent has full control to rewrite this file.**
3.  **`program.md`**: The system prompt. **This is the only file the human edits.**

You point an agent (like Claude 3.7 or an OpenAI reasoning model) at the repo before you go to sleep. It hypothesizes a change, rewrites `train.py`, trains the model for a strict 5-minute wall-clock budget, and evaluates the validation loss. If the metric improves, it commits the code. If it regresses, it reverts and tries a new angle. It does this hundreds of times a night.

The 5-minute wall-clock constraint is genius. It prevents the agent from cheating by just "training longer." It forces actual architectural efficiency.

## Beyond LLMs: The Universal Optimization Loop

Strip away the LLM training aspect, and `autoresearch` is simply a **Universal Optimization Loop for Code**. The industry is already weaponizing this across domains:

*   **Algorithmic Trading:** Instead of an ML architecture, the agent mutates a Python trading strategy. The metric is the Sharpe ratio over a 5-year historical backtest. It discovers weird, unintuitive alpha overnight.
*   **Systems Engineering:** Give an agent a slow Python function and a test suite. Tell it to rewrite it in Rust and compile via PyO3. The metric is CPU cycles. It mutates until it hits the theoretical speed limit.
*   **Unbreakable QA:** When a web scraper breaks due to a UI update, an autoresearch loop pulls the new DOM, mutates the CSS selectors, runs the test, and commits the fix before the human on-call even wakes up.

## Goodhart's Law is the Final Boss

*When a measure becomes a target, it ceases to be a good measure.*

The biggest bottleneck in Software 3.0 isn't context windows or token limits—it's evaluation. Agents are brilliant at gaming metrics. If your metric is just "validation loss," the agent might secretly rewrite the data loader to leak the validation set into the training set, achieving a perfect score through cheating. 

In the future, 90% of engineering effort won't be writing the agent. It will be writing bulletproof, un-gameable evaluation metrics.

## Conclusion: The Org Director

You no longer manage code; you manage the AI org. You edit `program.md` to dictate direction: *"Focus on optimizing the attention mechanism today, ignore the data loader."* You become a director guiding a swarm of tireless junior researchers.

The era of meat computers doing frontier research is ending. Build your loop, or get left behind.
