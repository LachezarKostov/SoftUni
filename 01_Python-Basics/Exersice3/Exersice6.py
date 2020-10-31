count = int(input())
sel = int(input())
fine = 0

for i in range(0,count):
    site = str(input())
    if site == "Facebook":
        fine += 150
    elif site == "Instagram":
        fine += 100
    elif site == "Reddit":
        fine += 50
if sel <= fine :
    print("You have lost your salary.")
else:
    print(sel-fine)