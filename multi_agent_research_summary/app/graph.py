# connecting all the nodes
from langgraph.graph import StateGraph,START,END
from app.state import AgentState
from app.nodes import manager_node,researcher_node,writer_node


builder = StateGraph(AgentState)

# add nodes
builder.add_node("manager",manager_node)
builder.add_node("researcher",researcher_node)
builder.add_node("writer",writer_node)

# add the edges/set the flow
builder.add_edge(START, "manager")
builder.add_edge("researcher", "manager")

# Optimization: After writer is done, go straight to END 
# This prevents one extra Manager call.
builder.add_edge("writer", END) 

builder.add_conditional_edges(
    "manager",
    lambda state: state["next_node"],
    {
        "researcher": "researcher",
        "writer": "writer",
        "finish": END
    }
)

app = builder.compile()