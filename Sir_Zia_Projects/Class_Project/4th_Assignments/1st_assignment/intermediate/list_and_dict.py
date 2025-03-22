def main():
    fruits = ["apple", "banana", "orange", "grape", "pineapple"]  # 🥭 A list of fruits
    print(f"\n🍏 Current List: {fruits}")

    while True:
        print("\n📜 Choose an option:\n1️⃣ Access Item\n2️⃣ Change Item\n3️⃣ Show Part of List\n4️⃣ Exit")
        choice = input("Enter choice (1-4): ")

        if choice == "1":  # Access
            index = int(input("Enter index (0-4): "))
            if 0 <= index < len(fruits):
                print(f"👉 The item is: {fruits[index]}")
            else:
                print("⚠️ Invalid index!")

        elif choice == "2":  # Modify
            index = int(input("Enter index (0-4): "))
            if 0 <= index < len(fruits):
                new_value = input("Enter new item: ")
                fruits[index] = new_value
                print(f"✅ Updated List: {fruits}")
            else:
                print("⚠️ Invalid index!")

        elif choice == "3":  # Slice
            start = int(input("Start index (0-4): "))
            end = int(input("End index (1-5): "))
            if 0 <= start < end <= len(fruits):
                print(f"📌 List slice: {fruits[start:end]}")
            else:
                print("⚠️ Invalid range!")

        elif choice == "4":  # Exit
            print("👋 Goodbye!")
            break

        else:
            print("⚠️ Please choose 1-4.")

if __name__ == "__main__":
    main()
