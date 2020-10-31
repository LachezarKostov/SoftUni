bord_size = int(input())
num_mines = int(input())

NEIGHBORINGCELLS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

minefield = [[0] * bord_size
             for i in range(bord_size)]

for _ in range(num_mines):
    i, j = eval(input())
    minefield[i][j] = "*"



for i in range(1, bord_size-1):
    for j in range(1, bord_size-1):
        mine_count = 0
        for di, dj in NEIGHBORINGCELLS:
                if minefield[i+di][j+dj]:
                    mine_count += 1
    


print(minefield)