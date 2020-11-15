from project.car import Car
from project.family_car import FamilyCar
from project.vehicle import Vehicle


print(Vehicle.__mro__)
print(FamilyCar.__mro__)


c = Car(30, 50)
print(c.drive(10))
print(c.fuel)
