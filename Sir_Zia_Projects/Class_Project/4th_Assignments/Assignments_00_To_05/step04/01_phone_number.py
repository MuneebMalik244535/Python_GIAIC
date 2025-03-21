def main():
    phone_list = {}
    while True:
        print("\n📖 PHONEBOOK MENU 📖")
        print("1️⃣ Add Contact")
        print("2️⃣ View All Contacts")
        print("3️⃣ Search Contact")
        print("4️⃣ Exit")
        choice = input("Please select one option (1-4) : " )
        if choice == "1":
            number = int(input("Enter Your Phone Number"))
            name = str(input("Enter Your Name"))
            phone_list[name] = number
            print(f"✅ Contact saved: {name} -> {number}")
        elif choice == "2":
              if phone_list:
               for name , number in phone_list.items():
                print(f"{name} => {number}")
              else :
                  print("Your phone list is empty") 
        elif choice == "3":
                name = input("🔍 Enter Name to Search: ")
                print(f"📞 {name}'s Number: {phone_list.get(name, '❌ Not Found')}")

        elif choice == "4":
            print("👋 Goodbye! Have a great day!")
            break  # ✅ Program exits

        else:
            print("⚠️ Invalid option! Please enter 1-4.")

if __name__ == '__main__':
    main()           
    
    
    
    