n = int(input())

longest_intersection = set()
best_length = 0

for _ in range(n):
    ranges = input().split("-")
    first_range_start, first_range_end = map(int, ranges[0].split(","))
    second_range_start, second_range_end = map(int, ranges[1].split(","))

    first_set = set([x for x in range(first_range_start, first_range_end + 1)])
    second_set = set([x for x in range(second_range_start, second_range_end + 1)])

    intersection = first_set.intersection(second_set)

    if len(intersection) > best_length:
        best_length = len(intersection)
        longest_intersection = intersection


print(f"Longest intersection is [{', '.join([str(x) for x in longest_intersection])}] with length {best_length}")
