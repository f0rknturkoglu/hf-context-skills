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
    └── 3-plugins/                # Unit 3: Plugins
        └── text-processor-plugin/# Text Processor plugin bundle
            ├── .claude-plugin/
            │   └── plugin.json   # Claude Code manifest
            ├── .codex-plugin/
            │   └── plugin.json   # Codex manifest
            ├── .mcp.json         # Shared Stdio MCP server configuration
            ├── README.md         # Plugin documentation
            └── skills/           # Curated agent skills
                ├── analyze-text/
                │   └── SKILL.md
                ├── extract-keywords/
                │   └── SKILL.md
                └── check-reading-level/
                    └── SKILL.md
```

## 🚀 Setup & Usage

### Prerequisites
Ensure Python 3.11+ is installed.

```bash
# Create virtual environment and install dependencies
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r context-course/1-skills/hf-dataset-validation/requirements.txt -r context-course/2-mcp/requirements.txt
```

### Run MCP Local Server
```bash
export no_proxy=localhost,127.0.0.1
export NO_PROXY=localhost,127.0.0.1
.venv/bin/python context-course/2-mcp/app.py
```

### Validate Unit 3 Plugin Structure
Verify all manifests, skills, and configuration files exist under `context-course/3-plugins/text-processor-plugin`.
