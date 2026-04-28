import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

def call_api(endpoint, payload):
    try:
        res = requests.post(f"{BASE_URL}{endpoint}/invoke", json={"input": payload})
        if res.status_code == 200:
            data = res.json()["output"]
            return data["content"] if isinstance(data, dict) else data
        else:
            return f"Error {res.status_code}: {res.text}"
    except Exception as e:
        return f"Request failed: {e}"

st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("AI Chatbot (FastAPI + LangChain + Ollama)")

task = st.selectbox(
    "Choose a task",
    ("Chat", "Generate Essay", "Generate Poem")
)

if task == "Chat":
    question = st.text_input("Ask a question")
    if st.button("Submit") and question:
        with st.spinner("Thinking..."):
            result = call_api("/chat", {"question": question})
        st.subheader("Response")
        st.write(result)

elif task == "Generate Essay":
    topic = st.text_input("Enter topic for essay")
    if st.button("Generate Essay") and topic:
        with st.spinner("Generating essay..."):
            result = call_api("/essay", {"topic": topic})
        st.subheader("Essay")
        st.write(result)

elif task == "Generate Poem":
    topic = st.text_input("Enter topic for poem")
    if st.button("Generate Poem") and topic:
        with st.spinner("Generating poem..."):
            result = call_api("/poem", {"topic": topic})
        st.subheader("Poem")
        st.write(result)