import streamlit as st
from gemini_api import get_gemini_reply, get_grammar_feedback
from speech_recognition import Recognizer, Microphone

st.set_page_config(page_title="AI English Speaking Partner")
st.title("🎙️ Speak English with AI Partner")

topic = st.selectbox("Choose a topic", ["Free Talk", "Travel", "Job Interview", "Daily Life"])

if st.button("🎤 Speak Now"):
    r = Recognizer()
    with Microphone() as source:
        st.info("Listening... Please speak.")
        audio = r.listen(source)
        try:
            user_input = r.recognize_google(audio)
            st.success(f"🗣️ You said: {user_input}")
            
            ai_response = get_gemini_reply(user_input, topic)
            feedback = get_grammar_feedback(user_input)

            st.markdown("**🤖 AI Reply:**")
            st.write(ai_response)

            st.markdown("**🧠 Grammar Feedback:**")
            st.info(feedback)

        except Exception as e:
            st.error(f"Error: {e}")
