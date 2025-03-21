def main():
    list = []
    user_input = input("Enter : ")
    while user_input :
        print("But if you want to stop press just enter without writing any word")
        if user_input.isdigit():
            list.append(int(user_input))
        elif user_input.replace(".", "").isdigit():
            list.append(float(user_input))
        else :
            list.append(user_input)  
        user_input = input("Write Anything : ")
    print("Here is your list :",list)

if __name__ == '__main__':
    main()
                      
    