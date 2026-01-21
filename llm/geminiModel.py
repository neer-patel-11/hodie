import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from graph.tools.tools import get_tools

load_dotenv()

def get_llm():
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in .env file")
    
    # Try these Gemini models in order
    models_to_try = [
        "gemini-2.5-flash"
    ]
    
    for model_name in models_to_try:
        try:
            print(f"Trying model: {model_name}")
            
            chat_model = ChatGoogleGenerativeAI(
                model=model_name,
                google_api_key=api_key,
                temperature=0.1,
                convert_system_message_to_human=True,
            )
            
            print(f"✓ Successfully initialized {model_name}")
            
            tools = get_tools()
            
            chat_model_with_tools = chat_model.bind_tools(tools)
            return chat_model_with_tools
            
        except Exception as e:
            print(f"✗ Failed with {model_name}: {e}")
            continue
    
    raise RuntimeError("All model initialization attempts failed")