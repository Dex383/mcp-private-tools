# 🛠️ MCP Private Tools Core (for Gemini CLI)

A professional, modular MCP (Model Context Protocol) server specifically designed to extend the capabilities of the **Gemini CLI**. This server provides high-quality, non-rate-limited tools that allow the AI to search the web and discover technical resources without the restrictions of built-in tools.

## 🎯 Purpose
The `private-tools` server is a specialized extension for **Gemini CLI** users who need a more robust way to fetch real-time data. It replaces limited or unstable built-in tools with an optimized, local implementation.

## 🚀 Features

This server provides a set of tools that the Gemini CLI can invoke autonomously:

- **`private_search`**: Robust web exploration via DuckDuckGo. No API keys, no limits, and clean results.
- **`private_fetch`**: Flexible content extraction. Unlike standard fetchers, it preserves the structure of the page (ideal for Stack Overflow and forums) while removing technical noise.
- **`stackoverflow_search`**: Direct API integration with Stack Overflow to find the most relevant questions and their accepted answers.
- **`search_github_repos`**: Deep search for the most popular and relevant open-source repositories on GitHub.
- **`search_huggingface_models`**: Specialized scouting for the best AI models on Hugging Face.

## 📦 Installation & Gemini CLI Integration

### 1. Setup Environment
```bash
git clone https://github.com/Dex383/mcp-private-tools.git
cd mcp-private-tools
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Register with Gemini CLI
Depending on how you want to use the tools, choose one of the following registration methods.

#### 🏠 Project Scope (Local)
Available only when the Gemini CLI is launched from the project root or its subdirectories.
```bash
gemini mcp add private-tools ./venv/bin/python ./main.py --trust
```

#### 🌍 Global Scope (User)
Available in every terminal session, regardless of your current working directory. 
**Important:** You must use **absolute paths** for this configuration to work globally.

```bash
gemini mcp add private-tools <PATH_TO_PROJECT>/venv/bin/python <PATH_TO_PROJECT>/main.py --scope user --trust
```
*Replace `<PATH_TO_PROJECT>` with the full path to the `mcp-private-tools` directory on your machine.*

*The `--trust` flag is recommended to avoid confirmation prompts for every tool call.*

## 🛠️ Architecture
- **Entry Point**: `main.py`
- **Core Logic**: `src/server.py`
- **Tools Modules**: `src/tools/` (e.g., `web_tools.py`, `repo_tools.py`).
- **Documentation**: `docs/TOOLS.md` contains the full technical specification of each tool.

## ⚖️ License
Distributed under the **MIT License**. See `LICENSE` for more details.
