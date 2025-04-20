import google.generativeai as genai
import os

# Add your Gemini API Key
genai.configure(api_key="AIzaSyBDPoqkFJIDIv0QcCi5MHA8WRv3nCI5imc")

def generate_questions(code):
    model = genai.GenerativeModel("gemini-1.5-pro")

    prompt = f"""
    You're an expert Python instructor.
    Based on the following code, generate:

    1. 100 Multiple Choice Questions dont compromise for giving any mcqs i want 100 thats it i dont want to listen that you are not giving me fully 100 mcqs or less than 100 (with 4 options each and correct answer marked)
    2. 20 Short answer questions (about logic/functions/modules used)
    3. You Should Explain Each and Every mcqs and short Question Answer in Roman English Thats means how to solve it and make us understand about answer in just 2 lines in very easy and friendly way 
    4. Each mcqs and question should be number wise like(1,2,3,4.....)
    5. Each Mcqs Section must have some space from next question 
    6. mcqs choose option should be number wise like(i,ii,iii,iv.....)

    Code:
    {code}
    """

    response = model.generate_content(prompt)
    return {
        "mcqs": response.text.split("Short answer questions:")[0].strip(),
        "short": response.text.split("Short answer questions:")[-1].strip()
    }
