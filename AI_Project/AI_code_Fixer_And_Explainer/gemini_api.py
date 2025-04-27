import google.generativeai as genai
import os
from dotenv import load_dotenv


genai.configure(api_key="AIzaSyD0H_WeVN3k4Hxae1RNDp_hFBEiG4zbrTc")

def get_fixed_code(code, explain=False):
    with open("prompt_template.txt", "r") as f:
        prompt = f.read()

    prompt = prompt.replace("<CODE_HERE>", code)

    if not explain:
        prompt = prompt.split("3.")[0] + f"\n\nHere is the code:\n{code}"

    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text
