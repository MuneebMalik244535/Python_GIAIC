import streamlit as st 
import google.generativeai as genai
genai.configure(api_key="AIzaSyD0H_WeVN3k4Hxae1RNDp_hFBEiG4zbrTc")
model = genai.GenerativeModel("gemini-1.5-pro")
st.title("AI Helpful Assistant")
st.subheader("Enter Your Prompt And Get Answer")
user_input = st.text_input("Write Here")
if user_input:
    prompt = f""" You are a Helpfull AI Assistant like AI assistant,
    you should give answer according to the Queries and Act like best friend with friendly reaction,
    user Asked : {user_input}
    """
    response = model.generate_content(prompt)
    st.success("Here is Your Answer")
    st.write(response.text)