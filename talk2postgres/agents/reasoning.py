from agents.llm import llm
from services.sql_service import get_database_schema

def multi_step_reasoning(state):
    """
    Handles complex questions like:
    "Show total sales in Karachi and Lahore and compare with Islamabad"
    Returns structured SQL and final result.
    """
    question = state["question"]
    schema = get_database_schema()

    prompt = f"""
You are a PostgreSQL data analyst.

Schema:
{schema}

Task:
Generate SQL queries to answer the following user question:
{question}

Return:
1. SQL query
2. Explanation of logic
"""

    response = llm.invoke(prompt)
    sql_query = response.content

    # Clean markdown if any
    if sql_query.startswith("```sql"):
        sql_query = sql_query[len("```sql"):].strip()
    if sql_query.endswith("```"):
        sql_query = sql_query[:-3].strip()

    state["sql_query"] = sql_query
    return state