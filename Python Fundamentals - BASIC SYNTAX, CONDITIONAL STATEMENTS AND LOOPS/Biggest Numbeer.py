a = float(input())

if a == 0:
    print("zero")
else:
    if abs(a) < 1:
        print("small", end=" ")
    elif abs(a) > 1000000:
        print("large", end=" ")

    if a < 0:
        print("negative")
    else:
        print("positive")

