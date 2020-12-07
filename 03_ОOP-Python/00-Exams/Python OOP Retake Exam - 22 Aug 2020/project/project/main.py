from project.appliances.appliance import Appliance
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.alone_old import AloneOld
from project.rooms.alone_young import AloneYoung
from project.rooms.old_couple import OldCouple
from project.rooms.room import Room
from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren
from project.people.child import Child
from project.everland import Everland

everland = Everland()


def test_one():
    young_couple = YoungCouple("Johnsons", 150, 205)

    child_one = Child(5, 1, 2, 1)
    child_two = Child(3, 2)
    young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child_one, child_two)

    everland.add_room(young_couple)
    everland.add_room(young_couple_with_children)

    print(everland.get_monthly_consumptions())
    print(everland.pay())
    print(everland.status())


Appliance(10).get_monthly_expense()
Fridge().get_monthly_expense()
Laptop().get_monthly_expense()
Stove().get_monthly_expense()
TV().get_monthly_expense()
Child(1, 2, 3)
AloneOld("BOB", 2)
AloneYoung("ROB", 2)
OldCouple("Bobby", 1, 2)
Room("Room", 2, 3)
YoungCouple("Pep", 20, 20)
YoungCoupleWithChildren("Bob", 10, 15, Child(1, 2, 3), Child(4, 5, 6))
Everland().add_room(Room("Room", 2, 3))
Everland().get_monthly_consumptions()
Everland().pay()
Everland().status()

if __name__ == "__main__":
    test_one()
