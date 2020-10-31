days = int(input())
type_room = str(input())
option = str(input())


night = days - 1
price = 0

if type_room == "room for one person":
    price = night * 18

elif type_room == "apartment":
    price = night * 25

    if night <= 10:
        price = price*0.7

    elif 10 < night < 15:
        price = price*0.65

    elif 15 <= night:
        price = price*0.50

elif type_room == "president apartment":
    price = night * 35

    if night <= 10:
        price = price * 0.9

    elif 10 < night < 15:
        price = price * 0.85

    elif 15 <= night:
        price = price * 0.80

if option == "positive":
    price = price * 1.25

elif option == "negative":
    price = price * 0.9

print(f"{price:.02f}")



