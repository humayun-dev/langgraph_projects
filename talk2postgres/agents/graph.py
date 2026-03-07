from langgraph.graph import StateGraph
from agents.nodes import generate_sql
from agents.validation import validate_sql
from agents.error_handler import handle_sql_errors
from agents.reasoning import multi_step_reasoning

def build_production_graph():
    graph = StateGraph(dict)

    # 1️⃣ Reasoning node (multi-step complex questions)
    graph.add_node("reasoning", multi_step_reasoning)
    # 2️⃣ SQL generation
    graph.add_node("generate_sql", generate_sql)
    # 3️⃣ SQL validation / correction
    graph.add_node("validate_sql", validate_sql)
    # 4️⃣ Execution with error handling
    graph.add_node("execute_sql", handle_sql_errors)

    # Define edges
    graph.set_entry_point("reasoning")
    graph.add_edge("reasoning", "generate_sql")
    graph.add_edge("generate_sql", "validate_sql")
    graph.add_edge("validate_sql", "execute_sql")

    # Finish point
    graph.set_finish_point("execute_sql")

    return graph.compile()