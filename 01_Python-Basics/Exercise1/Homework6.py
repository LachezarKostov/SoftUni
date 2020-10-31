days = int(input())
cooks = int(input())
cake = int(input())
waffle = int(input())
pancake = int(input())

money_cake = cake * 45
money_waffle = waffle * 5.80
money_pancake = pancake * 3.20

money_for_a_day = (money_waffle + money_cake + money_pancake) * cooks

money = money_for_a_day * days

final_money = money - (money/8)

print(f"{final_money:.2f}")




