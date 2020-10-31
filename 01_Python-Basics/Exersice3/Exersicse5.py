count = int(input())

p1 = 0
p2 = 0
p3 = 0


for i in range(0,count):
    num = int(input())

    if num%4 == 0:
        p3 += 1
    if num%3 == 0:
        p2 += 1
    if num%2 == 0:
        p1 += 1


p1 = p1/count*100
p2 = p2/count*100
p3 = p3/count*100

print(f"{p1:.2f}%\n{p2:.2f}%\n{p3:.2f}%")
