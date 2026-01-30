# ReAct Math Agent with LangGraph

A high-performance, autonomous AI Agent built using **LangGraph** and the **ReAct** (Reasoning + Action) pattern. This agent demonstrates the ability to reason about mathematical simple tasks and execute Python-based tools to ensure 100% accuracy.

## Key Features
- **Autonomous Tool Selection**: The agent intelligently decides whether to answer directly or use a specific mathematical tool.
- **Stateful Logic**: Built on `StateGraph`, maintaining a clean conversation flow between the LLM and functional nodes.
- **Dynamic Routing**: Implements conditional edges to handle the "Thought -> Action -> Observation" loop.
- **Multi-Model Support**: Integrated with Google Gemini 2.5 Flash.

## The Architecture
The agent follows a cyclic graph structure:
1. **Agent Node**: Processes input and generates a "thought" or a tool call.
2. **Conditional Edge**: Evaluates if the LLM requested a tool.
3. **Tool Node**: Executes the native Python function (`add` or `multiply`).
4. **Return Edge**: Loops the result back to the Agent for final synthesis.



## Tech Stack
- **Framework**: LangGraph, LangChain
- **LLMs**: Google Gemini
- **Language**: Python 3.10+
- **Environment**: Dotenv for secure API management

## Folder Structure
```text
ReAct_agent/
├── app/
│   ├── state.py    # TypedDict State definition
│   ├── tools.py    # Custom @tool logic
│   ├── nodes.py    # LLM & Node functions
│   └── graph.py    # Graph construction & Routing
├── .env            # Private API Keys
├── main.py         # Terminal UI & Streaming Loop
└── requirements.txt