h = int(input())
m = int(input())
hs = int(input())
ms = int(input())

m = m + h*60
ms = ms + hs*60
delta = m - ms
mm = delta % 60
hh = abs(delta - mm) / 60

if delta > 30:
    print("Early")
    if hh > 0 and mm < 10:
        print(f"{hh:.0f}:0{mm} hours before the start")
    elif hh > 0:
        print(f"{hh:.0f}:{mm} hours before the start")
    else:
        print(f"{mm} minutes before the start")

elif delta > 0:
    print("On time")
    print(f"{mm} minutes before the start")

elif delta == 0:
    print("On time")

else:
    delta = ms - m
    mm = delta % 60
    hh = abs(delta - mm) / 60
    print("Late")

    if hh > 0 and mm < 10:
        print(f"{hh:.0f}:0{mm} hours after the start")
    elif hh > 0:
        print(f"{hh:.0f}:{mm} hours after the start")
    else:
        print(f"{mm} minutes after the start")


