x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())


boarder = ((x == x1 or x == x2) and (y1 <= y <= y2)) or ((y == y1 or y == y2) and (x1 <= x <= x2))

# inside = (x1 < x < x2) and (y1 < y < y2)

if boarder:
    print("Border")
# elif inside:
 #   print("Inside")
else:
    print("Inside / Outside")

