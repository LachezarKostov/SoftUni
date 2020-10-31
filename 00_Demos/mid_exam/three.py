import math
type_sushi = input()
restaurant = input()
count = int(input())
invalid = True

y_n = input()
price = 0


if restaurant == "Sushi Zone":
    if type_sushi == "sashimi":
        price = 4.99
    elif type_sushi == "maki":
        price = 5.29
    elif type_sushi == "uramaki":
        price = 5.99
    elif type_sushi == "temaki":
        price = 4.29
elif restaurant =="Sushi Time":
    if type_sushi == "sashimi":
        price = 5.49
    elif type_sushi == "maki":
        price = 4.69
    elif type_sushi == "uramaki":
        price = 4.49
    elif type_sushi == "temaki":
        price = 5.19
elif restaurant =="Sushi Bar":
    if type_sushi == "sashimi":
        price = 5.25
    elif type_sushi == "maki":
        price = 5.55
    elif type_sushi == "uramaki":
        price = 6.25
    elif type_sushi == "temaki":
        price = 4.75
elif restaurant =="Asian Pub":
    if type_sushi == "sashimi":
        price = 4.50
    elif type_sushi == "maki":
        price = 4.80
    elif type_sushi == "uramaki":
        price = 5.50
    elif type_sushi == "temaki":
        price = 5.50
else:
    print(f"{restaurant} is invalid restaurant!")
    invalid = False
if y_n == "Y":
    price = math.ceil(price*count*1.2)
else:
    price = math.ceil(price*count)
if invalid:
    print(f"Total price: {price} lv.")
