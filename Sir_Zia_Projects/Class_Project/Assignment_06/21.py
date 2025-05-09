class Countdown:
    def __init__(self, start):
        self.num = start

    def __iter__(self): return self

    def __next__(self):
        if self.num < 0: raise StopIteration
        val = self.num
        self.num -= 1
        return val

for i in Countdown(5):
    print(i)
