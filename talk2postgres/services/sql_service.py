# these services will be used by the AI Agent or the AI agent will interact Postgres through these services
# the AI agent will not directly communicate with the Postgres but will use the services

from database.connection import SessionLocal
from sqlalchemy import text     # allows raw sql execution safely

# function which will execute sql query to the PostgreSQL and will return the result in the JSON Format
def execute_sql_query(query: str):
    
    db = SessionLocal()

    try:
        result = db.execute(text(query))
        rows = result.fetchall()

        return [dict(row._mapping) for row in rows]

    except Exception as e:
        return {"error": str(e)}

    finally:
        db.close()

# function that will get the database schema 
# the AI must know table name, datatypes and columns as it will receive data in the json format
def get_database_schema():

    db = SessionLocal()

    query = """
    SELECT
        table_name,
        column_name,
        data_type
    FROM information_schema.columns
    WHERE table_schema = 'public'
    """

    result = db.execute(text(query))
    rows = result.fetchall()

    db.close()

    schema = {}

    for row in rows:
        table = row.table_name

        if table not in schema:
            schema[table] = []

        schema[table].append({
            "column": row.column_name,
            "type": row.data_type
        })

    return schema

