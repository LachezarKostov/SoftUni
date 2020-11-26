from project.animals.birds import Owl, Hen
from project.animals.mammals import Mouse, Dog, Cat, Tiger


def main():
    def test_can_initiate_bird():
        Owl("Buho", weight=2, wing_size=20)
        Hen("Hencho", weight=3, wing_size=30)

        print("test_can_initiate_bird passed")

    def test_can_initiate_mammals():
        Mouse("Goshko", 100, "Pernik")
        Dog("Pencho", 120, "Sofia")
        Cat("Ivanco", 150, "Troian")
        Tiger("Vasko", 50, "Varna")

        print("test_can_initiate_mammals passed")

    test_can_initiate_bird()
    test_can_initiate_mammals()


if __name__ == "__main__":
    main()

# first zero test
import unittest
from project.animals.birds import Owl, Hen
from project.animals.mammals import Mouse, Dog, Cat, Tiger
from project.food import Vegetable, Fruit, Meat, Seed

class WildFarmTests(unittest.TestCase):
    def test_first_zero(self):
        owl = Owl("Pip", 10, 10)
        self.assertEqual(str(owl), "Owl [Pip, 10, 10, 0]")

        self.assertEqual(owl.make_sound(), "Hoot Hoot")
        owl.feed(Meat(4))
        veg = Vegetable(1)
        owl.feed(veg)
        self.assertEqual(owl.feed(veg), "Owl does not eat Vegetable!")
        self.assertEqual(str(owl), "Owl [Pip, 10, 11.0, 4]")

if __name__ == "__main__":
    unittest.main()