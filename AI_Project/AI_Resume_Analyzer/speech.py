import speech_recognition as sr
import streamlit as st

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        with st.spinner("Listening... 🎤"):
            audio = r.listen(source)
        try:
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "API error. Try again."
