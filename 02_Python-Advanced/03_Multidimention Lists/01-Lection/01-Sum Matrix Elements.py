import itertools

rows, cols = map(int, input().split(", "))
matrix = []
total = 0

for i in range(rows):
    row = [int(x) for x in input().split(", ")]
    assert len(row) == cols, f"Expecting {cols} got {len(row)}"
    matrix.append(row)
    total += sum(row)

# matrix = [[int(x) for x in input().split(", ")] for j in range(rows)]
# total = sum(itertools.chain(*matrix))

print(total)
print(matrix)
