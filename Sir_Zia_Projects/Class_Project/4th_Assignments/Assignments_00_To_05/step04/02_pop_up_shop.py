def main():
    fruits_variety = {
         'apple': 1.5, 
        'durian': 50, 
        'jackfruit': 80, 
        'kiwi': 1, 
        'rambutan': 1.5, 
        'mango': 5
    }
    total_cost = 0
    for fruits, price in fruits_variety.items():
        while True:
            try:
                user_input = int(input(f"How many Fruits : {fruits_variety} Do you want to Purchase : "))
                if user_input < 0:
                    print("Please enter a positive number")
                else:
                     break
            except ValueError:
                print("⚠️ Invalid input! Please enter a valid number.")
        
        total_cost += price * user_input
        print(f"\n💰 Your total is **${total_cost:.2f}**")

if __name__ == '__main__':
    main()
               
         