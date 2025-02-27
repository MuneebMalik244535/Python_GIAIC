import streamlit as st 
from gtts import gTTS
import os
st.title("AI Text To Speech Converter")
user_Input_box = st.text_area("Write Your Words")
multiple_Languages = st.selectbox("Select Your Language",["en","fr","de","es"])
if st.button("Convert Into Speech"):
    if user_Input_box:
      tts = gTTS(text=user_Input_box,lang=multiple_Languages,slow=False)
      tts.save("speech.mp3")
      st.audio("speech.mp3")