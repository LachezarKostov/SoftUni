a = int(input())
b = int(input())
sum = ""

for j in range(a, b+1):
    sum += chr(j)
    sum += " "

print(sum)