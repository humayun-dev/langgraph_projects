# state.py will act as shared folder or container for agents to read or write


from typing import Annotated,List,TypedDict
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    messages: Annotated[List,add_messages]
    research_notes:str  # where the Researcher leaves their findings
    next_node:str       # manager leaves to say who is next