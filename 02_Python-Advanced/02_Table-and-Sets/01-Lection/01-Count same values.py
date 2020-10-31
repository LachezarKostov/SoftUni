def count_numbers(values):
    values_count = {}

    for value in values:
        if value not in values_count:
            values_count[value] = 0
        values_count[value] += 1

    return values_count


def print_result(values_count):
    for (value, count) in values_count.items():
        print(f'{value} - {count} times')


result = count_numbers(map(float, input().split(" ")))
print_result(result)
