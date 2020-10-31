budget = float(input())
season = str(input())
cost = 0
destination = ""
type_acc = ""

if budget <= 100:
    cost = budget * 0.3 if season == "summer" else budget*0.7
    destination = "Bulgaria"
    type_acc = "Camp" if season == "summer" else "Hotel"

elif budget <= 1000:
    cost = budget * 0.4 if season == "summer" else budget*0.8
    destination = "Balkans"
    type_acc = "Camp" if season == "summer" else "Hotel"

else:
    cost = budget * 0.9
    destination = "Europe"
    type_acc = "Hotel"

print(f"Somewhere in {destination}")
print(f"{type_acc} - {cost:.2f}")