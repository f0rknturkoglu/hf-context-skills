# Hugging Face Context Skills: Dataset Validation

This repository contains learning material, documentation, and the complete implementation of the **Hugging Face Dataset Validation Skill** built as part of the **Hugging Face Context Course (Unit 1: Agent Skills)**.

A **skill** is a portable, structured package of domain knowledge conforming to the [Agent Skills Specification](https://agentskills.io). It allows code agents (such as Claude Code, Codex, OpenCode, or Pi) to discover, load, and run validation scripts automatically to ensure dataset formats, schema, and quality comply with Hugging Face Hub requirements.

---

## 📂 Repository Structure

```
.
├── README.md                     # Root documentation (this file)
├── .gitignore                    # Root git ignore patterns
└── hf-dataset-validation/        # The dataset validation skill package
    ├── SKILL.md                  # Main skill configuration and instructions
    ├── requirements.txt          # Python dependencies
    ├── .gitignore                # Skill git ignore patterns
    ├── scripts/                  # Executable helper scripts
    │   ├── validate_dataset.py   # JSON report and schema validator
    │   └── generate_report.py    # Human-readable CLI text report
    ├── references/               # Additional documentation
    │   └── examples.md           # CLI and Python import usage examples
    └── assets/                   # Skill assets and templates
        └── validation-template.txt
```

---

## 🛠️ Getting Started & Installation

### 1. Prerequisites
- **Python 3.8+**
- Packages: `pandas`, `datasets`, `numpy` (listed in `hf-dataset-validation/requirements.txt`)

### 2. Setup a Local Environment
To run the scripts locally:
```bash
# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r hf-dataset-validation/requirements.txt
```

### 3. Usage Examples
You can validate a dataset file using either script:

* **JSON Report Output:**
  ```bash
  python hf-dataset-validation/scripts/validate_dataset.py test_data/sample.csv
  ```

* **Human-Readable Report:**
  ```bash
  python hf-dataset-validation/scripts/generate_report.py test_data/sample.csv
  ```

---

## 🤖 Using the Skill with Code Agents

To make this skill discoverable by your AI agent, you can symlink the skill directory `hf-dataset-validation` into the agent's project or global skills directory.

### Project-local Symlinks

* **Claude Code** (`.claude/skills/`):
  ```bash
  mkdir -p .claude/skills
  ln -s $(pwd)/hf-dataset-validation .claude/skills/hf-dataset-validation
  ```

* **Codex / Pi** (`.agents/skills/` or `.pi/skills/`):
  ```bash
  mkdir -p .agents/skills
  ln -s $(pwd)/hf-dataset-validation .agents/skills/hf-dataset-validation
  ```

* **OpenCode** (`.opencode/skills/`):
  ```bash
  mkdir -p .opencode/skills
  ln -s $(pwd)/hf-dataset-validation .opencode/skills/hf-dataset-validation
  ```

Once symlinked, simply ask your agent:
> *"Validate my dataset at data/my_dataset.csv"*

The agent will match your request to the description in [SKILL.md](hf-dataset-validation/SKILL.md), load the instructions, and use the helper scripts automatically.

---

## 📄 License
This project is licensed under the MIT License. See the [SKILL.md](hf-dataset-validation/SKILL.md) file for details.
