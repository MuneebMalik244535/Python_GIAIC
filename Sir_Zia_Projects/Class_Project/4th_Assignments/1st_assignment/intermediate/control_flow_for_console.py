import random

NUM_ROUNDS = 5  # ✅ Number of rounds to play

def play_round():
    """Plays one round of the High-Low game."""
    player_number = random.randint(1, 100)  # 🎲 Player's random number
    computer_number = random.randint(1, 100)  # 🎲 Computer's random number

    print(f"\n🎲 Your number is: {player_number}")
    
    # ✅ Get player's guess with validation
    while True:
        guess = input("📢 Will the computer's number be 'higher' or 'lower'? ").strip().lower()
        if guess in ["higher", "lower"]:
            break
        print("⚠️ Invalid input! Please type 'higher' or 'lower'.")

    # ✅ Determine if the player won the round
    if (guess == "higher" and computer_number > player_number) or (guess == "lower" and computer_number < player_number):
        print(f"✅ Correct! Computer's number was {computer_number}.")
        return 1  # ✅ Player wins the round
    elif player_number == computer_number:
        print(f"😲 It's a tie! Both numbers are {player_number}.")
        return 0  # ✅ No points
    else:
        print(f"❌ Wrong! Computer's number was {computer_number}.")
        return 0  # ✅ Player loses the round

def main():
    print("🎮 Welcome to the High-Low Game!")
    print(f"🔢 You will play {NUM_ROUNDS} rounds. Try to guess correctly!\n")

    score = 0  # ✅ Player's score tracker

    for _ in range(NUM_ROUNDS):
        score += play_round()

    # ✅ Final Results
    print("\n🏆 Game Over!")
    print(f"🎯 Your final score: {score}/{NUM_ROUNDS}")

    # ✅ Final message based on performance
    if score == NUM_ROUNDS:
        print("🌟 Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("👏 Good job, you played well!")
    else:
        print("😞 Better luck next time!")

if __name__ == '__main__':
    main()
