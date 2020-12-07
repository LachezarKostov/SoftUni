from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel, consumption):
        self.fuel_quantity    = fuel
        self.fuel_consumption = consumption

    @abstractmethod
    def refuel(self, fuel: int):
        pass

    @abstractmethod
    def drive(self, distance):
        pass


class Car(Vehicle):
    def refuel(self, fuel: int):
        self.fuel_quantity += fuel

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + 0.9)
        if self.fuel_quantity < fuel_needed:
            return
        self.fuel_quantity -= fuel_needed


class Truck(Vehicle):
    def refuel(self, fuel: int):
        self.fuel_quantity += (fuel * 0.95)

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + 1.6)
        if self.fuel_quantity < fuel_needed:
            return
        self.fuel_quantity -= fuel_needed


