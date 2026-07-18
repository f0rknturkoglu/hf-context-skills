# Nano Harness

Nano Harness is a ~220-line educational Python agent framework designed to show how code-first agents work under the hood.

## 📂 Project Structure

```
6-nano-harness/
├── nano_harness.py            # Base Python-first agent loop and core tools
├── nano_harness_extended.py   # Extended harness with web_fetch, hf_search, git_log, stats tools
├── requirements.txt           # OpenAI client dependency
└── README.md                  # Project documentation (this file)
```

## ⚙️ How It Works

1. **Prompt & Instructions**: The system prompt instructs the model to only output executable Python block content and lists available safe tools.
2. **LLM Invocation**: The harness queries the configured model via Hugging Face Inference Providers (defaulting to model `zai-org/GLM-5.1` on the HF Router).
3. **Restricted Code Execution (`exec`)**: The python block is extracted and evaluated in a constrained context (`__builtins__` removed) with sandboxed functions.
4. **Sandboxed Tools**: Path confinement checks (`safe_path`), command allowlists, character output caps, and write guards are enforced at the tool boundary.
5. **Memory Loop**: Observations (stdout, stderr, errors) are fed back to the conversation message history for up to 50 iterations.

## 🚀 Running the Agent

### Configuration & Credentials
Set your API token in the environment variables:
```bash
export HF_TOKEN="hf_..."
export NANO_MODEL="zai-org/GLM-5.1"
```

### Execution
```bash
python3 nano_harness.py
# Or to run with HF API search capabilities:
python3 nano_harness_extended.py
```
