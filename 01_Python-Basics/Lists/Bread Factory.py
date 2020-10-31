events = input().split("|")
energy = 100
coins = 100
is_bankrupt = False

for event in events:
    args = event.split("-")
    name = args[0]
    value = int(args[1])

    if name == "rest":
        rested_energy = 0

        new_energy = energy + value
        if new_energy >= 100:
            new_energy = 100
        rested_energy = new_energy - energy
        energy = new_energy

        print(f"You gained {rested_energy} energy.")
        print(f"Current energy: {new_energy}.")

    elif name == "order":

        if energy < 30:
            energy += 50
            print("You had to rest!")
            continue
        else:
            coins += value
            energy -= 30
            print(f"You earned {value} coins.")

    else:
        if coins - value <= 0:
            print(f"Closed! Cannot afford {name}.")
            is_bankrupt = True
            break
        else:
            print(f"You bought {name}.")
            coins -= value

if not is_bankrupt:
    print(f"""Day completed!
Coins: {coins}
Energy: {energy}""")