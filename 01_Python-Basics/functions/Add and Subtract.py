def sum_numbers(a, b):
    res_one = a + b
    return res_one


def subtract(a, b):
    res_two = a - b
    return res_two


a = int(input())
b = int(input())
c = int(input())

res = subtract(sum_numbers(a, b),c)

print(res)

