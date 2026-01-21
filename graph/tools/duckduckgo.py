from langchain_core.tools import tool
from ddgs import DDGS

@tool
def duckduckgo_search(query: str, max_results: int = 5) -> str:
    """
    Search the web using DuckDuckGo.
    
    Args:
        query: The search query string
        max_results: Maximum number of results to return (default: 5)
    
    Returns:
        Formatted string containing search results with titles, URLs, and descriptions
    """
    print("using duckduckGo Tool")
    try:
        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=max_results):
                results.append(
                    f"Title: {r['title']}\n"
                    f"URL: {r['href']}\n"
                    f"Description: {r['body']}\n"
                )
        
        if not results:
            return "No results found."
        
        # print("Duck duck go result " , results)
        return results
    
    except Exception as e:
        return f"Error performing search: {str(e)}"
