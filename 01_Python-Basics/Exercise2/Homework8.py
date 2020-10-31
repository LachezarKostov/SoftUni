vac = float(input())
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())

price = a*2.6 + b*3 + c*4.1 + d*8.2 + e*2

if (a+b+c+d+e) >= 50:
    price = price*0.75

price = price*0.9

finale = abs(vac-price)

if price >= vac:
    print(f"Yes! {finale:.2f} lv left.")
else:
    print(f"Not enough money! {finale:.2f} lv needed.")