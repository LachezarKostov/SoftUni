a = int(input())
b = int(input())
n = int(input())
count = 0
breaker = False
for i in range(a, b+1):
        for j in range(a, b+1):
            count += 1
            if i+j == n:
                breaker = True
                print(f"Combination N:{count} ({i} + {j} = {i+j})")
                break
        if breaker:
            break
if not breaker:
    print(f"{count} combinations - neither equals {n}")


