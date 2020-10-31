import math
h_ship = float(input())
a_ship = float(input())
b_ship = float(input())
astro_high = float(input())

volume_ship = h_ship*a_ship*b_ship

volume_room = (astro_high+0.4)*4

count = math.floor(volume_ship/volume_room)

if count > 10:
    print("The spacecraft is too big.")
elif count < 3:
    print("The spacecraft is too small.")
else:
    print(f"The spacecraft holds {count} astronauts.")