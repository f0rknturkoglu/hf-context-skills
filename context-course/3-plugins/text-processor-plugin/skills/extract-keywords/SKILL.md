# Extract Keywords

Use the `extract_keywords` tool from the text-processor MCP server to find the most important words in text.

## When to Use
Use this skill when the user asks for keywords, key terms, topic extraction, or content summarization.

## How to Use
Call `extract_keywords` with the text and an optional `count` parameter (default: 5). The tool returns JSON with a `keywords` array, each containing `word` and `frequency`.

## Example
User: "What are the main topics in this article?"
1. Call `extract_keywords` with count=10
2. Group related keywords into themes
3. Present themes with supporting keyword frequencies
