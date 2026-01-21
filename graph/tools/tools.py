from graph.tools.duckduckgo import duckduckgo_search
from graph.tools.executeCommand import execute_command

# Testing
# @tool
# def add_numbers(a: int, b: int) -> int:
#     """Add two numbers and return the result."""
#     print("using adding tool")
#     return a + b


def get_tools():
    tools = [duckduckgo_search,execute_command]

    return tools