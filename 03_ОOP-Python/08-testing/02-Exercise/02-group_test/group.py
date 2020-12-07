class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return self.name + ' ' + self.surname

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __str__(self):
        people_str = ', '.join([str(person) for person in self.people])
        return "Group " + self.name + " with members " + people_str

    def __len__(self):
        return len(self.people)

    def __getitem__(self, index):
        return "Person " + str(index) + ": " + str(self.people[index])

    def __add__(self, other):
        return Group(self.name, self.people + other.people)


# from typing import List
#
# class Person:
#     def __init__(self, name: str, surname: str):
#         self.name = name
#         self.surname = surname
#
#     def __add__(self, other):
#         if not isinstance(other, self.__class__):
#             raise TypeError
#
#         return Person(name=self.name, surname=other.surname)
#
#     def __repr__(self):
#         return self.name + " " + self.surname
#
# class Group:
#     def __init__(self, name: str, people: List[Person]):
#         self.name = name
#         self.people = people
#
#     def __add__(self, other):
#         return Group("TODO", people=self.people + other.people)
#
#     def __len__(self):
#         return len(self.people)
#
#     def __str__(self):
#         all_names = ", ".join([n.__repr__() for n in self.people])
#         return f"Group {self.name} with members {all_names}"
#
#     def __getitem__(self, key):
#         return f"Person {key}: {self.people[key].__repr__()}"

