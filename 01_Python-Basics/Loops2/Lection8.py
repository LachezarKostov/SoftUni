name = input()

grades_completed = 1
sum_marks = 0

while grades_completed  <= 12 :

    mark = float(input())

    if mark >= 4 :
        grades_completed += 1
        sum_marks += mark

avarega_mark = sum_marks / 12

print(f"{name} graduated. Average grade: {avarega_mark:.2f}")
