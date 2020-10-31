n = int(input())
sum1 = 0
sum2 = 0

for i in range(1, n+1):
    num = int(input())
    sum1 += num
for i in range(n+1, (2*n+1)):
    num = int(input())
    sum2 += num

if sum1 == sum2:
    print(f"Yes, sum = {sum1}")
else:
    print(f"No, diff = {abs(sum1-sum2)}")