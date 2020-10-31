money_food = float(input())
money_souvenirs = float(input())
money_hotel = float(input())
days = 3

money_for_fuel = (420/100*7)*1.85

money = (money_souvenirs+money_food)*3 + money_for_fuel
money += money_hotel*0.9 + money_hotel*0.85 + money_hotel*0.80

print(f"Money needed: {money:.2f}")



