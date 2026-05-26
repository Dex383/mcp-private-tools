# 🛠️ MCP Private Tools Core

A professional, modular MCP (Model Context Protocol) server designed to expand the capabilities of AI agents with high-quality, non-rate-limited web and repository tools.

## 🚀 Features

This server centralizes a set of tools that avoid common API limitations and provide cleaned, structured data for LLMs:

- **`private_search`**: Robust web exploration via DuckDuckGo (No API key required).
- **`private_fetch`**: Flexible content extraction that preserves page structure while removing technical noise (scripts, navs, footers).
- **`stackoverflow_search`**: Direct access to the most relevant technical solutions and accepted answers on Stack Overflow.
- **`search_github_repos`**: Discovery of popular open-source implementations and libraries.
- **`search_huggingface_models`**: Scouting for the best AI models based on downloads and descriptions.

## 📦 Installation

### 1. Clone or Download
```bash
git clone <repository-url>
cd mcp-private-tools
```

### 2. Setup Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Register with Gemini CLI
Run the following command to add the server to your CLI:
```bash
gemini mcp add private-tools ./venv/bin/python ./main.py --trust
```

## 🛠️ Architecture
The project follows a modular design:
- `main.py`: Entry point and server initialization.
- `src/server.py`: Server configuration and module registration.
- `src/tools/`: Individual modules for each toolset (e.g., `web_tools.py`).
- `docs/`: Detailed technical specifications of each tool.

## ⚖️ License
MIT
