import math

count = int(input())
num_min = math.inf
num_max = -math.inf
for position in range(count):

    num = int(input())
    if num < num_min:
        num_min = num

    if num > num_max:
        num_max = num

print(f"""Max number: {num_max}
Min number: {num_min}""")
