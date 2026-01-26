import sys
from pathlib import Path
# import logging
# logging.basicConfig(level=logging.DEBUG)


# Add project root to path FIRST
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))


from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
from graph.graph import get_graph
import asyncio
load_dotenv()


SYSTEM_PROMPT = SystemMessage(
    content=(
        "You are a desktop AI agent. "
        "You have access to tools that can interact with the user's computer, "
        "run commands, read/write files, and perform system-level tasks. "
        "You should decide when to use tools and help the user accomplish "
        "whatever they want efficiently and safely."
        "Use sequential-thinking to reason step by step before complex actions. Store important facts in memory"
    )
)


async def main():


    chatbot =await get_graph()


    print("Type 'exit' to quit.\n")

    # thread_id still works with MemorySaver (conversation kept in RAM)
    thread_id = "demo-thread"

    initialized = False

    while True:

        user_input = input("You: ")
        if user_input.lower().strip() in {"exit", "quit"}:
            print("GoodBye")
            break

        if not initialized:
            messages = [
                SYSTEM_PROMPT,
                HumanMessage(content=user_input),
            ]
            initialized = True
        else:
            messages = [HumanMessage(content=user_input)]

        state = {"messages": messages}

        result = await chatbot.ainvoke(
            state,
            config={"configurable": {"thread_id": thread_id}},
        )

        print("Bot:", result["messages"][-1].content)
        
if __name__ == "__main__":
    asyncio.run(main())