import sys
import os

# Add the project root to the Python path to allow imports from the 'src' directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.server import mcp

if __name__ == "__main__":
    mcp.run()
