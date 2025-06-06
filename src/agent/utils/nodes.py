from langchain_openai import ChatOpenAI


system_prompt = """
You are a helpful assistant that answers questions about the world.
"""

def call_model(state):
    messages = state["massages"]

    massages = [{"role": "user", "content": system_prompt}] + messages

    llm = ChatOpenAI(temperature=0)

    response = llm.invoke(massages)

    return {"messages": [response]}
