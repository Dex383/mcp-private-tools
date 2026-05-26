import requests
from mcp.server.fastmcp import FastMCP
from typing import List, Dict, Any

def register_repo_tools(mcp: FastMCP):
    """
    Registers repository and model search tools (GitHub & Hugging Face) into the MCP server.
    """

    @mcp.tool()
    async def search_github_repos(query: str) -> str:
        """
        Searches for the most popular repositories on GitHub based on the query.
        Returns a formatted list of the top 5 repositories.
        """
        url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            items = data.get('items', [])[:5]
            
            if not items:
                return "No repositories found on GitHub for this query."
            
            output = []
            for repo in items:
                # Using a safe formatting method to avoid f-string line break issues
                line1 = f"Repo: {repo['full_name']}"
                line2 = f"⭐ Stars: {repo['stargazers_count']}"
                line3 = f"URL: {repo['html_url']}"
                line4 = f"Description: {repo['description']}"
                output.append(f"{line1}\n{line2}\n{line3}\n{line4}\n{'-'*30}")
                
            return "\n".join(output)
        except Exception as e:
            return f"Error searching GitHub: {str(e)}"

    @mcp.tool()
    async def search_huggingface_models(query: str) -> str:
        """
        Searches for the most downloaded models on Hugging Face based on the query.
        Returns a formatted list of the top 5 models.
        """
        url = f"https://huggingface.co/api/models?search={query}&sort=downloads&direction=-1"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            results = response.json()[:5]
            
            if not results:
                return "No models found on Hugging Face for this query."
            
            output = []
            for model in results:
                # Using a safe formatting method to avoid f-string line break issues
                line1 = f"Model: {model['modelId']}"
                line2 = f"⬇️ Downloads: {model.get('downloads', 'N/A')}"
                line3 = f"URL: https://huggingface.co/{model['modelId']}"
                line4 = f"Description: {model.get('description', 'No description available')}"
                output.append(f"{line1}\n{line2}\n{line3}\n{line4}\n{'-'*30}")
                
            return "\n".join(output)
        except Exception as e:
            return f"Error searching Hugging Face: {str(e)}"
