from _collections import deque as dq


def deque_print_list(deque):
    string_deque_list = [str(x) for x in list(deque)]
    string_deque_list = ', '.join(string_deque_list)

    return string_deque_list


BOMB_TYPES = (40, 60, 120)
datura_Bombs = 0
cherry_Bombs = 0
smoke_Decoy_Bombs = 0

bomb_effects = dq(int(i) for i in input().split(", "))
bomb_casings = dq(int(i) for i in input().split(", "))

while (bomb_effects and bomb_casings) \
        and (datura_Bombs < 3 or cherry_Bombs < 3 or smoke_Decoy_Bombs < 3):

    bomb = bomb_effects[0] + bomb_casings[-1]
    if bomb in BOMB_TYPES:
        bomb_effects.popleft()
        bomb_casings.pop()

        if bomb == 40:
            datura_Bombs += 1
        elif bomb == 60:
            cherry_Bombs += 1
        elif bomb == 120:
            smoke_Decoy_Bombs += 1
    else:
        bomb_casings[-1] -= 5

if datura_Bombs >= 3 \
        and cherry_Bombs >= 3 \
        and smoke_Decoy_Bombs >= 3:

    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {deque_print_list(bomb_effects)}")
else:
    print(f"Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {deque_print_list(bomb_casings)}")
else:
    print(f"Bomb Casings: empty")

print(f"""Cherry Bombs: {cherry_Bombs}
Datura Bombs: {datura_Bombs}
Smoke Decoy Bombs: {smoke_Decoy_Bombs}
""")
