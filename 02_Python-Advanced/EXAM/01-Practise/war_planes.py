moves = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}

n = int(input())


def matrix_input(n):
    matrix = []
    for i in range(n):
        matrix.append(input().split(" "))
    return matrix


def matrix_print(matrix):
    for i in range(len(matrix)):
        print(" ".join(matrix[i]))


def find_plane(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "p":
                return i, j


def target_finder(matrix):
    targets = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "t":
                targets += 1
    return targets


battle_field = matrix_input(n)
m = int(input())
starting_targets = target_finder(battle_field)

for _ in range(m):
    plane_position = find_plane(battle_field)
    new_position = [0, 0]
    command, orientation, steps = input().split(" ")
    delta_position = [x * int(steps) for x in moves[orientation]]
    new_x = plane_position[0] + delta_position[0]
    new_y = plane_position[1] + delta_position[1]

    if 0 <= new_x <= n-1 and 0 <= new_y <= n-1 and target_finder(battle_field) > 0:
        if command == "move":
            if battle_field[new_x][new_y] == ".":
                battle_field[plane_position[0]][plane_position[1]] = "."
                plane_position = new_x, new_y
                battle_field[new_x][new_y] = "p"
        if command == "shoot":
            battle_field[new_x][new_y] = "x"

if target_finder(battle_field) > 0:
    print(f"Mission failed! {target_finder(battle_field)} targets left.")
else:
    print(f"Mission accomplished! All {starting_targets} targets destroyed.")

matrix_print(battle_field)