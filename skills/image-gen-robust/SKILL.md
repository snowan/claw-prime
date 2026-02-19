# Image Generation (Robust)

Universal interface for image generation that automatically handles fallback, quota management, and tool selection.

## Tools

### `image-gen --prompt <text> --output <path> [--style blueprint|minimal|notion]`
Generates an image using the best available backend (OpenAI, Google, or Gemini-Web).

## Logic
1. Checks for API keys (`OPENAI_API_KEY`, `GOOGLE_API_KEY`).
2. Tries official `baoyu-image-gen` first.
3. If quota exceeded (429), falls back to `baoyu-danger-gemini-web` (if consent is given).
4. Handles environmental issues (bun vs ts-node).
