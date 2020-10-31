product = str(input())
town = str(input())
num = float(input())

if town == "Sofia":
    if product == "beer":
        price = 1.20
    elif product == "coffee":
        price = 0.50
    elif product == "water":
        price = 0.80
    elif product == "sweets":
        price = 1.45
    elif product == "peanuts":
        price = 1.60

elif town == "Plovdiv":
    if product == "beer":
        price = 1.15
    elif product == "coffee":
        price = 0.40
    elif product == "water":
        price = 0.70
    elif product == "sweets":
        price = 1.30
    elif product == "peanuts":
        price = 1.50

elif town == "Varna":
    if product == "beer":
        price = 1.10
    elif product == "coffee":
        price = 0.45
    elif product == "water":
        price = 0.70
    elif product == "sweets":
        price = 1.35
    elif product == "peanuts":
        price = 1.55

print(price*num)




