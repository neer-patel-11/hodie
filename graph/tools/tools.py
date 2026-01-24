from graph.tools.duckduckgo import duckduckgo_search
from graph.tools.executeCommand import execute_command

from graph.tools.processManager import list_processes , get_process_info , get_system_info , find_process_by_name , list_disk_drives

from mcp_client import get_mcp_tools
# Testing
# @tool
# def add_numbers(a: int, b: int) -> int:
#     """Add two numbers and return the result."""
#     print("using adding tool")
#     return a + b


async def get_tools():
    tools = [
        duckduckgo_search,

        execute_command,

        #process management
        list_processes , get_process_info ,  get_system_info , find_process_by_name , list_disk_drives


        ]
    
    mcp_tools = await get_mcp_tools()

    tools.extend(mcp_tools)

    return tools