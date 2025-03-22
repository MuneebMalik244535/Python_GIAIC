import streamlit as st
import random

words = ["python", "streamlit", "hangman"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

st.title("📝 Hangman Game")
st.write(" ".join(guessed))
letter = st.text_input("Guess a letter: ").lower()

if letter:
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        attempts -= 1

    if "_" not in guessed:
        st.success(f"🎉 You won! The word was {word}")
    elif attempts == 0:
        st.error(f"❌ You lost! The word was {word}")

st.write(f"Attempts left: {attempts}")
