numbers = list(map(int, input().split()))

average = sum(numbers) / len(numbers)

greater_nums = [x for x in numbers if x > average]

greater_nums.sort()
greater_nums.reverse()

if len(greater_nums) > 5:
    for _ in range(len(greater_nums) - 5, 0, -1):
        greater_nums.pop()

greater_nums = list(map(str, greater_nums))

if len(greater_nums) == 0:
    print("No")
else:
    print(" ".join(greater_nums))
