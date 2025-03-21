def Is_Leap_Year(year):
    """Input Your Number and check is it Leap Year """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input("Enter Your Year : "))
def main():
    try :
        if Is_Leap_Year(year):
            print(f"{year} is a leap year")
        else :
            print(f"{year} it is not a leap year")    
    except ValueError :
        print("Please Enter a Valid Number")

if __name__ == '__main__':
    main()
        
    