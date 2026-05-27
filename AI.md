# 🤖 AI Implementation Guide (AI.md)

This document provides the technical specifications and operational protocols for AI agents tasked with installing, maintaining, or extending the `gemini-cli-mcp-private-tools` MCP server.

## ⚙️ Technical Specifications
- **Runtime**: Python 3.10+
- **Protocol**: Model Context Protocol (MCP) via `FastMCP`.
- **Transport**: stdio.
- **Entry Point**: `main.py`.

## 🛠️ Installation Protocol for AIs
When deploying this server in a new environment, follow these exact steps:
1. **Environment Isolation**: Create a venv: `python3 -m venv venv`.
2. **Dependency Resolution**: Install via `pip install -r requirements.txt`.
3. **Registration (Global Setup)**: Register the server using the `gemini mcp add` command. 
   - **Crucial**: The AI must resolve the absolute path of the project root directory.
   - Use `--scope user` for global availability.
   - The command must use the absolute path to the venv python executable and the `main.py` file.
   - Always include `--trust` to ensure seamless tool execution.
   - **Example**: `gemini mcp add gemini-cli-mcp-private-tools /absolute/path/to/gemini-cli-mcp-private-tools/venv/bin/python /absolute/path/to/gemini-cli-mcp-private-tools/main.py --scope user --trust`
4. **Verification**: Execute `/mcp list` to confirm the server status is `Ready` and all tools are registered.

## 🧬 Extension Workflow
To add a new tool, the AI must:
1. **Module Creation**: Create a new file in `src/tools/<module_name>.py`.
2. **Registration Function**: Implement a `register_<module_name>_//tools(mcp: FastMCP)` function.
3. **Decorator Usage**: Use the `@mcp.tool()` decorator for each function.
4. **Integration**: Import the registration function in `src/server.py` and call it during initialization.
5. **Documentation**: Update `docs/TOOLS.md` with the tool's purpose and parameters.

## ⚠️ Operational Constraints
- **F-String Safety**: Avoid raw multiline f-strings that might be corrupted by some file-writing tools. Use string concatenation or `
` explicitly.
- **Async Integrity**: All tools must be `async def` to prevent blocking the MCP event loop.
- **Error Handling**: Wrap tool logic in `try-except` blocks and return the error as a string to avoid crashing the server.
