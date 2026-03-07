from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.responses import StreamingResponse
import json

from database.create_tables import create_tables
from services.sql_service import get_database_schema, execute_sql_query
from agents.graph import build_production_graph  

import sys
from pathlib import Path

# This finds the directory where main.py is, then goes one level up to 'talk2postgres'
root_path = Path(__file__).resolve().parent.parent
if str(root_path) not in sys.path:
    sys.path.append(str(root_path))

# -------------------- lifespan --------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables...")
    create_tables()
    print("Startup finished")
    yield

# -------------------- FastAPI app --------------------
app = FastAPI(
    title="AI SQL Data Analyst",
    description="Natural Language to SQL Agent using LangGraph",
    version="1.0",
    lifespan=lifespan
)

# -------------------- Root --------------------
@app.get("/")
def root():
    return {"message": "AI SQL Agent Running"}

# -------------------- Get DB Schema --------------------
@app.get("/schema")
def schema():
    return get_database_schema()

# -------------------- Test Query --------------------
@app.get("/test-query")
def test_query():
    query = "SELECT * FROM sales;"
    return execute_sql_query(query)

# -------------------- Build LangGraph Agent --------------------
agent = build_production_graph()  # ✅ correct

# -------------------- Ask Endpoint --------------------
@app.get("/ask")
def ask(question: str):
    schema = get_database_schema()
    response = agent.invoke({
        "question": question,
        "schema": schema
    })
    # Return SQL + result
    return response

# -------------------- Streaming / Dashboard Endpoint --------------------
@app.get("/ask_stream")
def ask_stream(question: str):
    schema = get_database_schema()
    response = agent.invoke({
        "question": question,
        "schema": schema
    })

    def result_generator():
        for row in response["result"]:
            yield json.dumps(row) + "\n"

    return StreamingResponse(result_generator(), media_type="application/json")