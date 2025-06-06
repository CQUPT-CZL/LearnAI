from typing import TypedDict, Literal

from langgraph.graph import StateGraph, START, END
from agent.utils.nodes import call_model
from agent.utils.state import AgentState


workflow = StateGraph(AgentState)

workflow.add_node("start", START)
workflow.add_node("call_model", call_model)
workflow.add_node("end", END)

workflow.set_entry_point("start")

workflow.add_edge("start", "call_model")
workflow.add_edge("call_model", "end")

graph = workflow.compile()
