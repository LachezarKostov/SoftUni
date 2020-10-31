def is_valid(matrix, cmd):

    if cmd and cmd[0] != "swap":
        return False
    if len(cmd[1:]) != 4:
        return False
    i1, i2, j1, j2 = tuple(map(int, cmd[1:]))

    if i1 < 0 or i1 > m:
        return False
    if i2 < 0 or i2 > m:
        return False
    if j1 < 0 or j1 > n:
        return False
    if j2 < 0 or j2 > n:
        return False

    return True

def print_func(matrix):
    for i in range(len(matrix)):
        print(" ".join(matrix[i]))


n, m = [int(x) for x in input().split()]

matrix = []
counter = 0
for i in range(n):
    matrix.append(input().split())

cmd = input()
while cmd != "END":
    cmd = cmd.split()

    if is_valid(matrix, cmd):
        i1, i2, j1, j2 = tuple(map(int, cmd[1:]))
        tmp = matrix[i1][i2]
        matrix[i1][i2] = matrix[j1][j2]
        matrix[j1][j2] = tmp

        print_func(matrix)

    else:
        print("Invalid input!")
    cmd = input()