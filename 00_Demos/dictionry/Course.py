line = input()
courses = {}

while line != "end":
    args = line.split(" : ")
    course_name = args[0]
    student_name = args[1]

    if course_name not in courses:
        courses[course_name] = []

    courses[course_name].append(student_name)

    line = input()

sorted_courses = dict(sorted(courses.items(), key=lambda c: -len(c[1])))

for key, value in sorted_courses.items():
    print(f"{key}: {len(value)}")
    for student_name in sorted(value):
        print(f"-- {student_name}")
