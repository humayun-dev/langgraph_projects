# Logic for 'agent' and 'tools' nodes

from dotenv import load_dotenv
from app.state import AgentState
from app.tools import tools
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage

# load the keys and gemini model
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature = 0,
    max_retries = 2
)

# binding the tools to the llm
llm_with_tools = llm.bind_tools(tools)

# call the llm
def call_model(state:AgentState):
    messages = state['messages']
    system_prompt = SystemMessage(content="You are a helpful Math Assistant. Use tools to ensure accuracy.")
    response = llm_with_tools.invoke([system_prompt]+messages)
    return {"messages":[response]}


