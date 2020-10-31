age = int(input())
price_to_pay = float(input())
toy_price = int(input())

bday_money = 0
money = 0
toys = 0

for count in range(2, age+1, 2):
    bday_money += 10
    money += bday_money - 1


for count in range(1, age+1, 2):
    toys += 1

money += toy_price*toys

if money >= price_to_pay:
    print(f"Yes! {(money - price_to_pay):.2f}")
else:
    print(f"No! {(price_to_pay-money):.2f}")