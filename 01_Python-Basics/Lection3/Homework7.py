fruit = str(input())
day = str(input())
quantity = float(input())

list_a = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
list_b = ["Saturday", "Sunday"]

price = 0

if day in list_a:
    if fruit == "banana":
        price = 2.5
    elif fruit == "apple":
        price = 1.20
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.50
    elif fruit == "grapes":
        price = 3.85
    else:
        print("error")

elif day in list_b:
    if fruit == "banana":
        price = 2.7
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.90
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == "kiwi":
        price = 3.00
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20
    else:
        print("error")
else:
    print("error")

if price > 0:
    print(f"{(price*quantity):.02f}")

