import streamlit as st
import google.generativeai as genai
import fitz  # PyMuPDF for PDF extraction

# Configure Gemini API
genai.configure(api_key="AIzaSyD0H_WeVN3k4Hxae1RNDp_hFBEiG4zbrTc")

# Extract text from PDF
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    return text

# Summarize or extract specific content
def process_text(text, user_input):
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(f"{user_input}: {text[:2000]}")
    return response.text

# Streamlit UI
st.title("📂 AI PDF Processor")

# File Upload
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    st.success("✅ PDF uploaded successfully!")
    pdf_text = extract_text_from_pdf(uploaded_file)

    # User Input
    user_request = st.text_area("Enter your request (e.g., Summarize, Extract Key Points, Find Topic X):")

    if st.button("Process"):
        if user_request:
            output = process_text(pdf_text, user_request)
            st.subheader("📝 AI-Generated Response:")
            st.write(output)
        else:
            st.warning("⚠️ Please enter a request before processing!")
