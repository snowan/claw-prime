# Mission Control

Manage and visualize the agent's context, token usage, and goal progress.

## Tools

### `mission-control --status`
Show current telemetry and goal progress.

### `mission-control --check-budget`
Verify token usage. If context > 10M, stop and request user permission to continue.

## Telemetry
Logs are stored in `../../memory/telemetry.jsonl`.
