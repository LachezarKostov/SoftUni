max_bad = int(input())
stop = False
count = 0
num_tasks = 0
bad_count = 0
last_task = ""
grade_add = 0

while True:
    task = input()

    if task != "Enough":
        grade = int(input())
        grade_add += grade
        count += 1
        last_task = task

        if grade <= 4:
            bad_count += 1

        if bad_count == max_bad:

            print(f"You need a break, {max_bad} poor grades.")
            break
    else:
        print(f"""Average score: {(grade_add/count):.2f}
Number of problems: {count}
Last problem: {last_task}""")
        break
