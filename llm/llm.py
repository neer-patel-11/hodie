# from llm.ollamaModel import get_llm
# from llm.hugginfaceModel import get_llm
# from llm.geminiModel import get_llm
from llm.gptModel import get_gptModel

_model = None

async def get_llm():
    global _model
    if _model is None:
        _model = await get_gptModel()
    
    return _model
