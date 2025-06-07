import os

from functools import lru_cache
from typing import Literal
from dotenv import load_dotenv
from langgraph.prebuilt import ToolNode
from langchain_openai import ChatOpenAI

from src.agent.utils.tools import tools

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

    model = model.bind_tools(tools)
    return model

system_prompt = """
You are a helpful assistant that answers questions about the world.
"""

def call_model(state):
    messages = state["messages"]

    messages = messages

    llm = _get_model()
    response = llm.invoke(messages)

    return {"messages": [response]}


def should_continue(state) -> Literal["tools", "end"]:
    messages = state["messages"]
    last_message = messages[-1]
    if not last_message.tool_calls:
        return "end"
    else:
        return "tools"


tool_node = ToolNode(tools=tools)