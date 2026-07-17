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
    └── 2-mcp/                    # Unit 2: The Model Context Protocol (MCP)
```

## 🚀 Unit 1 Setup & Usage

### Prerequisites
Ensure Python 3.8+ is installed.

```bash
# Create virtual environment and install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -r context-course/1-skills/hf-dataset-validation/requirements.txt
```

### Validation Examples

* **Generate JSON validation report:**
  ```bash
  python context-course/1-skills/hf-dataset-validation/scripts/validate_dataset.py test_data/sample.csv
  ```

* **Generate human-readable text report:**
  ```bash
  python context-course/1-skills/hf-dataset-validation/scripts/generate_report.py test_data/sample.csv
  ```

---

## 🤖 Agent Integration

Symlink the `context-course/1-skills/hf-dataset-validation/` directory into your agent's local or global skills directory (e.g. `.claude/skills/`, `.agents/skills/`, or `.opencode/skills/`) for automatic skill discovery.
