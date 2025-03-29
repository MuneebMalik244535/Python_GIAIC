import streamlit as st
import speech_recognition as sr

# Function to capture voice and convert to text
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

# Streamlit UI
st.title("🎤 Voice-Activated Form Submission")

# Name field with voice input
if st.button("🎙 Speak Your Name"):
    name = get_voice_input()
    st.text_input("Your Name:", value=name, key="name")

# Feedback field with voice input
if st.button("🎙 Speak Your Feedback"):
    feedback = get_voice_input()
    st.text_area("Your Feedback:", value=feedback, key="feedback")

# Submit button
if st.button("Submit"):
    st.success("✅ Form Submitted Successfully!")          
