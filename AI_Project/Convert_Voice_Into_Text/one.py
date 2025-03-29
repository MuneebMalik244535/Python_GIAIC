import streamlit as st
import speech_recognition as sr

def get_voice_input(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        st.info("Processing audio file...")
        audio = recognizer.record(source)  # Read the entire file
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, couldn't understand."
        except sr.RequestError:
            return "API unavailable."

st.title("🎤 Voice-Activated Form Submission")

# Upload an audio file instead of using the microphone
audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

if audio_file is not None:
    with open("temp_audio.wav", "wb") as f:
        f.write(audio_file.read())
    transcript = get_voice_input("temp_audio.wav")
    st.text_area("Transcription:", value=transcript, height=150)

st.success("✅ Ready to process audio!")
