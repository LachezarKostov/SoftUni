Divisor = int(input())
Bound = int(input())

for i in range(Bound, Divisor-1, -1):
    if i % Divisor == 0:
        print(i)
        break
