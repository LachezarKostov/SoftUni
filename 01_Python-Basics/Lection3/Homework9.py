town = str(input())
num = float(input())

commission = 0

if town == "Sofia":
    if 0 <= num <= 500:
        commission = 0.05 * num
    elif 500 <= num <= 1000:
        commission = 0.07 * num
    elif 1000 <= num <= 10000:
        commission = 0.08 * num
    elif 10000 <= num:
        commission = 0.12 * num
    else:
        print("error")

elif town == "Varna":

    if 0 <= num <= 500:
        commission = 0.045 * num
    elif 500 <= num <= 1000:
        commission = 0.075 * num
    elif 1000 <= num <= 10000:
        commission = 0.10 * num
    elif 10000 <= num:
        commission = 0.13 * num
    else:
        print("error")

elif town == "Plovdiv":

    if 0 <= num <= 500:
        commission = 0.055 * num
    elif 500 <= num <= 1000:
        commission = 0.08 * num
    elif 1000 <= num <= 10000:
        commission = 0.12 * num
    elif 10000 <= num:
        commission = 0.145 * num
    else:
        print("error")

else:
    print("error")

if commission > 0:

    print(f"{commission:.02f}")