count = int(input())
plants_rarity = {}
plants_rating = {}
plants_rating_avg = {}

for i in range(count):
    plant, rarity = input().split("<->")
    plants_rarity[plant] = int(rarity)
    plants_rating[plant] = []

while True:
    try:
        commands = input().split(": ")
        command = commands[0]
        if command == "Exhibition":
            break

        second_part_of_command = commands[1].split(" - ")
        plant = second_part_of_command[0]

        if command == "Rate":
            rating = int(second_part_of_command[1])
            plants_rating[plant].append(rating)

        elif command == "Update":
            rarity = int(second_part_of_command[1])
            plants_rarity[plant] = rarity

        elif command == "Reset":
            plants_rating[plant].clear()
        else:
            print("error")
    except:
        print("error")
        break

for plant_list in plants_rating.items():
    if len(plant_list[1]) != 0:
        plants_rating_avg[plant_list[0]] = [sum(plant_list[1]) / len(plant_list[1])]
    else:
        plants_rating_avg[plant_list[0]] = [0]

    plants_rating_avg[plant_list[0]].append(plants_rarity[plant_list[0]])

sorted_plants = dict(sorted(plants_rating_avg.items(), key=lambda item: ((-item[1][1]), -item[1][0], )))

print("Plants for the exhibition:")

for plant in sorted_plants:
    print(f"- {plant}; Rarity: {sorted_plants[plant][1]}; Rating: {(sorted_plants[plant][0]):.2f} ")