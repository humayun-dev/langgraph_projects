import streamlit as st
import requests
import json

st.title("AI SQL Data Analyst Dashboard")

# Input box for user question
question = st.text_input("Ask a question about your sales data:")

# Choice: Normal or Streaming
mode = st.radio("Mode", ["Normal", "Streaming"])

# Button to submit
if st.button("Ask AI"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        if mode == "Normal":
            # Call /ask endpoint
            resp = requests.get("http://localhost:8000/ask", params={"question": question})
            data = resp.json()

            st.subheader("Generated SQL")
            st.code(data.get("sql_query", ""))

            st.subheader("Result")
            st.write(data.get("result", []))

        else:
            # Call /ask_stream endpoint
            resp = requests.get("http://localhost:8000/ask_stream", params={"question": question}, stream=True)
            st.subheader("Streaming Results")
            results = []
            for line in resp.iter_lines():
                if line:
                    row = json.loads(line)
                    results.append(row)
                    st.write(row)