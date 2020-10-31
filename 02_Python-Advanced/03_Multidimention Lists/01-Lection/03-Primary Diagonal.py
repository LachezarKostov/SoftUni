n = int(input())
matrix = []
total = 0

for _ in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    total += matrix[i][i]

print(total)