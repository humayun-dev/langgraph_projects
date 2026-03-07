from agents.llm import llm

response = llm.invoke("Hello")

print(response.content)