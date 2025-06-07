from langgraph.graph import StateGraph, END
from src.agent.utils.state import AgentState
from src.agent.utils.nodes import call_model, should_continue, tool_node

workflow = StateGraph(AgentState)

workflow.add_node("call_model", call_model)
workflow.add_node("tool", tool_node)
# workflow.add_node("end", END)

workflow.set_entry_point("call_model")

workflow.add_conditional_edges(
    "call_model",
    should_continue,
    {
        "tools": "tool",
        "end": END,
    }
)

# workflow.add_edge("start", "call_model")
workflow.add_edge("tool", "call_model")

graph = workflow.compile()
