from math import ceil

count = 0

employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())

students = int(input())

employees = (employee_1 + employee_2 + employee_3)

hours = ceil(students / employees)

brakes = hours // 3

hours += brakes

if hours % 4 == 0 and hours != 0:
    hours -= 1

print(f"Time needed: {hours}h.")
