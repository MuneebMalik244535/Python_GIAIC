import streamlit as st
import google.generativeai as genai
from resume_utils import Extract_text

# Direct API key use karo
genai.configure(api_key="AIzaSyD0H_WeVN3k4Hxae1RNDp_hFBEiG4zbrTc")

# Streamlit App Title
st.title("AI Resume Analyzer")

# Upload Resume
upload_file = st.file_uploader("Upload Your Pdf File Here : ")

# Process if file is uploaded
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
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
    
    st.markdown("✅ Analysis Result:")
    st.write(response.text)
