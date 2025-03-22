import random

def guess_number():
    print("🎯 Think of a number between 1 and 100.")

    low, high = 1, 100

    while True:
        guess = random.randint(low, high)  # 🔥 Randomly guess a number
        print(f"🤖 Is your number {guess}?")

        feedback = input("Type 'low' (Too Low), 'high' (Too High), or 'correct': ").strip().lower()

        if feedback == "low":
            low = guess + 1
        elif feedback == "high":
            high = guess - 1
        elif feedback == "correct":
            print(f"🎉 Yay! The computer guessed your number {guess}!")
            break
        else:
            print("⚠️ Invalid input. Please type 'low', 'high', or 'correct'.")

guess_number()
