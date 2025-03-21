

Max_Value : int = 3


def Shorten(lst,Max_Value):
    while len(lst) > Max_Value:
        delete_elem = lst.pop()
        print(delete_elem)
        

def Get_list():
    lst = []
    elem = input("Write which You want or press enter having not written any thing for stopping")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst                 
    

def main():
    user_list = Get_list()
    Shorten(user_list,Max_Value)
    


        
if __name__ == '__main__':
    main()
        