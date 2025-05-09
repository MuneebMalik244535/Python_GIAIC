class Engine:
    def start(self):
        print("Engine starting...")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def run(self):
        self.engine.start()

e = Engine()
c = Car(e)
c.run()
