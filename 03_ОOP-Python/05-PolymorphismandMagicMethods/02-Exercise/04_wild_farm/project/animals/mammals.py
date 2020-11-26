from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit


class Mouse(Mammal):
    _FOOD_PREFERENCES = (Fruit, Vegetable)
    _WEIGH_GAIN = 0.10

    def make_sound(self) -> str:
        return "Squeak"


class Dog(Mammal):
    _FOOD_PREFERENCES = (Meat,)
    _WEIGH_GAIN = 0.40

    def make_sound(self) -> str:
        return "Woof!"


class Cat(Mammal):

    _FOOD_PREFERENCES = (Vegetable, Meat)
    _WEIGH_GAIN = 0.30

    def make_sound(self) -> str:
        return "Meow"


class Tiger(Mammal):
    _FOOD_PREFERENCES = (Meat,)
    _WEIGH_GAIN = 1.00

    def make_sound(self) -> str:
        return "ROAR!!!"
