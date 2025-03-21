import random
import streamlit as st

def guess_game_cli():
    """✅ CLI (Terminal) Mode"""
    secret_number = random.randint(1, 99)
    print("🤖 I am thinking of a number between 1 and 99...")

    while True:
        try:
            guess = int(input("🎯 Enter a guess: "))
            if guess < 1 or guess > 99:
                print("⚠️ Please enter a number between 1 and 99!")
                continue
            if guess < secret_number:
                print("📉 Your guess is too low!")
            elif guess > secret_number:
                print("📈 Your guess is too high!")
            else:
                print(f"🎉 Congrats! The number was: {secret_number}")
                break
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

def guess_game_streamlit():
    """✅ Streamlit Mode"""
    st.title("🎯 Guess My Number Game")
    st.write("🤖 I am thinking of a number between 1 and 99...")
    
    if "secret_number" not in st.session_state:
        st.session_state.secret_number = random.randint(1, 99)
    
    guess = st.number_input("Enter a guess:", min_value=1, max_value=99, step=1, format="%d")

    if st.button("Submit Guess"):
        if guess < st.session_state.secret_number:
            st.warning("📉 Your guess is too low!")
        elif guess > st.session_state.secret_number:
            st.warning("📈 Your guess is too high!")
        else:
            st.success(f"🎉 Congrats! The number was: {st.session_state.secret_number}")
            st.session_state.secret_number = random.randint(1, 99)  # Reset game

def main():
    mode = input("Choose mode (CLI or Streamlit): ").strip().lower()
    if mode == "cli":
        guess_game_cli()
    elif mode == "streamlit":
        st.set_page_config(page_title="Guess My Number", layout="centered")
        guess_game_streamlit()
    else:
        print("⚠️ Invalid mode! Please choose 'CLI' or 'Streamlit'.")

if __name__ == '__main__':
    main()
