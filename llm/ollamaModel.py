import os
from dotenv import load_dotenv

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_ollama import ChatOllama

from graph.tools.tools import get_tools

load_dotenv()


def get_llm():
    """
    provider: "ollama" | "huggingface"
    """

    tools = get_tools()

    # =========================
    # OLLAMA (LOCAL)
    # =========================

    models_to_try = [
        # "llama3"
        # "llama3.1"
        "mistral"
        # "phi3",
    ]

    for model in models_to_try:
        try:
            print(f"Trying Ollama model: {model}")

            chat_model = ChatOllama(
                model=model,
                temperature=0.1,
            )

            chat_model_with_tools = chat_model.bind_tools(
                tools,
                tool_choice="auto",
            )

            print(f"✓ Using Ollama model: {model}")
            return chat_model_with_tools

        except Exception as e:
            print(f"✗ Ollama failed with {model}: {e}")
            continue

    raise RuntimeError("All Ollama models failed")


