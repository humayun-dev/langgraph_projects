# Natural Language → SQL AI Data Analyst
> This system is designed to mimic real-world enterprise data systems by bridging the gap between natural language and relational databases.

## The Idea
The user asks questions in natural language, and the system performs the following:

* **Converts** the question to SQL using an LLM
* **Executes** it on PostgreSQL
* **Returns** results
* **Explains** insights

---

## Example
**User asks:**
> “Show total sales in Karachi last month”

---

## Agent Workflow
The system follows a structured, multi-agent process to ensure accuracy and safety:

1. **User Question** * The entry point of the request.
2. **Schema Retrieval** * Fetches the relevant table structures from the database.
3. **SQL Generation (LLM)** * Translates the intent into a precise SQL query.
4. **SQL Validation** * Checks the query for syntax errors or security risks.
5. **PostgreSQL Execution** * Runs the validated query against the live database.
6. **Result Explanation** * Transforms raw data rows into a natural language summary.

---
## LangGraph Agent Flow
This visualizes the logical path the system takes from start to finish:

**START**
   ↓
**Intent Classifier**
   ↓
**Schema Retriever**
   ↓
**SQL Generator**
   ↓
**SQL Validator**
   ↓
**Execute Query**
   ↓
**Explain Result**
   ↓
**END**

---

## Tech Stack
* **Frontend:** Streamlit
* **Backend:** FastAPI
* **Agent:** LangGraph
* **LLM:** Llama
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Cache:** Redis
* **Vector DB:** PGVector
* **Deployment:** Docker + AWS

---

## Project Structure
Below is the directory layout for the **Natural Language → SQL** system:

* **`app/`** — **FastAPI** entry point (`main.py`) and API routing.
* **`agents/`** — **LangGraph** nodes (SQL Generator, Validator, Intent Classifier, etc.).
* **`database/`** — Connection logic, SQLAlchemy models, and **PGVector** setup.
* **`schemas/`** — Pydantic models for API request/response validation.
* **`services/`** — Core business logic (e.g., direct LLM calls and LangChain tools).
* **`utils/`** — Helper functions for SQL string cleaning, formatting, and logging.
* **`tests/`** — Unit and integration tests for agentic workflow.