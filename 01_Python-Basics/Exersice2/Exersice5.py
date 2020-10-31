money = int(input())
season = str(input())
num = int(input())

price = 0

if season == "Spring":
    price = 3000

elif season == "Summer" or season == "Autumn":
    price = 4200

elif season == "Winter":
    price = 2600

if num <= 6 :
    price *= 0.9

elif num <= 11 :
    price *= 0.85

else:
    price *= 0.75

if (num % 2 == 0) and (season != "Autumn"):

    price *= 0.95

if money >= price :

    print(f"Yes! You have {(money-price):.2f} leva left.")

else:

    print(f"Not enough money! You need {(price-money):.2f} leva.")