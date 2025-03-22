def double_number():
    try:
        curr_value = int(input(" Enter a number: "))
        if curr_value < 1:
            print("⚠️ Please enter a positive number.")
            return

        while curr_value < 100: 
            curr_value *= 2  
            print(curr_value, end=" ") 
        print()  

    except ValueError:
        print(" Invalid input! Please enter a valid number")

if __name__ == '__main__':
    double_number()
