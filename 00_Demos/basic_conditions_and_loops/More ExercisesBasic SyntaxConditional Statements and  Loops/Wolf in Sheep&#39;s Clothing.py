herd = input().split(", ")

herd_count = len(herd)

for sheep in range(0, herd_count):
    if herd[sheep] == "wolf":
        if sheep + 1 == herd_count:
            print("Please go away and stop eating my sheep")
        else:
            sheep_count = herd_count - (sheep + 1)
            print(f"Oi! Sheep number {sheep_count}! You are about to be eaten by a wolf!")

