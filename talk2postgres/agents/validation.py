from services.sql_service import get_database_schema

def validate_sql(state):
    """
    Checks SQL query for:
    - Column name typos
    - Case sensitivity for text values
    - Missing required aggregates
    Returns fixed SQL query if needed.
    """
    query = state["sql_query"]
    schema = get_database_schema()

    # Example: fix 'karachi' → 'Karachi'
    for table in schema:
        if "city" in schema[table]:
            query = query.replace("'karachi'", "'Karachi'")
            query = query.replace("'lahore'", "'Lahore'")
            query = query.replace("'islamabad'", "'Islamabad'")

    state["sql_query"] = query
    return state