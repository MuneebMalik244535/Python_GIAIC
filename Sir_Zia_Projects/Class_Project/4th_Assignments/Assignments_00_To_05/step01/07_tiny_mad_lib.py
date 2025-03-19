SENTENCE_START = "Panaversity is fun. I learned to program and used Python to make my "

def main():
    adjective = input("Please type an adjective: ")
    noun = input("Please type a noun: ")
    verb = input("Please type a verb: ")

    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

if __name__ == '__main__':
    main()
