whiskey_price = float(input())

quantity_beer = float(input())
quantity_wine = float(input())
quantity_rakia = float(input())
quantity_whiskey = float(input())

rakia_price = whiskey_price /2
wine_price = rakia_price - (0.4 * rakia_price)
beer_price = rakia_price - (0.8 * rakia_price)

price = whiskey_price * quantity_whiskey + wine_price * quantity_wine + beer_price * quantity_beer + rakia_price * quantity_rakia

print(f"{price:.2f}")

