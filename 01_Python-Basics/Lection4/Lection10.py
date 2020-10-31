n = int(input())
num = 0
odd = 0
even = 0

for i in range(1, n+1):
    num = int(input())

    if i % 2 == 0:
        odd += num
    else:
        even += num

if even == odd:
    print(f"Yes\n Sum = {odd}")
else:
    print(f"No\n Diff = {abs(odd-even)}")

