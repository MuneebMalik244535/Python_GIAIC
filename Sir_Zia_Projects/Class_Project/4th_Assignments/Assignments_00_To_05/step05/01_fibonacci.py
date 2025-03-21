MAX_TERM_VALUE = 10000  # ✅ Maximum value limit for Fibonacci sequence

def main():
    curr_term, next_term = 0, 1  # ✅ Initialize first two Fibonacci numbers

    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")  # ✅ Print numbers on same line
        curr_term, next_term = next_term, curr_term + next_term  # ✅ Swap values

if __name__ == '__main__':
    main()
