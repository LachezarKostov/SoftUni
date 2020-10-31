import math

money_in = float(input())
stats = float(input())
price_for_stats = float(input())

decor = money_in*0.1
tottal_stats = price_for_stats*stats

if stats > 150:
    tottal_stats = tottal_stats*0.9

tottal = money_in - decor - tottal_stats

if tottal < 0:
    print("Not enough money!")
    print(f"Wingard needs {abs(tottal):.2f} leva more.")

else:
    print("Action!")
    print(f"Wingard starts filming with {abs(tottal):.2f} leva left.")