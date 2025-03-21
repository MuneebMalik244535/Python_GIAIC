def Last_Number(lst):
    return lst[-1]  # ✅ Last element return karna

def Get_list():
    lst = []  # ✅ Empty list create karna
    user_input = input("Enter Your Text here: ")
    
    while user_input != "":
        lst.append(user_input)
        user_input = input("Enter Your Text here: ")
    
    return lst  # ✅ Correct return statement

def Main():
    user_list = Get_list()  # ✅ 'list' ki jagah 'user_list' use kiya
    print("Last element:", Last_Number(user_list))  # ✅ Last element print karna

if __name__ == '__main__':
    Main()
