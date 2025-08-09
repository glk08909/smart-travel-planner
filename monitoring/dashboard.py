
# monitoring/dashboard.py

import streamlit as st
import json
import os
from datetime import datetime
from collections import Counter
import plotly.express as px

# Ensure correct import path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from monitoring.logger import log_user_action

#  Log a sample user action (for testing)
log_user_action("user001", "searched_flight", {
    "from": "Toronto",
    "to": "Paris",
    "date": "2025-09-10"
})

# Load logs safely
log_path = "monitoring/user_logs.json"
if not os.path.exists(log_path):
    st.warning("No user logs available yet.")
    st.stop()

with open(log_path, "r") as f:
    logs = json.load(f)

if not logs:
    st.warning("Log file is empty.")
    st.stop()

# Extract destinations
destinations = [
    log["details"].get("to")
    for log in logs
    if log["action"] == "searched_flight" and "to" in log["details"]
]
unique_destinations = sorted(set(destinations))
selected_destination = st.selectbox("Filter by Destination", ["All"] + unique_destinations)
selected_date = st.date_input("Filter by Date")

# Apply filters
filtered_logs = []
for log in logs:
    log_date = datetime.fromisoformat(log["timestamp"]).date()
    details = log.get("details", {})
    to_dest = details.get("to")

    if (
        log["action"] == "searched_flight" and
        (selected_destination == "All" or to_dest == selected_destination) and
        log_date == selected_date
    ):
        filtered_logs.append(log)

# Popular Routes Chart
routes = [
    f"{log['details'].get('from')} to {log['details'].get('to')}"
    for log in filtered_logs
]
route_counts = Counter(routes)
fig_routes = px.bar(
    x=list(route_counts.keys()),
    y=list(route_counts.values()),
    title="Most Popular Routes",
    labels={"x": "Route", "y": "Count"}
)
st.plotly_chart(fig_routes)

# Peak Hours Chart
hours = [datetime.fromisoformat(log["timestamp"]).hour for log in filtered_logs]
hour_counts = Counter(hours)
fig_hours = px.line(
    x=list(hour_counts.keys()),
    y=list(hour_counts.values()),
    title="Peak Search Hours",
    labels={"x": "Hour of Day", "y": "Search Count"}
)
st.plotly_chart(fig_hours)
