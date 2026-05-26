from mcp.server.fastmcp import FastMCP
from .tools.web_tools import register_web_tools
from .tools.repo_tools import register_repo_tools

# Initialize the central hub server
mcp = FastMCP("PrivateTools", version="0.1.0")

# --- Tool Registration ---
# Each module is responsible for registering its own set of tools.
register_web_tools(mcp)
register_repo_tools(mcp)

# Future modules can be added here:
# register_db_tools(mcp)
# register_system_tools(mcp)

if __name__ == "__main__":
    mcp.run()

