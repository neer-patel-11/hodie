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
        }
    }
)


async def get_mcp_tools():

    return await client.get_tools()
