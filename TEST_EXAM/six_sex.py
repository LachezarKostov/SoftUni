num = input()

one = num[0]
one = int(one)
two = num[1]
two = int(two)
three = num[2]
three = int(three)

for a in range(1, three+1):
    for b in range(1, two+1):
        for c in range(1, one+1):
            multy = a*b*c
            print(f"{a} * {b} * {c} = {multy};")


