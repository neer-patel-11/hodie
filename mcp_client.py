from langchain_mcp_adapters.client import MultiServerMCPClient


client = MultiServerMCPClient(
     {
        "filesystem": {
            "transport": "stdio",
            "command": "npx",
            "args": [
                "@modelcontextprotocol/server-filesystem",
                "D:/",
            ],
        }, 

        # Browser automation with Playwright
        "playwright": {
            "transport": "stdio",
            "command": "npx",
            "args": [
                "@executeautomation/playwright-mcp-server"
            ],
            "env": {
                "PLAYWRIGHT_HEADLESS": "false",
                "PLAYWRIGHT_KEEP_OPEN": "true",  # If supported
                "PLAYWRIGHT_TIMEOUT": "0"    # 5 minutes timeout
            }
        },
        
    }
)


async def get_mcp_tools():
    return await client.get_tools()
