str_numbers = input().split()
counter = int(input())
numbers = []

for num in str_numbers:
    num = int(num)
    numbers.append(num)

for _ in range(counter):
   numbers.remove(min(numbers))

print(numbers)

