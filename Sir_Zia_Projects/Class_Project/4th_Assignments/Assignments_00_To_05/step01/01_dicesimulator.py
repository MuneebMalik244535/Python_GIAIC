import random
def Home():
    sides = 6
    one = random.randint(1,sides)
    two = random.randint(1,sides)
    total = one + two
    print("Total of two dice:", total)

def Main():
    die_one = 10
    print("die1 in main() starts as:", die_one)
    Home()
    Home()
    Home()
    print("die1 in main() is:", die_one)

if __name__ == "__main__":
    Main()
    
        