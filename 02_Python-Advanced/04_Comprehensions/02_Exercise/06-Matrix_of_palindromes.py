def char_finder(num):
    return chr(num + 97)


n, m = [int(x) for x in input().split()]

matrix = []

for i in range(n):
    list = []
    for j in range(m):
        list.append(char_finder(i)+char_finder(j+i)+char_finder(i))
    matrix.append(list)

[print(" ".join(row)) for row in matrix]