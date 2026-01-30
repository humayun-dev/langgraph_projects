# The StateGraph construction & compilation

import sqlite3
from langgraph.graph import StateGraph,START,END
from langgraph.checkpoint.sqlite import SqliteSaver
from app.tools import tools
from app.state import AgentState
from app.nodes import call_model
from langgraph.prebuilt import ToolNode


# Setup the SQLite Database - memory.sqlite will be the file
conn = sqlite3.connect("memory.sqlite",check_same_thread=False)
memory = SqliteSaver(conn)

# initialize the graph
workflow = StateGraph(AgentState)

# Add nodes to the graph
workflow.add_node("agent",call_model)

# add tools 
tool_node = ToolNode(tools)
workflow.add_node("tools",tool_node)

# Create the edges
workflow.add_edge(START,"agent")

# conditioanal edge for the tools - either need to go the tools or should return the answer
def should_continue(state:AgentState):
    last_message = state['messages'][-1]
    if hasattr(last_message,"tool_calls") and last_message.tool_calls:
        return "tools"
    return END

workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "tools": "tools", # Map the return value "tools" to the node "tools"
        END: END
    }
)

# once tool finished then return to the agent for the final answer
workflow.add_edge("tools","agent")

# compile the graph
app = workflow.compile(checkpointer=memory)



