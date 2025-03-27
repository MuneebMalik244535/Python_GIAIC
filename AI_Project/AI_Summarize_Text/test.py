import streamlit as st
import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Streamlit UI
st.title("🎙️ AI Voice Notes to Text Converter")

st.write("Press the button and speak. AI will convert your voice into text!")

if st.button("Start Recording"):
    with sr.Microphone() as source:
        st.write("Listening... Speak now!")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
        audio = recognizer.listen(source)  # Listen to user voice
        
        try:
            text = recognizer.recognize_google(audio)  # Convert speech to text
            st.subheader("📝 Converted Text:")
            st.write(text)

            # Option to download the text file
            st.download_button("Download Notes", text, file_name="voice_notes.txt")
        
        except Exception as e:
            st.error("Sorry, I couldn't understand. Try again!")

