# Entry point to run the agent
# Build a ReAct Agent (Reasoning + Acting) that has access to basic calculator tools. 
# Instead of the LLM just "guessing" the answer, it must:
# 1. Analyze the query.
# 2. Decide to use a tool (e.g., multiply or add).
# 3. Execute the tool and observe the result.
# 4. Repeat or Finish by providing the final answer.

# Author: Muhammmad Humayun Khan

from app.graph import app
from langchain_core.messages import HumanMessage

def run_agent():
    print("--- Welcome ReAct (Reasoning plus action) LangGraph Agent! ---")
    print("Type 'quit' or 'exit' to stop.\n")

    # config telling LLM as which conversation does this execution belongs too
    # here I am using the fixed user_session_1 otherwise in production it will be real user id
    # for unique users it will be as thread_id = str(uuid.uuid4())
    # for web based systems it will be then thread_id = f"user_{user_id}_chat_{chat_id}"
    config = {
        "configurable": {
            "thread_id": "user_session_1"
        }
    }
    
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        inputs = {"messages": [HumanMessage(content=user_input)]}

        # stream() to see the steps the agent takes (Agent -> Tools -> Agent)
        print("\n--- Agent Thinking ---")
        for event in app.stream(inputs,config=config):
            # Each 'event' is a dictionary showing which node just ran
            for node_name, output in event.items():
                print(f"[Node: {node_name}]")
                
                # Check if there is a message to print
                if "messages" in output:
                    last_msg = output["messages"][-1]
                    
                    # If it's the agent node, show what it said
                    if node_name == "agent":
                        # If the agent decided to use a tool, it won't have text content yet
                        if last_msg.tool_calls:
                            print(f"Action: Agent wants to use tools: {[t['name'] for t in last_msg.tool_calls]}")
                        else:
                            print(f"Assistant: {last_msg.content}")
                    
                    # If it's the tools node, show the result of the math
                    elif node_name == "tools":
                        print(f"Tool Result: {last_msg.content}")
        
        snapshot = app.get_state(config)
        if snapshot.next:
            print("\nPAUSED: Approval required to execute tools.")
            user_approval = input("Proceed? (y/n): ")

            if user_approval.lower() in ['y', 'yes']:
                print("Resuming...")
                # Resume by passing None. It picks up right where it stopped.
                for event in app.stream(None, config=config):
                    for node_name, output in event.items():
                        print(f"[Node: {node_name}]")
                        if "messages" in output:
                            last_msg = output["messages"][-1]
                            if node_name == "agent":
                                print(f"Assistant: {last_msg.content}")
                            elif node_name == "tools":
                                print(f"Tool Result: {last_msg.content}")
            else:
                print("Tool execution cancelled.")
        
        print("-" * 30 + "\n")

if __name__ == "__main__":
    run_agent()
