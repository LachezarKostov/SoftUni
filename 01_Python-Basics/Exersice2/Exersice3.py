deg = int(input())
time = str(input())

outfit = ""
shoes = ""

if time == "Morning":
    if 10 <= deg <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"

    elif 18 < deg <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"

    elif 24 < deg:
        outfit = "T-Shirt"
        shoes = "Sandals"

elif time == "Afternoon":
    if 10 <= deg <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"

    elif 18 < deg <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"

    elif 24 < deg:
        outfit = "Swim Suit"
        shoes = "Barefoot"

elif time == "Evening":

        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {deg} degrees, get your {outfit} and {shoes}.")