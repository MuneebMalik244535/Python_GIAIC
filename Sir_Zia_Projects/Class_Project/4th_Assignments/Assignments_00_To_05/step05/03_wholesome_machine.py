AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    while True:
        user_input = input(f"🔹 Please type the following affirmation:\n➡️ {AFFIRMATION}\n")

        if user_input == AFFIRMATION:
            print("✅ That's right! :)")
            break  # ✅ Stop loop if input is correct
        else:
            print("❌ That was not the affirmation. Try again!\n")

if __name__ == '__main__':
    main()
