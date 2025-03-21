def get_num(args):
    lst = []
    while True:
        user_input = input("Enter The Number")
        if user_input == "" :
            break
        try:
            convert_num = int(user_input)
            lst.append(user_input)
        except  ValueError :
             print("⚠️ Please enter a valid number!")
    return convert_num         


def count_num(num_list):
    num_dict = {}
    for num in num_list:
        num_dict[num] = num_dict.get(num , 0) + 1 
    return num_dict    

def print_num(num_dict):
    for num , count in num_dict.items():
        print(f"{num} appears {count} times.")


def main():
    user_number = get_num()
    if user_number:
        num_dict = count_num(user_number)
        print_num(num_dict)
    else:
        print("No numbers were entered. Exiting program.")
        

if __name__ == '__main__':
    main()
            
            