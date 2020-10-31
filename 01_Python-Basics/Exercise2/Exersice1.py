import math

t1 = int(input())
t2 = int(input())
t3 = int(input())

t = t1 + t2 + t3

m = math.floor(t / 60)
s = t % 60

if s < 10:
    print(f"{m}:0{s}")
else:
    print(f"{m}:{s}")
