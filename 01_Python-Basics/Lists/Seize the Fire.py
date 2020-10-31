events = input().split("#")
water = int(input())
effort = 0
total_fire = 0

print("Cells:")

for i in events:

    cell = i.split(" = ")
    type_of_fire = cell[0]
    volume_of_fire = int(cell[1])

    if \
            (water - volume_of_fire) >= 0 and (
                    (type_of_fire == "High" and (81 <= volume_of_fire <= 125)) or
                    (type_of_fire == "Medium" and (51 <= volume_of_fire <= 80)) or
                    (type_of_fire == "Low" and (1 <= volume_of_fire <= 50))):

        water -= volume_of_fire
        effort += 0.25*volume_of_fire
        total_fire += volume_of_fire
        print(f" - {volume_of_fire}")

print(f"""Effort: {effort:.2f}
Total Fire: {total_fire}""")




