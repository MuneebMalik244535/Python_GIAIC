import streamlit as st
import os 
from dotenv import load_dotenv
import google.generativeai as genai
from resume_utils import Extract_text

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro")
st.title("AI Resume Analyzer")
upload_file = st.file_uploader("Upload Your Pdf File Here : ")
if upload_file:
    resume_text = Extract_text(upload_file)
    prompt = f"""
    Analyze this resume and provide the following:
    - Summary of the candidate
    - List of key skills
    - Experienced
    - Suggestions for improvement
    - Job role fit (e.g., Frontend, Backend, Data Analyst, etc.)

    Resume:
    {resume_text}
    """
    st.subheader("🧠 Analyzing Resume...")
    response = model.generate_content(prompt)
    st.markdown("✅ Analysis Result:")
    st.write(response.text)

