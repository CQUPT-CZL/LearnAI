import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

load_dotenv()


@lru_cache(maxsize=4)
def _get_model(model_name: str = "deepseek"):
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_API_BASE")
    if not api_key:
        raise ValueError("API_KEY not found in environment variables.")

    if model_name == "openai":
        model = ChatOpenAI(temperature=0, model_name="gpt-4o", api_key=api_key)
    elif model_name == "deepseek":
        model = ChatOpenAI(temperature=0, model_name="deepseek-chat", api_key=api_key, base_url=base_url)
    else:
        raise ValueError(f"Unsupported model type: {model_name}")

    return model

system_prompt = """
You are a helpful assistant that answers questions about the world.
"""

def call_model(state):
    messages = state["massages"]

    massages = [{"role": "user", "content": system_prompt}] + messages

    llm = ChatOpenAI(temperature=0)

    response = llm.invoke(massages)

    return {"messages": [response]}
