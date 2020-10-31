for num in range(1, 101):
    if num % 15 is 0:
        print("AB")
    elif num % 3 is 0:
        print("A")
    elif num % 5 is 0:
        print("B")
    else:
        print(num)