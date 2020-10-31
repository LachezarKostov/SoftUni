def get_factorial_one(num_one):
    factorial_one = 1

    for i in range(1, num_one+1):
        factorial_one = factorial_one*i

    return factorial_one


def get_factorial_two(num_two):
    factorial_two = 1

    for i in range(1, num_two + 1):
        factorial_two = factorial_two * i

    return factorial_two


num_one = int(input())
num_tow = int(input())

res = get_factorial_one(num_one) / get_factorial_two(num_tow)

print(f"{res:.2f}")