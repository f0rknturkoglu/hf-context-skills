# Hugging Face Context Skills: Course Workspace

This repository contains the learning materials and implementations from the **Hugging Face Context Course**.

## 📂 File Tree

```
.
├── LICENSE                       # MIT License
├── README.md                     # Project documentation (this file)
├── .gitignore                    # Root git ignore patterns
└── context-course/
    ├── 1-skills/                 # Unit 1: Agent Skills
    │   └── hf-dataset-validation/# The dataset validation skill package
    │       ├── SKILL.md                  # Main skill configuration and instructions
    │       ├── requirements.txt          # Python dependencies
    │       ├── .gitignore                # Skill-specific git ignore patterns
    │       ├── scripts/                  # Executable helper scripts
    │       │   ├── validate_dataset.py   # JSON report and schema validator
    │       │   └── generate_report.py    # Human-readable CLI text report
    │       ├── references/               # Skill reference files
    │       │   └── examples.md           # CLI and Python import usage examples
    │       └── assets/                   # Skill templates and assets
    │           └── validation-template.txt
    ├── 2-mcp/                    # Unit 2: The Model Context Protocol (MCP)
    │   ├── app.py                # Gradio Blocks MCP text processor server
    │   ├── requirements.txt      # Python dependencies
    │   └── .gitkeep              # Keep directory placeholder
    ├── 3-plugins/                # Unit 3: Plugins
    │   └── text-processor-plugin/# Text Processor plugin bundle
    │       ├── .claude-plugin/
    │       │   └── plugin.json   # Claude Code manifest
    │       ├── .codex-plugin/
    │       │   └── plugin.json   # Codex manifest
    │       ├── .mcp.json         # Shared Stdio MCP server configuration
    │       ├── README.md         # Plugin documentation
    │       └── skills/           # Curated agent skills
    │           ├── analyze-text/
    │           │   └── SKILL.md
    │           ├── extract-keywords/
    │           │   └── SKILL.md
    │           └── check-reading-level/
    │               └── SKILL.md
    ├── 4-subagents/              # Unit 4: Subagents
    │   └── code-quality-pipeline/# Multi-agent research -> implement -> review pipeline
    │       ├── .claude/
    │       │   ├── agents/       # Claude custom agent definitions
    │       │   │   ├── researcher.md
    │       │   │   ├── implementer.md
    │       │   │   ├── security-reviewer.md
    │       │   │   └── performance-reviewer.md
    │       │   └── CLAUDE.md     # Claude-scoped project policies
    │       ├── .codex/
    │       │   └── agents/       # Codex custom agent definitions (TOML)
    │       │       ├── researcher.toml
    │       │       ├── implementer.toml
    │       │       ├── security-reviewer.toml
    │       │       └── performance-reviewer.toml
    │       ├── AGENTS.md         # Shared agent guidelines
    │       └── main.py           # Entry point mock script for auth system
    └── 5-hooks/                  # Unit 5: Hooks
        └── agent-activity-dashboard/# Cross-platform Agent Activity Dashboard
            ├── app.py            # Gradio + FastAPI server
            ├── requirements.txt  # Python requirements
            ├── .claude/
            │   └── settings.json # Claude hooks setting (with guardrail)
            ├── .codex/
            │   └── hooks.json    # Codex hooks settings (curl/jq pipes)
            ├── .opencode/
            │   └── plugins/
            │       └── dashboard.ts # OpenCode plugin hook
            └── .pi/
                └── extensions/
                    └── dashboard.ts # Pi extension hook
```

## 🚀 Setup & Usage

### Prerequisites
Ensure Python 3.11+ is installed.

```bash
# Create virtual environment and install dependencies
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r context-course/1-skills/hf-dataset-validation/requirements.txt -r context-course/2-mcp/requirements.txt -r context-course/5-hooks/agent-activity-dashboard/requirements.txt
```

### Run MCP Local Server
```bash
export no_proxy=localhost,127.0.0.1
export NO_PROXY=localhost,127.0.0.1
.venv/bin/python context-course/2-mcp/app.py
```

### Run Activity Dashboard
```bash
export no_proxy=localhost,127.0.0.1
export NO_PROXY=localhost,127.0.0.1
.venv/bin/python context-course/5-hooks/agent-activity-dashboard/app.py
```
Check the live dashboard in your browser at `http://localhost:8000`.
