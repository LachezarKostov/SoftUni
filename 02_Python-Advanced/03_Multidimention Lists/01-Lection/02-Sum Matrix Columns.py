rows, cols = map(int, input().split(", "))
matrix = []
total = 0

for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for col in range(cols):
    for row in range(rows):
        number = matrix[row][col]
        total += number
    print(total)
    total = 0
