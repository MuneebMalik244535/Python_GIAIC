C = 299792458  # Speed of Light in m/s

def main():
    mass = float(input("Enter mass in kg: "))
    energy = mass * (C ** 2)
    print("e = m * C^2...")
    print("m =", mass, "kg")
    print("C =", C, "m/s")
    print(energy, "joules of energy!")

if __name__ == '__main__':
    main()
