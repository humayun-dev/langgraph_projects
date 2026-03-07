# the tools will allow llm to interact with the database
from services.sql_service import execute_sql_query, get_database_schema
from langchain.tools import tool


@tool
def read_schema():
    """Returns the database schema."""
    return get_database_schema()


@tool
def run_sql(query: str):
    """Executes SQL query on the database."""
    return execute_sql_query(query)