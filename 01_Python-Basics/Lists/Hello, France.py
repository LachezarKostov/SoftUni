shop_list = input().split("|")
budget = int(input())

profit = 0
total_profit = 0
cloths_max = 50
shoes_max = 35
accessories = 25.50

for i in shop_list:
    cloths_and_price = i.split("->")
    cloths = cloths_and_price[0]
    price = float(cloths_and_price[1])

    if ((budget - price) >= 0 and (
            (cloths == "Clothes" and price <= cloths_max) or
            (cloths == "Shoes" and price <= shoes_max) or
            (cloths == "Accessories" and price <= accessories))):
        budget -= price
        new_price = 1.4 * price
        profit += new_price - price
        total_profit += new_price

        print(f"{new_price:.2f}", end=" ")

print(f"""
Profit: {profit:.2f}""")

if total_profit+budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")