# Multi-Agent Research Team

A modular AI research assistant built with **LangGraph**, **LangChain**, and **Groq**. This system uses a "Supervisor" architecture where a Manager agent coordinates between a specialized Researcher and a Technical Writer.


## Features
* **Manager Agent**: Rule-based logic to control workflow and prevent infinite loops.
* **Researcher Agent**: Extracts 3 key facts about any given topic.
* **Writer Agent**: Transforms raw facts into a professional, structured summary.
* **Streamlit UI**: A clean, web-based dashboard to interact with your agents.


##  Project Structure
```text
multi_agent_research_summary/
├── app/
│   ├── __init__.py
│   ├── state.py    # Shared state definition (TypedDict)
│   ├── nodes.py    # Agent logic (Researcher, Writer, Manager)
│   └── graph.py    # LangGraph workflow & edges
├── .env            # API Keys (hidden)
├── main.py         # CLI Entry point
├── streamlit_app.py # Web UI Entry point
└── README.md