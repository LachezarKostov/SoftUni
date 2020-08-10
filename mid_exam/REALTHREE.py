money = float(input())
gender = input()
age = int(input())
sport = input()

price = 0

if gender == "m":
    if sport == "Gym":
        price = 42
    if sport == "Boxing":
        price = 41
    if sport == "Yoga":
        price = 45
    if sport == "Zumba":
        price = 34
    if sport == "Dances":
        price = 51
    if sport == "Pilates":
        price = 39

else:
    if sport == "Gym":
        price = 35
    if sport == "Boxing":
        price = 37
    if sport == "Yoga":
        price = 42
    if sport == "Zumba":
        price = 31
    if sport == "Dances":
        price = 53
    if sport == "Pilates":
        price = 37

if age <= 19:
    price = price * 0.8

if money >= price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${(price-money):.2f} more.")