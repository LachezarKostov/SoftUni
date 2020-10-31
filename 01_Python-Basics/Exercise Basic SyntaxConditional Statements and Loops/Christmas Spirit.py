quantity = int(input())
days = int(input())
Ornament_Set = 2
Tree_Skirt = 5
Tree_Garlands = 3
Tree_Lights = 15
Christmas_spirit = 0
day = 1
cost = 0

while days >= day:

    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        cost += quantity * Ornament_Set
        Christmas_spirit += 5

    if day % 3 == 0:
        cost += quantity * (Tree_Garlands + Tree_Skirt)
        Christmas_spirit += 13

    if day % 5 == 0:
        cost += quantity * Tree_Lights
        Christmas_spirit += 17
        if day % 3 == 0:
            Christmas_spirit += 30

    if day % 10 == 0:
        Christmas_spirit -= 20
        cost +=   (Tree_Skirt + Tree_Garlands + Tree_Lights)

    if days == day and day % 10 == 0:
        Christmas_spirit -= 30

    day += 1


print(f"""Total cost: {cost}
Total spirit: {Christmas_spirit}""")
