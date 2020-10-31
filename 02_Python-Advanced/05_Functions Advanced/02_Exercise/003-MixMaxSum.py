list_of_numbers = list(map(int, input().split()))
min_number = min(list_of_numbers)
max_number = max(list_of_numbers)
sum_of_numbers = sum(list_of_numbers)

print(f"""
The minimum number is {min_number}
The maximum number is {max_number}
The sum number is: {sum_of_numbers}
""")