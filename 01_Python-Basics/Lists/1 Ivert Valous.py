text = input()
numbers_str = text.split(" ")
numbers = []

for num_str in numbers_str:
    number = -int(num_str)
    numbers.append(number)

print(numbers)

