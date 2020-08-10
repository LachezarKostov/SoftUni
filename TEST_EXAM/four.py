passengers = int(input())
stops = int(input())
count = 1

while count <= stops:
    passengers_off = int(input())
    passengers -= passengers_off
    passengers_on = int(input())
    passengers += passengers_on

    if count % 2 != 0:
        passengers += 2
    else:
        passengers -= 2
    count += 1
print(f"The final number of passengers is : {passengers}")



