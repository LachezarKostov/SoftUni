import math

expression = input().split(" ")

list_to_operate = []

for x in expression:
    try:
        x = int(x)
        list_to_operate.append(str(x))
    except ValueError:
        if x == "*":
            result = eval(" * ".join(list_to_operate))
            list_to_operate.clear()
            list_to_operate.append(str(result))
        elif x == "+":
            result = eval(" + ".join(list_to_operate))
            list_to_operate.clear()
            list_to_operate.append(str(result))
        elif x == "-":
            result = eval(" - ".join(list_to_operate))
            list_to_operate.clear()
            list_to_operate.append(str(result))
        elif x == "/":
            result = eval(" / ".join(list_to_operate))
            list_to_operate.clear()
            list_to_operate.append(str(math.floor(result)))

print(list_to_operate[0])
