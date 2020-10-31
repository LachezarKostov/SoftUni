count = int(input())
plant_rarity_rating = {}

for i in range(count):
    plant_and_rarity = input().split("<->")
    plant = plant_and_rarity[0]
    rarity = plant_and_rarity[1]

    plant_rarity_rating[plant] = {"Rarity": rarity, "Rating": []}

command = input()

while command != "Exhibition":
    command = command.split()
    plant = command[1]

    if command[0] == "Rate:":
        rating = int(command[3])
        plant_rarity_rating[plant]["Rating"].append(rating)
    elif command[0] == "Update:":
        new_rarity = int(command[3])
        plant_rarity_rating[plant]["Rarity"] = new_rarity

    elif command[0] == "Reset:":
        plant_rarity_rating[plant]["Rating"].clear()
        plant_rarity_rating[plant]["Rating"].append(0)
    else:
        print("error")
    command = input()
for plant in plant_rarity_rating.items():
    if len(print(1)["Rating"]) != 0:
        plant(1)["Rating"] = sum(plant(1)["Rating"])/len(plant(1)["Rating"])
    #["Rating"] = sum(plant["Rating"]) / len(plant["Rating"])



print(plant_rarity_rating)
