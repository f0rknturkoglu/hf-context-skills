# Hugging Face Dataset Validation Skill

This repository contains the implementation of a portable **Hugging Face Dataset Validation Skill** following the [Agent Skills Specification](https://agentskills.io). It allows AI agents to automatically discover, load, and execute dataset format and schema validation.

## 📂 File Tree

```
.
├── LICENSE                       # MIT License
├── README.md                     # Project documentation (this file)
├── .gitignore                    # Root git ignore patterns
└── hf-dataset-validation/        # The dataset validation skill package
    ├── SKILL.md                  # Main skill configuration and instructions
    ├── requirements.txt          # Python dependencies
    ├── .gitignore                # Skill-specific git ignore patterns
    ├── scripts/                  # Executable helper scripts
    │   ├── validate_dataset.py   # JSON report and schema validator
    │   └── generate_report.py    # Human-readable CLI text report
    ├── references/               # Skill reference files
    │   └── examples.md           # CLI and Python import usage examples
    └── assets/                   # Skill templates and assets
        └── validation-template.txt
```

## 🚀 Setup & Usage

### Prerequisites
Ensure Python 3.8+ is installed.

```bash
# Create virtual environment and install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -r hf-dataset-validation/requirements.txt
```

### Validation Examples

* **Generate JSON validation report:**
  ```bash
  python hf-dataset-validation/scripts/validate_dataset.py test_data/sample.csv
  ```

* **Generate human-readable text report:**
  ```bash
  python hf-dataset-validation/scripts/generate_report.py test_data/sample.csv
  ```

---

## 🤖 Agent Integration

Symlink the `hf-dataset-validation/` directory into your agent's local or global skills directory (e.g. `.claude/skills/`, `.agents/skills/`, or `.opencode/skills/`) for automatic skill discovery.
