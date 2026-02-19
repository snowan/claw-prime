# Viking Context

Implements a hierarchical Level-of-Detail (LOD) context management system inspired by OpenViking. 

## Structure
- **L0 (.abstract):** ~100-200 token summary for rapid relevance checking.
- **L1 (.overview):** ~1-2k token structured outline.
- **L2 (Original):** The full content.

## Tools
### `viking-context --index <path>`
Generates L0 and L1 layers for a file or directory.

### `viking-context --search <query>`
Scans L0 layers first to find relevant nodes before loading deeper context.
