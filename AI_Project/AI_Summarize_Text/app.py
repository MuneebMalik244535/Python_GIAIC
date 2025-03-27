import streamlit as st 
import google.generativeai as genai
import fitz

genai.configure(api_key="AIzaSyD0H_WeVN3k4Hxae1RNDp_hFBEiG4zbrTc")
def extraction(pdf):
    docs = fitz.open(stream=pdf.read(), filetype="pdf")
    text = ""
    for page in docs:
        text += page.get_text("text") + "\n"
    return text

def summarize(text):
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(f"Summarize this text in five Sentence : {text[:2000]}") # yahan prompt den jo chahiye apko 
    return response.text

st.title("AI Summarize Text From Pdf")
st.subheader("Browse Your PDF file for extracting the text : ")
uploaded_file = st.file_uploader("Upload You PDF file here : " , type=["pdf"])
if uploaded_file :
    st.success("Successfully Your Files Jas been Browsed")
    pdf_text = extraction(uploaded_file)
    if st.button("Summarize"):
        Summarize_text = summarize(pdf_text)
        st.subheader("🎉 Extracted Text Summary : ")
        st.write(Summarize_text)
            
    
    