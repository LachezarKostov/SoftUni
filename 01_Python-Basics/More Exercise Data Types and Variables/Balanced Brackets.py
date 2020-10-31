num_of_lines = int(input())
is_balanced = True
list_of_lines = []
list_of_lines_2 = []

for _ in range(num_of_lines):
    line = input()
    list_of_lines.append(line)

count_1 = list_of_lines.count("(")
count_2 = list_of_lines.count(")")



if count_1 == count_2 and is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
