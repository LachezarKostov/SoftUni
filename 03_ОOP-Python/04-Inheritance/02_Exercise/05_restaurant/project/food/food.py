from project.product import Product


class Food(Product):
    _grams: float

    def __init__(self, name, price, grams):
        self._grams = grams
        super().__init__(name, price)

    @property
    def grams(self):
        return self._grams

    @grams.setter
    def grams(self, val):
        self._grams = val



