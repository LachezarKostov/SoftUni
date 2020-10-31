name = input()

grades_completed = 1
sum_marks = 0
expeled = 0
while grades_completed  <= 12 :

    mark = float(input())

    if mark >= 4 :
        grades_completed += 1
        sum_marks += mark
    else:
        expeled += 1
        if expeled == 2:
            break

avarega_mark = sum_marks / 12

if expeled != 2:
    print(f"{name} graduated. Average grade: {avarega_mark:.2f}")
else:
    print(f"{name} has been excluded at {grades_completed} grade")