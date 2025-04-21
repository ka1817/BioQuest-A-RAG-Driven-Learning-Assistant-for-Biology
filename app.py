import streamlit as st
import requests

st.set_page_config(page_title="BioRAG Assistant 🧬", page_icon="🧪", layout="wide")

st.markdown("<h1 style='text-align: center;'>🧠 BioRAG: Biology Learning Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Ask your biology questions and get accurate, syllabus-based answers.</p>", unsafe_allow_html=True)

with st.form("chat_form", clear_on_submit=True):
    question = st.text_input("Ask your question:", placeholder="e.g. What is the function of mitochondria?")
    submitted = st.form_submit_button("Ask")

API_URL = "http://localhost:2000/predict"  

if submitted and question:
    with st.spinner("Thinking..."):
        try:
            response = requests.post(API_URL, json={"question": question})
            answer = response.json().get("answer", "Sorry, no answer found.")
        except Exception as e:
            answer = f"⚠️ Error: {e}"

    st.markdown(f"**🧑 You:** {question}")
    st.markdown(
        f"<div style='background-color: #f1f1f1; padding: 15px; border-radius: 10px;'><strong>🧬 BioRAG:</strong><br>{answer}</div>",
        unsafe_allow_html=True
    )

