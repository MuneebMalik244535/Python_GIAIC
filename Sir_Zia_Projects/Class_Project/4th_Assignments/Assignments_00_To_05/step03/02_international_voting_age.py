# ✅ Voting age dictionary
voting_ages = {
    "Peturksbouipo": 16,
    "Stanlau": 25,
    "Mayengua": 48
}

def main():
    try:
        user_age = int(input("Enter Your Age for Casting The Vote: "))  # ✅ User input as integer

        # ✅ Loop through the dictionary to check voting eligibility
        for country, age in voting_ages.items():
            status = "can" if user_age >= age else "cannot"  # ✅ Conditional check in one line
            print(f"You {status} vote in {country} where the voting age is {age}.")  

    except ValueError:
        print("⚠️ Please enter a valid number!")

if __name__ == '__main__':
    main()
