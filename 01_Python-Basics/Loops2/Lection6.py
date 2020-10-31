import math
bigest_number = math.inf
count = int(input())
count1 = 0
while count > count1:
    number = int(input())
    count1 += 1
    if number < bigest_number:
        bigest_number = number
print(bigest_number)
