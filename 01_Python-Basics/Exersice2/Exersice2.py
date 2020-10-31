type_ = str(input())
a = int(input())
b = int(input())

num = a * b

price = 0

if type_ == "Premiere" :
    price = num*12

elif type_ == "Normal" :
    price = num*7.50

elif type_ == "Discount":
    price = num * 5

else:

    print("error")

print(f"{price:.2f} leva")