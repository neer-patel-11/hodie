from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode, tools_condition

from graph.nodes.chat_node import chat_node
from graph.state import ChatState
from graph.tools.tools import get_tools

def get_graph():

    tools = get_tools()

    tool_node = ToolNode(tools)
    
    memory = MemorySaver()

    graph = StateGraph(ChatState)

    graph.add_node("chat_node", chat_node)
    graph.add_node("tools", tool_node)

    graph.add_edge(START, "chat_node")

    graph.add_conditional_edges("chat_node", tools_condition)
    
    graph.add_edge("tools", "chat_node")

    chatbot = graph.compile(checkpointer=memory)


    return chatbot