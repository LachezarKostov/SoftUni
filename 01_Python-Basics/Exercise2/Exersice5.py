hour = int(input())
minn = int(input())

minn = minn + 15

if minn >= 60:
    hour += 1
    minn -= 60

if hour >= 24:
    hour = 0

if minn < 10:

    print(f"{hour}:0{minn}")

else :
    print(f"{hour}:{minn}")