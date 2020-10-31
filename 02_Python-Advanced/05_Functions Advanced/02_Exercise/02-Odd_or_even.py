command = input()
numbers = list(map(int, input().split()))

if command == "Odd":
    result = sum(filter(lambda x: x % 2 == 1, numbers)) * len(numbers)
else:
    result = sum(filter(lambda x: x % 2 == 0, numbers)) * len(numbers)

print(result)