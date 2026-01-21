from graph.tools.duckduckgo import duckduckgo_search
from langchain_core.tools import tool

@tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    print("using adding tool")
    return a + b



def get_tools():
    # return [get_duckduckgo_tool()]
    tools = [add_numbers,duckduckgo_search]

    # tools.append(duckduckgoTool)
    return tools