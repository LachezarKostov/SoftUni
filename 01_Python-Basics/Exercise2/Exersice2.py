num = int(input())

bonus1 = float(0)

if num <= 100:
    bonus1 = 5
elif num >= 1000:
    bonus1 = 0.1*num
else:
    bonus1 = 0.2*num



bonus2 = float(0)

if num % 10 == 5:
    bonus2 = 2
elif num % 2 == 0:
    bonus2 = 1

print(f"{bonus2+bonus1}")
print(f"{bonus2+bonus1+num}")







