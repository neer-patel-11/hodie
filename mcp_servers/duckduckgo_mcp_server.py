from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
from duckduckgo_search import DDGS

server = Server("duckduckgo-search")

@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="duckduckgo_search",
            description="Search the web using DuckDuckGo",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "max_results": {"type": "integer", "default": 5}
                },
                "required": ["query"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name, arguments):
    if name != "duckduckgo_search":
        raise ValueError("Unknown tool")
    print("DuckDuckGo Tool Used")
    query = arguments["query"]
    max_results = arguments.get("max_results", 5)

    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append(
                f"- {r['title']}\n  {r['href']}\n  {r['body']}"
            )

    return [TextContent(type="text", text="\n\n".join(results))]

async def main():
    async with stdio_server() as (read, write):
        await server.run(read, write)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
