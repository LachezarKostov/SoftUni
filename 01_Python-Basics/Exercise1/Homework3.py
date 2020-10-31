x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

y = abs(y2 - y1)
x = abs(x2 - x1)

area = x * y
per = 2 * x + 2 * y

print(f'{area:.2f}')
print(f'{per:.2f}')