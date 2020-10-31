import sys

count = int(input())

oddmin = sys.maxsize
oddmax = -sys.maxsize
oddsum = 0
evenmin = sys.maxsize
evenmax = -sys.maxsize
evensum = 0

for i in range(0, count):
    num = float(input())
    if i%2 != 0:
        evensum += num
        if num > evenmax:
            evenmax = num
        if num < evenmin:
            evenmin = num
    else:
        oddsum += num
        if num > oddmax:
            oddmax = num
        if num < oddmin:
            oddmin = num

print(f"OddSum={oddsum:.2f},")

if oddmin < sys.maxsize:
    print(f"OddMin={oddmin:.2f},")
else:
    print("OddMin=No,")

if oddmax > -sys.maxsize:
    print(f"OddMax={oddmax:.2f},")
else:
    print("OddMax=No,")

print(f"EvenSum={evensum:.2f},")

if evenmin < sys.maxsize:
    print(f"EvenMin={evenmin:.2f},")
else:
    print("EvenMin=No,")

if evenmax > -sys.maxsize:
    print(f"EvenMax={evenmax:.2f}")
else:
    print("EvenMax=No")

