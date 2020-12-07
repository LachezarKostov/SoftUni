from venicle import Car, Truck
import unittest


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car(100, 3)

    def test_car_drive_with_not_less_fuel(self):
        self.car.drive(40)
        self.assertEqual(self.car.fuel_quantity, 100)

    def test_car_drive_with_fuel(self):
        self.car.drive(10)
        self.assertEqual(self.car.fuel_quantity, 61)

    def test_car_add_fuel_when_refueled(self):
        self.car.refuel(50)
        self.assertEqual(self.car.fuel_quantity, 150)


class TestTruck(unittest.TestCase):
    def setUp(self):
        self.truck = Truck(100, 3)

    def test_truck_drive_with_not_less_fuel(self):
        self.truck.drive(30)
        self.assertEqual(self.truck.fuel_quantity, 100)

    def test_truck_drive_with_fuel(self):
        self.truck.drive(15)
        self.assertEqual(self.truck.fuel_quantity, 31)

    def test_truck_add_fuel_when_refuel(self):
        self.truck.refuel(20)
        self.assertEqual(self.truck.fuel_quantity, 119)


if __name__ == "__main__":
    unittest.main()
