list_of_numbers = list(map(int, input().split()))
even_numbers = list(filter(lambda x: x % 2 == 0, list_of_numbers))
print(even_numbers)
