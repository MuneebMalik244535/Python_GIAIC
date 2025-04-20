import os
import google.generativeai as genai


genai.configure(api_key="AIzaSyD0H_WeVN3k4Hxae1RNDp_hFBEiG4zbrTc") 

model = genai.GenerativeModel("gemini-1.5-pro")

def analyze_code(code, language="general"):
    prompt = f"""
You are a cybersecurity expert AI.

Analyze the following {language} code or configuration for any vulnerabilities.
Be detailed and explain potential threats:

{code}
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error: {e}"
