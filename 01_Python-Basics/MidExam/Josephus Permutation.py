josephus_line = list(map(int, (input().split())))
count = int(input()) - 1
new_line = []

while josephus_line:
    if count > len(josephus_line):
        count = count % len(josephus_line)
    new_line.append(josephus_line.pop(count))
    count += count
print(new_line)
