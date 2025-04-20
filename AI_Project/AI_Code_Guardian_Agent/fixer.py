import os
import google.generativeai as genai


genai.configure(api_key="AIzaSyD0H_WeVN3k4Hxae1RNDp_hFBEiG4zbrTc")  # for direct test

model = genai.GenerativeModel("gemini-1.5-pro")

def suggest_fixes(code):
    prompt = f"""
You are an AI security fixer.

Based on the following code, suggest improved secure version with best practices:

{code}
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error: {e}"
