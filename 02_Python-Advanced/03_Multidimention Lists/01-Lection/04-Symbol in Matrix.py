def find_in_matrix(matrix, symbol):
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == symbol:
                return i, j


n = int(input())
matrix = [list(input()) for _ in range(n)]
symbol = input()

pos = find_in_matrix(matrix, symbol)

if pos:
    print(pos)
else:
    print(f"{symbol} does not occur in the matrix")


# n = int(input())
# matrix = []
# finde = True
# for _ in range(n):
#     matrix.append(input())
#
# special_sym = input()
#
# for i in range(n):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] == special_sym:
#             print(f"({i}, {j})")
#             finde = False
#
# if finde:
#     print(f"{special_sym} does not occur in the matrix")