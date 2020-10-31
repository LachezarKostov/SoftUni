health = 100
bitcoins = 0
dead = False
count = 0

rooms = (input()).split("|")

for i in rooms:
    list = i.split(" ")
    action = list[0]
    points = int(list[1])
    count += 1

    if action == "potion":
        if (health + points) >= 100:
            heal_points = 100 - health
            health = 100
        else:
            heal_points = points
            health += heal_points

        print(f"You healed for {heal_points} hp.")
        print(f"Current health: {health} hp.")

    elif action == "chest":
        bitcoins += points
        print(f"You found {points} bitcoins.")

    else:
        health -= points
        if health > 0:
            print(f"You slayed {action}.")
        else:
            print(f"You died! Killed by {action}.")
            print(f"Best room: {count}")
            dead = True
            break

if not dead:
    print(f"You've made it! \nBitcoins: {bitcoins} \nHealth: {health}")







