single_line = list(map(int, (input().split(", "))))

for num in single_line:
    if num == 0:
        single_line.remove(0)
        single_line.append(0)

print(single_line)
