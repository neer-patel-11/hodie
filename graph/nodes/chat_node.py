from llm.llm import get_llm
from graph.state import ChatState
from dotenv import load_dotenv


load_dotenv()




async def chat_node(state: ChatState):
    """LLM node that may answer or request a tool call."""
    
    llm =await get_llm()

    messages = state["messages"]

    response =await llm.ainvoke(messages)

    return {"messages": [response]}

