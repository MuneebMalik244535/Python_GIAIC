import random

def guess_number():
    secret_number = random.randint(1, 99) 
    attempts = 0

    print("I'm thinking of a number between 1 and 99...")
    
    while True:
        try:
            guess = int(input(" Enter your guess: "))  
            attempts += 1

            if guess < secret_number:
                print("⬆ Too low! Try again.")
            elif guess > secret_number:
                print(" Too high! Try again.")
            else:
                print(f" Correct! The number was {secret_number} in {attempts} attempts.")
                break 

        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == '__main__':
    guess_number()
