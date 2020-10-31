n = int(input())
matrix = []
i_knight, j_knight = 0, 0
K_count = 0
counter = 0

possible_moves = [
    (-2, -1),
    (-2, 1),
    (-1, 2),
    (-1, -2),
    (1, -2),
    (1, 2),
    (2, -1),
    (2, 1)
]

def index_validate(matrix_length, number):
    if -1 < number < matrix_length:
        return True
    return False


for i in range(n):
    matrix.append(list(input()))
    K_count += matrix[i].count("K")


for _ in range(K_count):
    K_to_take_max = 0
    i_to_remove, j_to_remove = 0, 0
    for i in range(n):
        for j in range(n):
            K_to_take = 0
            if matrix[i][j] == "K":
                i_knight, j_knight = i, j
                for move in possible_moves:
                    row_addition, column_addition = move
                    if index_validate(len(matrix), i + row_addition) and \
                            index_validate(len(matrix), j + column_addition):
                        K_to_take += 1

                # if i+1 in range(0, n) and j+2 in range(0, n) and matrix[i + 1][j + 2] == "K":
                #     K_to_take += 1
                # if i+1 in range(0, n) and j-2 in range(0, n) and matrix[i + 1][j - 2] == "K":
                #     K_to_take += 1
                # if i-1 in range(0, n) and j+2 in range(0, n) and matrix[i - 1][j + 2] == "K":
                #     K_to_take += 1
                # if i-1 in range(0, n) and j-2 in range(0, n) and matrix[i - 1][j - 2] == "K":
                #     K_to_take += 1
                # if i+2 in range(0, n) and j+1 in range(0, n) and matrix[i + 2][j + 1] == "K":
                #     K_to_take += 1
                # if i+2 in range(0, n) and j-1 in range(0, n) and matrix[i + 2][j - 1] == "K":
                #     K_to_take += 1
                # if i-2 in range(0, n) and j+1 in range(0, n) and matrix[i - 2][j + 1] == "K":
                #     K_to_take += 1
                # if i-2 in range(0, n) and j-1 in range(0, n) and matrix[i - 2][j - 1] == "K":
                #     K_to_take += 1

            if K_to_take > K_to_take_max:
                i_to_remove, j_to_remove = i_knight, j_knight
                K_to_take_max = K_to_take

    if K_to_take_max:
        matrix[i_to_remove][j_to_remove] = "0"
        counter += 1

print(counter)
