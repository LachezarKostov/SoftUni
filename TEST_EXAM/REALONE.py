pens = int(input())
markers = int(input())
chemical = float(input())
discount = int(input())

total = 0

total = (pens*5.8 + markers * 7.2 + chemical * 1.20) * ((100 - discount)/100)

print(f"{total:.3f}")

