command = input().split("-")
liked_meals = {}
unliked_meals = 0

while command[0] != "Stop":
    guest = command[1]
    meal = command[2]

    if command[0] == "Like":
        if guest not in liked_meals:
            liked_meals[guest] = []
        if meal not in liked_meals[guest]:
            liked_meals[guest].append(meal)

    elif command[0] == "Unlike":
        if guest not in liked_meals:
            print(f"{guest} is not at the party.")
        elif meal not in liked_meals[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")

        else:
            liked_meals[guest].remove(meal)
            unliked_meals += 1
            print(f"{guest} doesn't like the {meal}.")

    command = input().split("-")

liked_meals = dict(sorted(liked_meals.items(), key=lambda item: (-len(item[1]), item[0])))

for guest, meals in liked_meals.items():
    print(f"{guest}: {', '.join(meals)}")

print(f"Unliked meals: {unliked_meals}")