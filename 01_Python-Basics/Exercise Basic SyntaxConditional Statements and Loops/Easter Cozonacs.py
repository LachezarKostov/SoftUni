import math
money = float(input())
flour_price = float(input())
eggs_price = .75 * flour_price
milk_price = 1.25 * flour_price
egg_count = 0
cozunact_count = 0

price_for_one_cozunack = eggs_price + flour_price + .25*milk_price

while money >= price_for_one_cozunack:
    cozunact_count += 1
    egg_count += 3
    money -= price_for_one_cozunack

    if cozunact_count % 3 == 0:
        egg_count -= cozunact_count -2

print(f"You made {cozunact_count} cozonacs! Now you have {egg_count} eggs and {money:.2f}BGN left.")



