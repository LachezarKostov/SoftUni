
count = int(input())
name = input()
all_grade = 0
num = 0


while name != "Finish":
    grade = 0
    sum_grade = 0
    for i in range(1, count+1):
        grade = float(input())
        sum_grade += grade
        all_grade += grade
        num += 1
    print(f"{name} - {sum_grade/count:.2f}.")

    name = input()

print(f"Student's final assessment is {all_grade/num:.2f}.")






