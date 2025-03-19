def Main():
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5.0 / 9.0
    print(f"Temperature {f}F = {c:.2f}C")

if __name__ == "__main__":
    Main()    
    