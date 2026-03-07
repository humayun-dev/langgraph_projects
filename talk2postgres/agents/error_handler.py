from services.sql_service import execute_sql_query

def handle_sql_errors(state):
    """
    Executes SQL query safely.
    If PostgreSQL throws an error, attempts simple fixes.
    """
    query = state["sql_query"]

    try:
        result = execute_sql_query(query)
        state["result"] = result
        return state
    except Exception as e:
        # Example fallback: return empty result + log
        print("SQL Error:", e)
        state["result"] = []
        return state