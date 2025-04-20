import streamlit as st
from gemini_helper import generate_questions

st.set_page_config(page_title="CodeMate AI", layout="centered")

st.title("🤖 CodeMate AI – Coding MCQ Generator")

uploaded_file = st.file_uploader("📁 Upload your coding file", type=["py", "js", "cpp", "java", "txt"])

if uploaded_file is not None:
    file_content = uploaded_file.read().decode("utf-8")
    st.code(file_content[:500], language="python")  # show sample

    if st.button("🔍 Generate Questions"):
        with st.spinner("Generating using Gemini..."):
            result = generate_questions(file_content)

        st.success("✅ Questions Generated!")

        st.subheader("📘 Multiple Choice Questions")
        st.markdown(result.get("mcqs", "No MCQs found"))

