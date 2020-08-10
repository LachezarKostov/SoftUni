from re import findall

destinations = input()
regex = r"([=|\/]{1})([A-Z][A-za-z]{2,})(\1)"

valid_destinations = findall(regex, destinations)

travel_points = 0
travel_destinations = []
print("Destinations:", end=" ")
for i in valid_destinations:
    travel_destinations.append(i[1])
    travel_points += len(i[1])
print(", ".join(travel_destinations))
print(f"Travel Points: {travel_points}")