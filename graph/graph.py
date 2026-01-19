from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.tools import tool
from graph.state import ChatState
from graph.nodes.chat_node import chat_node


def get_graph():

    tools = []
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