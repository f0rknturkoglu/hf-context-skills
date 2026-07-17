# Text Processor Plugin

This plugin packages text-analysis workflows and statistical tools for code agents using the Model Context Protocol (MCP) server.

## 📂 Plugin Structure

```
text-processor-plugin/
├── .claude-plugin/
│   └── plugin.json       # Claude Code manifest
├── .codex-plugin/
│   └── plugin.json       # Codex manifest
├── .mcp.json             # Stdio MCP configuration pointing to Unit 2 server
├── README.md             # Plugin documentation (this file)
└── skills/               # Curated agent skills
    ├── analyze-text/
    │   └── SKILL.md
    ├── extract-keywords/
    │   └── SKILL.md
    └── check-reading-level/
        └── SKILL.md
```

## 🛠️ Usage & Integration

### Stdio MCP Setup
The plugin is pre-configured to run the local Gradio server via the project virtual environment:
```json
{
  "mcpServers": {
    "text-processor": {
      "command": "../../../.venv/bin/python",
      "args": ["../../2-mcp/app.py"]
    }
  }
}
```

### Deployed Space Integration
To use a remote Hugging Face Space deployment, edit `.mcp.json` to configure the URL:
```json
{
  "mcpServers": {
    "text-processor": {
      "url": "https://YOUR-USERNAME-text-processor-mcp.hf.space/gradio_api/mcp/"
    }
  }
}
```

---

## 📄 License
This plugin is licensed under the MIT License.
