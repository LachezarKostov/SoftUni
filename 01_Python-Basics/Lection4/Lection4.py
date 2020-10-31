n = int(input())

num = 0

for power in range(0, n+1, 2):
    num = 2 ** power
    print(num)
