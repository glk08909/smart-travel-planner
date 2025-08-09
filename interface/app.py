import streamlit as st
import sys
import os
import csv
from datetime import datetime
# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from retrieval.llm_caller import call_llm
from retrieval.prompt_builder import build_prompt
from retrieval.retriever import retrieve_chunks
from monitoring.logger import log_user_action

st.set_page_config(page_title="Smart Travel Planner", layout="centered")

st.title("🧳 Smart Travel Planner")
st.write("Ask me anything about your travel plans, and I’ll build a custom itinerary for you!")



log_user_action("user789", "searched_flight", "Toronto to Tokyo")


user_query = st.text_input("Where would you like to go?", placeholder="e.g. 3-day trip to Kyoto")

if user_query:
    st.write("Generating your itinerary...")

    # 🔍 Step 1: Retrieve relevant travel chunks
    retrieved_chunks = retrieve_chunks(user_query)

    # 🧠 Step 2: Build the prompt
    prompt = build_prompt(user_query, retrieved_chunks)

    # 🤖 Step 3: Call the LLM
    itinerary = call_llm(prompt)

    # 📝 Step 4: Display the result
    st.markdown("### ✨ Your Custom Itinerary")
    st.write(itinerary)
    st.markdown(f"### 🗓️ Itinerary\n\n{itinerary}")

# 🙋 Feedback section
feedback = st.radio("Was this itinerary helpful?", ["👍 Yes", "👎 No"])
if feedback:
    st.write("Thanks for your feedback!")
    # Optionally log this for monitoring

def log_interaction(query, feedback, response):
    with open("data/user_logs.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), query, feedback, response])
