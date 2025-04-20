import streamlit as st
from app.scanner import analyze_code
from app.fixer import suggest_fixes
from app.reporter import generate_pdf_report
st.set_page_config(page_title="CyberAI Agent", layout="wide")
st.title("🤖 CyberAI Agent – AI-Powered Vulnerability Scanner & Fixer")

code = st.text_area("Paste your code or config here:", height=300)

if st.button("🔍 Scan for Vulnerabilities"):
    with st.spinner("Analyzing with Gemini..."):
        result = analyze_code(code)
        st.markdown("### 🧪 Vulnerability Report")
        st.write(result)

        st.markdown("### 🛠 Suggested Fixes")
        fix = suggest_fixes(code)
        st.code(fix, language="python")
    report_path = generate_pdf_report(code, result, fix)
    with open(report_path, "rb") as f:
     st.download_button("📄 Download Full Report (PDF)", f, file_name="cyberai_report.pdf")    
