n = int(input())
students = {}

for i in range(n):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = []

    students[student_name].append(grade)

student_average_grade = {}

for key, value in students.items():
    average = sum(value) / len(value)

    if average < 4.5:
        continue

    student_average_grade[key] = average

student_average_grade = dict(sorted(student_average_grade.items(), key = lambda x: x[1], reverse= True))

for students, avrg in student_average_grade.items():
    print(f"{students} -> {avrg:.2f}")

