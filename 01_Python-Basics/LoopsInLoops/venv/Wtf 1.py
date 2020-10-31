n = input()
holder = 0
count = 0
for i in n:

    if holder != i :
        count += 1
    holder = i

print(count)
