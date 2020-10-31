rows = int(input())
list_1 = []
list_2 = []
for i in range(0, rows):
    count = 1
    list_1 = []
    for k in range(0, i + 1):

        list_1.append(count)

        count = int(count * (i - k) / (k + 1))

        if i + 1 == rows + 1:
            list_1.append(count)
    list_2.append(list_1)

print(list_2)
