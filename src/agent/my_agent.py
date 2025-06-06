from typing import TypedDict, Literal

from langgraph.graph import StateGraph, START, END
from src.agent.utils.state import AgentState
from src.agent.utils.nodes import call_model

workflow = StateGraph(AgentState)

workflow.add_node("call_model", call_model)
# workflow.add_node("end", END)

workflow.set_entry_point("call_model")

# workflow.add_edge("start", "call_model")
workflow.add_edge("call_model", END)

graph = workflow.compile()
