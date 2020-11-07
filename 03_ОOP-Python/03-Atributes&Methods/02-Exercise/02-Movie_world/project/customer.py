from typing import List
from project.dvd import DVD


class Customer:
    name: str
    age: int
    id: int
    rented_dvds = List[DVD]

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    def __repr__(self) -> str:
        dvd_name = ', '.join(d.name for d in self.rented_dvds)
        return f"{self.id}: {self.name} of age {self.age} has " \
               f"{len(self.rented_dvds)} rented DVD's ({dvd_name})"

    def has_dvd(self, dvd: DVD):
        return dvd in self.rented_dvds

    def add_dvd(self, dvd: DVD):
        self.rented_dvds.append(dvd)

    def remove_dvd(self, dvd: DVD):
        self.rented_dvds.remove(dvd)
