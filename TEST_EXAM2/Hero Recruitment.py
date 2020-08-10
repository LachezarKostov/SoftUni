heroes_spells = {}
while True:
    command = input()

    if command == "End":
        break

    command = command.split()
    hero_name = command[1]
    if command[0] == "Enroll":
        if hero_name not in heroes_spells:
            heroes_spells[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")

    elif command[0] == "Learn":
        new_spell = str(command[2])
        if hero_name not in heroes_spells:
            print(f"{hero_name} doesn't exist.")
        elif new_spell in heroes_spells[hero_name]:
            print(f"{hero_name} has already learnt {new_spell}.")
        else:
            heroes_spells[hero_name].append(new_spell)

    elif command[0] == "Unlearn":
        new_spell = str(command[2])
        if hero_name not in heroes_spells:
            print(f"{hero_name} doesn't exist.")
        elif new_spell not in heroes_spells[hero_name]:
            print(f"{hero_name} doesn't know {new_spell}.")
        else:
            heroes_spells[hero_name].remove(new_spell)

heroes_spells = dict(sorted(heroes_spells.items(), key=lambda item: (-len(item[1]), item[0])))
print("Heroes:")
for hero, spells in heroes_spells.items():
    print(f"== {hero}: {', '.join(spells)}")
