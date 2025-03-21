maximum_height = 50
def main():
     while True:
        user = input("Enter Your Height : ")
        if user == "":
            print("Good Bye")
            break
        try :
            user_con = float(user)
            if user_con >= maximum_height:
                print("You are Tall to enough for Ride")
            else:
                print("You are not Tall Please Try may ne Next Year")        
        except ValueError:
            print("Please Input Your Height")

            
if __name__ == '__main__':
    main()
        