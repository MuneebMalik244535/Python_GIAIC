import streamlit as st
import speech_recognition as sr

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Speak now!")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, couldn't understand."
        except sr.RequestError:
            return "API unavailable."

st.title("🎤 Voice-Activated Form Submission")

if st.button("🎙 Speak Your Name"):
    st.warning("Voice input is not supported on Streamlit Cloud.")
