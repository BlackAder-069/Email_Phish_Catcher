import streamlit as st
import requests

st.title("Email Phishing Analysis Dashboard")

try:
    resp = requests.get("http://localhost:8000/analyze")
    resp.raise_for_status()
    data = resp.json()
except Exception as e:
    st.error(f"Failed to fetch data: {e}")
    st.stop()

for email in data:
    st.header(email["subject"])
    st.write("URLs:", email["urls"])
    st.write("VirusTotal:", email["virustotal"])
    st.write("MxToolbox:", email["mxtoolbox"])
    st.write("YARA:", email["yara"])
    st.markdown("---")