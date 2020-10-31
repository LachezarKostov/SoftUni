count = int(input())
length = int(input())
multy = 0
list_to_make = []

for _ in range(length):
    multy += count
    list_to_make.append(multy)


print(list_to_make)


