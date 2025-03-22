import random

def print_random_numbers():
    print("🎲 Random numbers:", end=" ")
    print(*[random.randint(1, 100) for _ in range(10)])  # ✅ List comprehension for clean code

if __name__ == '__main__':
    print_random_numbers()
