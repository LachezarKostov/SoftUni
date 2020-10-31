n, m = [int(x) for x in input().split()]

matrix = []
counter = 0
for i in range(n):
    matrix.append(input().split())

for i in range(n):
    for j in range(m):
        if i - 1 >= 0 and j-1 >= 0 and \
                matrix[i][j] == matrix[i-1][j] == matrix[i][j-1] == matrix[i-1][j-1]:
            counter += 1

print(counter)