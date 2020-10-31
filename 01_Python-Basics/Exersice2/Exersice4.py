flower = str(input())
count = int(input())
money = float(input())

price = 0

if flower == "Roses" :
    price = count * 5
    if count > 80 :
        price = price*0.9

elif flower == "Dahlias" :
    price = count * 3.8
    if count > 90 :
        price = price*0.85

elif flower == "Tulips" :
    price = count * 2.8
    if count > 80 :
        price = price*0.85

elif flower == "Narcissus":
    price = count * 3
    if count < 120:
        price = price*1.15

elif flower == "Gladiolus":
    price = count * 2.50
    if count < 80:
        price = price*1.20

if price <= money:
    print(f"Hey, you have a great garden with {count} {flower} and {(money-price):.2f} leva left.")

elif money < price:
    print(f"Not enough money, you need {(price-money):.2f} leva more.")