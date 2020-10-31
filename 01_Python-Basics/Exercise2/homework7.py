from math import pi

fig = str(input())

if fig == "square":
    num = float(input())

    area = num*num


elif fig == "rectangle":
    num = float(input())
    num1 = float(input())

    area = num * num1

elif fig == "circle":
    num = float(input())
    area = pi*num*num

elif fig == "triangle":
    num = float(input())
    num1 = float(input())

    area = num * num1/2

print(f"{area:.3f}")
