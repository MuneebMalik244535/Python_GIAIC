import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from youtube_transcript_api.formatters import TextFormatter
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro")

st.title("🎥 YouTube Video Summarizer using AI")

video_url = st.text_input("Enter YouTube video URL:")

def extract_video_id(url):
    if "watch?v=" in url:
        return url.split("watch?v=")[-1][:11]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[-1][:11]
    return None

def get_transcript(video_id):
    try:
        # Try English transcript
        return YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    except:
        try:
            # Try Hindi if English is not available
            return YouTubeTranscriptApi.get_transcript(video_id, languages=['hi'])
        except Exception as e:
            return f"error::{str(e)}"

if st.button("Summarize Video"):
    video_id = extract_video_id(video_url)
    if video_id:
        transcript = get_transcript(video_id)

        if isinstance(transcript, str) and transcript.startswith("error::"):
            st.error(f"❌ {transcript[7:]}")
        else:
            full_text = " ".join([entry['text'] for entry in transcript])
            prompt = f"""
            Summarize the following YouTube video transcript into simple, clear points for a beginner to understand:

            Transcript:
            {full_text}
            """

            st.subheader("🧠 AI Summary")
            response = model.generate_content(prompt)
            st.markdown(response.text)
    else:
        st.warning("⚠️ Invalid YouTube URL!")
