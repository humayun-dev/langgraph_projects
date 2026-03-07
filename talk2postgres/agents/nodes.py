# SQL generation node
# the input will be as what is total sales in karachi?
# the plain text will be " Schema: sales(id, product, city, quantity, price)
# the AI generates " SELECT SUM(quantity * price) FROM sales WHERE city = 'Karachi';"

from agents.llm import llm
from services.sql_service import execute_sql_query

def clean_sql(raw_sql: str) -> str:
    """
    Remove Markdown code blocks from LLM output
    """
    sql = raw_sql.strip()
    # Remove starting ```sql or ```
    if sql.startswith("```sql"):
        sql = sql[len("```sql"):].strip()
    elif sql.startswith("```"):
        sql = sql[3:].strip()
    # Remove ending ```
    if sql.endswith("```"):
        sql = sql[:-3].strip()
    return sql

def generate_sql(state):
    question = state["question"]
    schema = state["schema"]

    prompt = f"""
You are an expert PostgreSQL data analyst.

Database Schema:
{schema}

Rules:
- Use correct column names
- Use exact values from the database
- city column stores values like 'Karachi', 'Lahore'
- Always calculate sales as quantity * price
- Return only SQL query
"""

    response = llm.invoke(prompt)
    sql_query = response.content

    # Clean Markdown formatting
    sql_query = clean_sql(sql_query)

    return {"sql_query": sql_query}

# SQL execution node
def execute_sql(state):
    query = state["sql_query"]
    result = execute_sql_query(query)
    return {
        "sql_query": query,
        "result": result
    }