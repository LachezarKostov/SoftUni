money_for_singer = int(input())
people = input()
money = 0
people_count = 0


while people != "The restaurant is full":
    people = int(people)
    if people < 5:
        money += people*100
        people_count += people
    else:
        money += people*70
        people_count += people
    people = input()

if money >= money_for_singer:
    money -= money_for_singer
    print(f"You have {people_count} guests and {money} leva left.")
else:
    print(f"You have {people_count} guests and {money} leva income, but no singer.")


