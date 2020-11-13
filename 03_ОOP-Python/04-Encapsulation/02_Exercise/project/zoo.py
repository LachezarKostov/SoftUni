from project.animal_base import AnimalBase
from project.employee_base import EmployeeBase
from project.lion import Lion
from project.tiger import Tiger
from project.cheetah import Cheetah
from project.vet import Vet
from project.keeper import Keeper
from project.caretaker import Caretaker


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal: AnimalBase, price: int):
        if self.__budget >= price and self.__animal_capacity > 0:
            self.animals.append(animal)
            self.__budget -= price
            self.__animal_capacity -= 1
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity > 0:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: EmployeeBase):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)

            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        prev_number_workers = len(self.workers)
        self.workers = [
            worker
            for worker in self.workers
            if worker_name != worker.name
        ]
        next_number_of_workers = len(self.workers)

        if prev_number_workers > next_number_of_workers:
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"


    def pay_workers(self):
        total_due = sum([w.salary for w in self.workers])
        if self.__budget >= total_due:
            self.__budget -= total_due
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_due = sum([a.get_needs() for a in self.animals])
        if self.__budget >= total_due:
            self.__budget -= total_due
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        total_animal_count = len(self.animals)
        lions = [a.__repr__() for a in self.animals if isinstance(a, Lion)]
        tigers = [a.__repr__() for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [a.__repr__() for a in self.animals if isinstance(a, Cheetah)]

        NEW_LINE = "\n"

        return f"""You have {total_animal_count} animals
----- {len(lions)} Lions:
{NEW_LINE.join(lions)}
----- {len(tigers)} Tigers:
{NEW_LINE.join(tigers)}
----- {len(cheetahs)} Cheetahs:
{NEW_LINE.join(cheetahs)}"""

    def workers_status(self):
        total_workers_count = len(self.workers)
        vets = [a.__repr__() for a in self.workers if isinstance(a, Vet)]
        keepers = [a.__repr__() for a in self.workers if isinstance(a, Keeper)]
        caretakers = [a.__repr__() for a in self.workers if isinstance(a, Caretaker)]

        NEW_LINE = "\n"

        return f"""You have {total_workers_count} workers
----- {len(keepers)} Keepers:
{NEW_LINE.join(keepers)}
----- {len(caretakers)} Caretakers:
{NEW_LINE.join(caretakers)}
----- {len(vets)} Vets:
{NEW_LINE.join(vets)}"""
