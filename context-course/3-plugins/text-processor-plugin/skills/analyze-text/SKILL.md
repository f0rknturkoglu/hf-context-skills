# Analyze Text

Use the `analyze_text` tool from the text-processor MCP server to compute text statistics.

## When to Use
Use this skill when the user asks about text statistics, word counts, character counts, sentence counts, average word length, or readability metrics.

## How to Use
Call the `analyze_text` tool with the full text as input. The tool returns JSON with:
- `total_characters`, `characters_without_spaces`
- `total_words`, `total_sentences`
- `average_word_length`, `average_sentence_length`
- `unique_words`

## Example
User: "How complex is this paragraph?"
1. Call `analyze_text` with the paragraph
2. Interpret the statistics (high unique word ratio = diverse vocabulary, long average sentence length = complex prose)
3. Summarize findings in plain language
