# Custom python functions (add, multiply)

from langchain_core.tools import tool

@tool
def multiply(a:int,b:int) -> int:
    """Multiply two integers together. Use this for any multiplication task"""
    return a*b

@tool
def add(a:int,b:int) -> int:
    """Add two integers together. Use this for any addition task"""
    return a + b

tools = [multiply,add]