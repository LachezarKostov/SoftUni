line = input()
sides = {}
while line != "Lumpawaroo":
    if " | " in line:
        side, user = line.split(" | ")

        if side not in sides:
            sides[side] = []
        all_values = []

        for current_list in sides.values():
            all_values += current_list

        if user not in all_values:
            sides[side].append(user)

    else:
        user, side = line.split(" -> ")
        old_side = ""

        for key, value in sides.items():
            if user in value:
                old_side = key
                break

        if old_side != "":
            sides[old_side].remove(user)

            if side not in sides:
                sides[side] = []

            sides[side].append(user)

        else:
            if side not in sides:
                sides[side] = []

            if user not in sides[side]:
                sides[side].append(user)

        print(f"{user} joins the {side} side!")

    line = input()

sides = dict(sorted(sides.items(), key=lambda x: (-len(x[1]), x[0])))

for side, users in sides.items():
    if len(users) == 0:
        continue
    print(f"Side: {side}, Members: {len(users)}")

    for user in sorted(users):
        print(f"! {user}")
