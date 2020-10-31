n = int(input())

for i in range(1111, 10000):
    count_str = 0
    count = 0
    i_str = str(i)
    for j in i_str:
        count_str += 1
        j = int(j)
        if j != 0:
            if n % j == 0:
                count += 1
    if count == count_str:
        print(i, end=" ")









