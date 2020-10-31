num = float(input())

a = str(input())
b = str(input())

if a == "mm":
    num = num/10
elif a == "m":
    num = num*100

if b == "mm":
    num = num*10
elif b == "m":
    num = num/100

print(f"{num:.3f}")