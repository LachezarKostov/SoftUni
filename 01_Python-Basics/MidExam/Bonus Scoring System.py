from math import ceil

num_of_students = int(input())
count_of_lectures = int(input())
initial_bonus = int(input())
max_attendances = 0

for _ in range(num_of_students):
    attendances = int(input())
    if attendances > max_attendances:
        max_attendances = attendances

if count_of_lectures != 0:
    max_bonus = max_attendances / count_of_lectures * (5 + initial_bonus)
    max_bonus = ceil(max_bonus)
else:
    max_bonus = 0

print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {max_attendances} lectures.")


