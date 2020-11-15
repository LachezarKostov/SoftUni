from project.product import Product


class Beverage(Product):
    _milliliters: float

    def __init__(self, name, price, milliliters):
        super().__init__(name, price)
        self._milliliters = milliliters


    @property
    def milliliters(self):
        return self._milliliters

    @milliliters.setter
    def milliliters(self, val):
        self._milliliters = val
