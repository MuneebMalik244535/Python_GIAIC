class Product:
    def __init__(self):
        self._price = 0

    @property
    def price(self): return self._price

    @price.setter
    def price(self, value): self._price = value

    @price.deleter
    def price(self): del self._price

p = Product()
p.price = 100
print(p.price)
del p.price
