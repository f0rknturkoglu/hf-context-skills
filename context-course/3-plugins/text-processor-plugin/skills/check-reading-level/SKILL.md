# Check Reading Level

Use the `check_reading_level` tool from the text-processor MCP server to estimate text difficulty.

## When to Use
Use this skill when the user asks about reading level, text difficulty, grade level, or audience appropriateness.

## How to Use
Call `check_reading_level` with the text. The tool returns JSON with:
- `grade_level` (numeric Flesch-Kincaid grade)
- `reading_level` (Elementary School, Middle School, High School, or College/Academic)

## Example
User: "Is this documentation appropriate for beginners?"
1. Call `check_reading_level` with the text
2. Compare the grade level to the target audience
3. Suggest simplifications if the level is too high
