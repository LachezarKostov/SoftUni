rows, columns = map(int, input().split())
a = [[int(j) for j in input().split()] for _ in range(rows)]

max_sum = 0
top_left_row = 0
top_left_column = 0

for i in range(rows - 2):
    for j in range(columns - 2):
        total = 0
        for k in range(i, i + 3):
            for m in range(j, j + 3):
                total += a[k][m]
        if total > max_sum:
            max_sum = total
            top_left_row, top_left_column = i, j

print(f'Sum = {max_sum}')

for i in range(top_left_row, top_left_row + 3):
    for j in range(top_left_column, top_left_column + 3):
        print(a[i][j], end=' ')
    print()