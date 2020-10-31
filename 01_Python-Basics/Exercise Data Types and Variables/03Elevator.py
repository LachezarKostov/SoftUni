import math

people = int(input())
capacity = int(input())

courses = people / capacity

print(math.ceil(courses))

