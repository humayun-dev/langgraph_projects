# The researcher, writer and manager nodes define here

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_groq import ChatGroq
from app.state import AgentState

#llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash",temperature = 0)
llm = ChatGroq(model="llama-3.3-70b-versatile")

# researcher node which will find the facts
def researcher_node(state:AgentState):
    query = state["messages"][-1].content
    prompt = f"Find 3 key facts about: {query}. Keep it brief"
    response = llm.invoke([SystemMessage(content="You are a factual researcher"), HumanMessage(content=prompt)])

    return {"research_notes": response.content, "messages":[response], "next_node": ""}

# writer node which will tells the manager to finish the task
def writer_node(state:AgentState):
    notes = state.get("research_notes", "")
    prompt = f"Turn these notes into a professional summary:\n{notes}"
    response = llm.invoke([SystemMessage(content="You are technical writer"), HumanMessage(content=prompt)])

    return {"messages": [response], "next_node": ""}

# The manager will act as the controller
def manager_node(state: AgentState):
    if not state.get("research_notes"):
        return {"next_node": "researcher"}
    if len(state["messages"]) < 3: 
        return {"next_node": "writer"}
    return {"next_node": "finish"}
    