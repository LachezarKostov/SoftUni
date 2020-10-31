a = int(input())
b = int(input())
area = a*b

while area >= 0:
    pisses = input()
    if pisses != "STOP":
        pisses = int(pisses)
        area -= pisses
    else:
        print(f"{area} pieces are left.")
        break

if area <= 0:
    print(f"No more cake left! You need {-area} pieces more.")
