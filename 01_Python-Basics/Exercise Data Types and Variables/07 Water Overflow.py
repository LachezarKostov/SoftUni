water_tank = 255
n = int(input())
fill = 0

while n > 0:
    liters = int(input())
    water_tank -= liters
    if water_tank >= 0:
        fill += liters
    else:
        print("Insufficient capacity!")
        water_tank += liters
    n -= 1
print(fill)

