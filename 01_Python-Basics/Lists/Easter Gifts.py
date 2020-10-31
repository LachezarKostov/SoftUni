gifts = input().split()

while True:
    command = input().split()

    if command[0] == "OutOfStock":
        for ind, gift in enumerate(gifts):
            if gift == command[1]:
                gifts[ind] = None

    elif command[0] == "Required":
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts.pop(index)
            gifts.insert(index, command[1])

    elif command[0] == "JustInCase":
        gifts.pop(-1)
        gifts.append(command[1])

    else:
        break

for i in gifts:
    if i != None:
        print(i, end=" ")





