n = int(input())
count = 1
total = 0
while count <= n :
    money = float(input())
    if money < 0:
        print("Invalid operation!")
        break
    else:
        total += money
        print(f"Increase: {money:.2f}")
        count +=1
print(f"Total: {total:.2f}")
