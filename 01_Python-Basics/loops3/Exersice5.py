change = float(input())*100
counter = 0

while change >= 200:
   change -= 200
   counter += 1

while change >= 100:
   change -= 100
   counter += 1

while change >= 50:
   change -= 50
   counter += 1

while change >= 20:
   change -= 20
   counter += 1

while change >= 10:
   change -= 10
   counter += 1

while change >= 5:
   change -= 5
   counter += 1

while change >= 2:
   change -= 2
   counter += 1

while change >= 1:
   change -= 1
   counter += 1

print(counter)
