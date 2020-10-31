def odd_even_sum(number):
    odd_sum = 0
    even_sum = 0
    for char in number:
        char = int(char)

        if char % 2 == 0:
            even_sum += char
        else:
            odd_sum += char

    return [even_sum, odd_sum]


num = input()
res = odd_even_sum(num)
print(f"Odd sum = {res[1]}, Even sum = {res[0]}")



