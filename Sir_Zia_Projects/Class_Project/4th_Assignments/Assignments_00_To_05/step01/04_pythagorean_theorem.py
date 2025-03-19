# "Pythagorean Theorem"
# Concept: math.sqrt(), Exponents
# Formula: hypotenuse = sqrt(a² + b²)

import math

def main():
    a = float(input("Enter the length of AB: "))
    b = float(input("Enter the length of AC: "))
    c = math.sqrt(a**2 + b**2)
    print("The length of BC (the hypotenuse) is:", c)

if __name__ == '__main__':
    main()
