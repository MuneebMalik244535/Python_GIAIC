def Sum_Of_All (numbers):
    """Takes in a list of numbers and returns the sum of those numbers."""
    add = 0
    for i in numbers:
        add += i
    return add

def Main():
    numbers_list = [1,2,3,4,5]
    sum = Sum_Of_All(numbers_list)
    print(sum)
 
if __name__ == '__main__':
    Main()
        
        
    