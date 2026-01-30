# Defines the TypedDict (Agent.graph.state import StateGraph

from typing import Annotated,TypedDict
from langgraph.graph.message import add_messages


# in the class, the messages is the key and the add_messages will append the conversation between different nodes and not overwrite
class AgentState(TypedDict):
    messages:Annotated[list,add_messages]



