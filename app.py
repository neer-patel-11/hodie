import sys
from pathlib import Path

# Add project root to path FIRST
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from mcp_client import get_mcp_tools
 
from langchain_core.messages import BaseMessage, HumanMessage
from dotenv import load_dotenv
from graph.graph import get_graph
import asyncio
load_dotenv()


async def main():


    chatbot =await get_graph()


    print("Type 'exit' to quit.\n")

    # thread_id still works with MemorySaver (conversation kept in RAM)
    thread_id = "demo-thread"

    while True:
        user_input = input("You: ")
        if user_input.lower().strip() in {"exit", "quit"}:
            print("Goodbye!")
            break

        # Build initial state for this turn
        state = {"messages": [HumanMessage(content=user_input)]}

        # Run the graph
        result =await chatbot.ainvoke(
            state,
            config={"configurable": {"thread_id": thread_id}},
        )

        # Get the latest message from the assistant
        messages = result["messages"]
        last_msg = messages[-1]
        print(f"Bot: {last_msg.content}\n")

if __name__ == "__main__":
    asyncio.run(main())