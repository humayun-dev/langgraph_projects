# Entry point for the Multi-Agent System
# Author: Muhammad Humayun Khan

from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import time
from app.graph import app
from langchain_core.messages import HumanMessage

st.set_page_config(page_title="Multi-Agent Research Team")

st.title("Multi-Agent Research Team")
st.markdown("Your AI Manager, Researcher, and Writer are ready to work.")

topic = st.text_input("What should we research today?", placeholder="e.g. Why are office assistants so cranky?")

if st.button("Start Research"):
    if not topic:
        st.warning("Please enter a topic first!")
    else:
        # Initialize State
        inputs = {"messages": [HumanMessage(content=topic)]}
        
        # Create a container for the "Live Feed"
        status_container = st.container()
        
        with st.spinner("Team is working..."):
            # Stream the Graph
            for event in app.stream(inputs):
                for node_name, output in event.items():
                    # Visual feedback for which agent is active
                    with status_container:
                        if node_name == "manager":
                            st.info("Manager is planning the next move...")
                        elif node_name == "researcher":
                            st.warning("Researcher is gathering facts...")
                        elif node_name == "writer":
                            st.success("Writer is drafting the final report...")
                    
                    # Store the final result when the writer finishes
                    if node_name == "writer":
                        # Fetch the final message content
                        final_report = output["messages"][-1].content
                        
                        # Display the Final Result in a nice box
                        st.markdown("---")
                        st.subheader("📝 Final Research Report")
                        st.write(final_message := final_report)
                        st.download_button("Download Report", final_message, file_name="research_report.txt")
