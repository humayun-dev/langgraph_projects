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

    while True:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        inputs = {"messages": [HumanMessage(content=user_input)]}

        # stream() to see the steps the agent takes (Agent -> Tools -> Agent)
        print("\n--- Agent Thinking ---")
        for event in app.stream(inputs):
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
        
        print("-" * 30 + "\n")

if __name__ == "__main__":
    run_agent()
