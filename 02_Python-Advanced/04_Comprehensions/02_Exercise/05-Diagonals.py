n = int(input())

matrix = []
primary = []
secondary = []

for i in range(n):
    matrix.append([int(x) for x in input().split(", ")])
    primary.append(matrix[i][i])
    secondary.append(matrix[i][n-i-1])

primary_str = [str(x) for x in primary]
secondary_str = [str(x) for x in secondary]

print(f"""
First diagonal: {", ".join(primary_str)}. Sum: {sum(primary)}
Second diagonal: {", ".join(secondary_str)}. Sum: {sum(secondary)}
""")