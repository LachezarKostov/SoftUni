import sys

count = int(input())

sum = 0
max_num = -sys.maxsize

for i in range(0,count):
    num = int(input())
    if num > max_num:
        max_num = num
    sum += num

if max_num == (sum-max_num):
    print(f"Yes\nSum = {max_num}")
else:
    print(f"No\nDiff = {abs(max_num - (sum-max_num))}")
