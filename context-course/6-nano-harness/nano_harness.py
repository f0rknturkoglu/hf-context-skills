#!/usr/bin/env python3
import io
import os
import re
import subprocess
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from openai import OpenAI

# Configuration
TASK = "Inspect the workspace and provide a summary."
MODEL = os.getenv("NANO_MODEL", "zai-org/GLM-5.1")
BASE_URL = os.getenv("OPENAI_BASE_URL", "https://router.huggingface.co/v1")
API_KEY = os.getenv("HF_TOKEN") or os.getenv("OPENAI_API_KEY", "")
WORKSPACE = str(Path.cwd())
MAX_STEPS = 50
TEMPERATURE = 0.2
TIMEOUT_S = 30
MAX_CHARS = 8000
ALLOW_WRITE = False
ALLOW_COMMANDS = ["ls", "cat", "pwd", "echo", "head", "tail", "wc", "rg"]

SYSTEM_PROMPT = f"""You are a code-first agent.
Output only executable Python code, no prose.
Tools available:
- list_dir(path='.'): List directory contents
- read_file(path, max_chars=4000): Read file
- write_file(path, content): Write file (only if ALLOW_WRITE=True)
- exec_cmd(args): Run shell command
When task is complete, call:
  final_answer(result)
Constraints:
- All file paths confined to workspace: {WORKSPACE}
- Allowed commands: {ALLOW_COMMANDS}
- Max output: {MAX_CHARS} chars
- No markdown, no prose—only Python
"""

DONE = False
FINAL_RESULT = None

def clip(x, n=MAX_CHARS):
    s = str(x)
    return s[:n] + "\n...[truncated]" if len(s) > n else s

def main():
    global DONE, FINAL_RESULT
    DONE = False
    FINAL_RESULT = None

    ws = Path(WORKSPACE).resolve()

    def safe_path(user_input):
        requested = (ws / user_input).resolve()
        if not requested.is_relative_to(ws):
            raise ValueError(f"Path escapes workspace: {user_input}")
        return requested

    def list_dir(path="."):
        p = safe_path(path)
        if not p.is_dir():
            raise NotADirectoryError(str(p))
        return sorted([x.name + ("/" if x.is_dir() else "") for x in p.iterdir()])

    def read_file(path, max_chars=4000):
        p = safe_path(path)
        content = p.read_text(encoding="utf-8", errors="replace")
        return clip(content, min(max_chars, MAX_CHARS))

    def write_file(path, content):
        if not ALLOW_WRITE:
            raise PermissionError("write_file disabled")
        p = safe_path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(str(content), encoding="utf-8")
        return f"Wrote {len(str(content))} bytes"

    def exec_cmd(args):
        if args[0] not in ALLOW_COMMANDS:
            raise PermissionError(f"Command {args[0]} not allowed")
        result = subprocess.run(args, capture_output=True, timeout=TIMEOUT_S, text=True)
        output_parts = []
        if result.stdout:
            output_parts.append(f"stdout:\n{result.stdout}")
        if result.stderr:
            output_parts.append(f"stderr:\n{result.stderr}")
        output = "\n\n".join(output_parts) or f"(exit code {result.returncode} with no output)"
        return clip(output, MAX_CHARS)

    def final_answer(value):
        global DONE, FINAL_RESULT
        DONE = True
        FINAL_RESULT = value
        return value

    client = OpenAI(
        api_key=API_KEY,
        base_url=BASE_URL
    )

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": TASK}
    ]

    def extract_python(text):
        match = re.search(r"```python\n(.*?)\n```", text, re.DOTALL)
        if match:
            return match.group(1)
        return text

    for step in range(MAX_STEPS):
        print(f"\n[Step {step + 1}]")

        # 1. Call LLM
        # Supports both standard chat.completions or custom responses endpoint wrappers
        try:
            response = client.chat.completions.create(
                model=MODEL,
                temperature=TEMPERATURE,
                messages=messages
            )
            content = response.choices[0].message.content
        except Exception:
            # Fallback to responses API if using specific custom client environments
            response = client.responses.create(
                model=MODEL,
                temperature=TEMPERATURE,
                input=messages
            )
            content = response.output_text

        print(f"Model output:\n{content[:500]}...")

        # 2. Add model response to history
        messages.append({"role": "assistant", "content": content})

        # 3. Parse and execute Python code
        code = extract_python(content)
        try:
            stdout_buffer = io.StringIO()
            stderr_buffer = io.StringIO()
            exec_globals = {
                "__builtins__": {},
                "list_dir": list_dir,
                "read_file": read_file,
                "write_file": write_file,
                "exec_cmd": exec_cmd,
                "final_answer": final_answer
            }
            with redirect_stdout(stdout_buffer), redirect_stderr(stderr_buffer):
                exec(code, exec_globals)
            stdout_text = stdout_buffer.getvalue().strip()
            stderr_text = stderr_buffer.getvalue().strip()
            if DONE:
                result = f"Final answer: {clip(FINAL_RESULT)}"
            else:
                observations = []
                if stdout_text:
                    observations.append(f"stdout:\n{clip(stdout_text)}")
                if stderr_text:
                    observations.append(f"stderr:\n{clip(stderr_text)}")
                result = "\n\n".join(observations) or "Executed successfully (no output)"
        except FileNotFoundError:
            result = "Error: FileNotFoundError: File not found"
        except PermissionError as e:
            result = f"Error: PermissionError: {str(e)}"
        except subprocess.TimeoutExpired:
            result = "Error: TimeoutError: Command took too long"
        except Exception as e:
            result = f"Error: {type(e).__name__}: {str(e)}"

        # 4. Check if agent called final_answer()
        if DONE:
            print(f"✓ Task complete: {FINAL_RESULT}")
            break

        # 5. Add observation to message history
        messages.append({"role": "user", "content": result})

    if not DONE:
        print(f"✗ Max steps ({MAX_STEPS}) reached without final_answer()")

if __name__ == "__main__":
    main()
