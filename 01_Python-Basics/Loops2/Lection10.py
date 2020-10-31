x = int(input())
y = int(input())
z = int(input())
a = ""
b = 0
free_voluem = x*y*z

while a != "Done":
    a = input()
    if a != "Done":
        a = int(a)
        b += a
    if free_voluem < b:
        print(f"No more free space! You need {b-free_voluem} Cubic meters more.")
        break
if b < free_voluem:
    print(f"{free_voluem-b} Cubic meters left.")
