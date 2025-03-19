# Concept: Integer Division = //, Modulus Operator = %
def main():
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))

    Int_devide = dividend // divisor  # Integer division
    remainder = dividend % divisor  # Modulus operator

    print(f"The result of this division is {Int_devide} with a remainder of {remainder}")

if __name__ == '__main__':
    main()
