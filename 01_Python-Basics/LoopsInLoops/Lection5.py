town = input()


while town != "End":
    min_budget = float(input())
    saved_money = 0

    while min_budget > saved_money:
        money = float(input())
        saved_money += money

        if saved_money >= min_budget:
            print(f"Going to {town}!")
    town = input()
