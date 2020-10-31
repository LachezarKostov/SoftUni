num = int(input())
is_prime = True

if num > 0:
    for i in range(2, num//2):
        if num % i != 0:
            continue
        else:
            is_prime = False
else:
    is_prime = False

print(is_prime)