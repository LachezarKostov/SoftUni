import math

nums = list(map(int, input().split(", ")))

max_num = max(nums)
number_of_groups = int(math.ceil(max_num / 10))

for i in range(1, number_of_groups + 1):
    current_range = [num for num in nums if i * 10 - 10 < num <= i * 10]
    # current_range = []
    # for num in nums:
    #   if i * 10 - 10 < num <= i * 10:
    #        current_range.append(num)

    print(f"Group of {i}0's: {current_range}")
