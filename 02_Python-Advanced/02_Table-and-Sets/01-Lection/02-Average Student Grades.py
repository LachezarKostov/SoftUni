import math
def inout_to_list(count):
    input_lines = []
    for _ in range(count):
        input_lines.append(input())

    return input_lines


def count_numbers(values):
    students_mark = {}

    for value in values:
        student, mark = value.split(" ")
        if student not in students_mark:
            students_mark[student] = []
        students_mark[student].append(mark)

    return students_mark


def avg(values):
    return sum(values) / len(values)


def print_result(students_mark):
    for (student_name, marks) in students_mark.items():
        avg_mark = avg(float(marks))
        marks_string = " ".join(f"{mark:2f}" for mark in marks)
        print(f"{student_name} -> {marks_string} (avg: {avg_mark:.2f})")


print_result(count_numbers(inout_to_list(int(input()))))
