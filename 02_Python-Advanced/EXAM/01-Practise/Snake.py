def create_bord(n):
    bord = []
    for i in range(n):
        bord.append([])
        row = input()
        for j in range(n):
            bord[i].append(row[j])

    return bord


def print_board(bord):
    n = len(bord)
    for i in range(n):
        for j in range(n):
            print(bord[i][j], end="")
        print()


def find_on_bord(bord, a):
    n = len(bord)
    for i in range(n):
        for j in range(n):
            if bord[i][j] == a:
                return i, j


food_eaten = 0
MOVES = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

n = int(input())

bord = create_bord(n)

Si, Sj = find_on_bord(bord, "S")

game_over = False
while not game_over:
    move = input()
    di, dj = MOVES[move]
    bord[Si][Sj] = "."
    new_Si, new_Sj = di + Si, dj + Sj

    if 0 <= new_Si <= n - 1 \
            and\
        0 <= new_Sj <= n - 1:

        position_to_move = bord[new_Si][new_Sj]

        if position_to_move == "-":
            Si, Sj = new_Si, new_Sj

        elif position_to_move == "B":
            bord[new_Si][new_Sj] = "."
            Bi, Bj = find_on_bord(bord, "B")
            Si, Sj = Bi, Bj

        elif position_to_move == "*":
            food_eaten += 1
            Si, Sj = new_Si, new_Sj

        bord[Si][Sj] = "S"
        if food_eaten == 10:
            game_over = True
            print('You won! You fed the snake.')
    else:
        game_over = True
        print(f"Game over!")


print(f"Food eaten: {food_eaten}")
print_board(bord)