import google.generativeai as genai

genai.configure(api_key="AIzaSyD0H_WeVN3k4Hxae1RNDp_hFBEiG4zbrTc")

def get_gemini_reply(user_input, topic="Free Talk"):
    prompt = f"You are an English speaking partner. Topic: {topic}. User said: '{user_input}'. Respond as a friendly tutor."
    model = genai.GenerativeModel("gemini-1.5-pro")
    chat = model.start_chat()
    response = chat.send_message(prompt)
    return response.text

def get_grammar_feedback(user_input):
    prompt = f"Give grammar feedback on this sentence: '{user_input}'. Suggest the correction and explain if needed."
    model = genai.GenerativeModel("gemini-1.5-pro")
    chat = model.start_chat()
    response = chat.send_message(prompt)
    return response.text
