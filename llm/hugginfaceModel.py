import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

def get_llm():
    api_token = os.getenv("HUGGINGFACE_API_TOKEN")
    
    if not api_token:
        raise ValueError("HUGGINGFACE_API_TOKEN not found in .env file")
    
    # Try these models in order - they're known to work with HF Inference API
    models_to_try = [
        "meta-llama/Llama-3.2-3B-Instruct",
        "mistralai/Mistral-7B-Instruct-v0.2",
        "HuggingFaceH4/zephyr-7b-beta",
        "microsoft/Phi-3-mini-4k-instruct",
    ]
    
    for model_id in models_to_try:
        try:
            print(f"Trying model: {model_id}")
            llm = HuggingFaceEndpoint(
                repo_id=model_id,
                huggingfacehub_api_token=api_token,
                temperature=0.1,
                max_new_tokens=256,
                task="text-generation",
            )
            
            chat_model = ChatHuggingFace(llm=llm)
            print(f"✓ Successfully initialized {model_id}")

                        
            tools = []

            
            chat_model = chat_model.bind_tools(tools)
            return chat_model
            
        except Exception as e:
            print(f"✗ Failed with {model_id}: {e}")
            continue
    
    raise RuntimeError("All model initialization attempts failed")