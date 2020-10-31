matrix = []

for i in range(3):
    matrix.append([])
    for j in range(2):
        matrix[i].append(0)

print(matrix)

matrix = [[0 for i in range(2)] for j in range(3)]

print(matrix)

matrix = []
for i in range(3):
    matrix.append([])
    for j in range(1,4):
        matrix.append(j)

print(matrix)
