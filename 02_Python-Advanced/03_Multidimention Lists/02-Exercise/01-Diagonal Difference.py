n = int(input())

matrix = []
total_primary = 0
total_secondary = 0

for i in range(n):
    matrix.append(int(x) for x in input().split())
    total_primary += matrix[i][i]
    total_secondary += matrix[i][n-i-1]

print(abs(total_secondary-total_primary))


