class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Objects created: {cls.count}")

Counter()
Counter()
Counter.show_count()
