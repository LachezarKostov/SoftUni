from math import sqrt

class Point:

    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, new_x: int) -> None:
        self.x = new_x

    def set_y(self, new_y: int) -> None:
        self.y = new_y

    def distance(self, x: int, y: int) -> float:
        del_x = abs(self.x - x)
        del_y = abs(self.y - y)

        return sqrt(del_x **2 + del_y ** 2)

p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))
