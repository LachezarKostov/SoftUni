need_to_save = float(input())
money = float(input())
spend_count = 0
days = 0

while money < need_to_save:
    action = input()
    action_money = float(input())
    days += 1

    if action == "spend":
        spend_count += 1
        money -= action_money
    if money < 0:
        money = 0
    if spend_count == 5:
        print(f"You can't save the money.\n{days}")
        break
    if action == "save":
        money += action_money
        spend_count = 0

if need_to_save <= money:
    print(f"You saved the money for {days} days.")

