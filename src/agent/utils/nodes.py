from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


@lru_cache(maxsize=4)
def _get_model(model_name: str = "deepseek"):
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not found in environment variables.")
    if model_name == "openai":
        model = ChatOpenAI(temperature=0, model_name="gpt-4o", api_key=api_key)
    elif model_name == "deepseek":
        model = ChatOpenAI(temperature=0, model_name="gpt-4o", api_key=api_key)
    else:
        raise ValueError(f"Unsupported model type: {model_name}")

    model = model.bind_tools(tools)
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
