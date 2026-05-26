from mcp.server.fastmcp import FastMCP
from duckduckgo_search import DDGS
import httpx
from bs4 import BeautifulSoup
import re
from typing import Optional

def register_web_tools(mcp: FastMCP):
    """
    Registers web-related tools into the provided MCP server instance.
    """
    
    @mcp.tool()
    async def private_search(query: str) -> str:
        """
        Searches the web using DuckDuckGo and returns the top 5 results.
        """
        try:
            with DDGS() as ddgs:
                results = [r for r in ddgs.text(query, max_results=5)]
                
            if not results:
                return "No results found."
            
            output = []
            for i, res in enumerate(results, 1):
                item = f"{i}. {res['title']}|URL: {res['href']}|Snippet: {res['body']}"
                output.append(item.replace('|', '\n   '))
                
            return "\n\n".join(output)
        except Exception as e:
            return f"Error: {str(e)}"

    @mcp.tool()
    async def private_fetch(url: str) -> str:
        """
        Fetches the content of a URL, removing only technical noise (scripts, styles, navs) 
        to preserve the full content of the page.
        """
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }
            async with httpx.AsyncClient(headers=headers, timeout=15.0) as client:
                response = await client.get(url)
                response.raise_for_status()
                html_content = response.text
            
            soup = BeautifulSoup(html_content, 'html.parser')
            
            for element in soup(['script', 'style', 'nav', 'footer', 'header', 'aside', 'noscript', 'iframe']):
                element.decompose()
            
            text = soup.get_text(separator='\n')
            lines = [line.strip() for line in text.splitlines()]
            cleaned_lines = [line for line in lines if line]
            
            return "\n".join(cleaned_lines)
            
        except Exception as e:
            return f"Error: {str(e)}"

    @mcp.tool()
    async def stackoverflow_search(query: str) -> str:
        """
        Searches Stack Overflow for the most relevant questions and returns the top result and its best answer.
        """
        search_url = f"https://api.stackexchange.com/2.3/search/advanced?site=stackoverflow&q={query}&sort=relevance&order=desc"
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                search_res = await client.get(search_url)
                search_res.raise_for_status()
                items = search_res.json().get('items', [])
            
            if not items:
                return "No results found on Stack Overflow."
            
            top_q = items[0]
            q_id = top_q['question_id']
            q_title = top_q['title']
            q_url = top_q['link']
            
            answer_url = f"https://api.stackexchange.com/2.3/questions/{q_id}/answers?site=stackoverflow&filter=withbody"
            async with httpx.AsyncClient(timeout=10.0) as client:
                ans_res = await client.get(answer_url)
                ans_res.raise_for_status()
                answers = ans_res.json().get('answers', [])
            
            best_answer = "No accepted answer found."
            for ans in answers:
                if ans.get('is_accepted') or ans.get('score', 0) == max([a.get('score', 0) for a in answers]):
                    clean_text = re.sub('<[^<]+?>', '', ans['body'])
                    best_answer = f"Best Answer (Score: {ans['score']}):\n{clean_text[:1000]}..." 
                    break
            
            output = [
                f"QUESTION: {q_title}",
                f"URL: {q_url}",
                f"\n{best_answer}"
            ]
            return "\n\n".join(output)
            
        except Exception as e:
            return f"Error: {str(e)}"
