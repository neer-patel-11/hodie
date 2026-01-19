from langchain_core.tools import Tool
import subprocess
import json

def get_duckduckgo_tool():
    """Create a DuckDuckGo search tool using MCP server"""
    
    def search_duckduckgo(query: str) -> str:
        """Search using DuckDuckGo via MCP server"""
        try:
            # Use raw string for Windows path
            result = subprocess.run(
                ["python", r"D:\AI_agents\hodie\mcp_servers\duckduckgo_mcp_server.py"],
                input=json.dumps({"query": query, "max_results": 5}),
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                return result.stdout
            else:
                return f"Error: {result.stderr}"
                
        except Exception as e:
            return f"Search failed: {str(e)}"
    
    duckduckgo_tool = Tool(
        name="duckduckgo_search",
        description="Search the web using DuckDuckGo. Input should be a search query string.",
        func=search_duckduckgo
    )
    
    return duckduckgo_tool