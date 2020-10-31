first_number = int(input())
second_number = int(input())

for i in range(first_number, second_number+1):
    num_to_str = str(i)

    odd_sum = 0
    even_sum = 0

    index = 0
    for dig in num_to_str:
        if index %2 == 0:
            even_sum += int(dig)
        else:
            odd_sum += int(dig)
        index += 1

    if odd_sum == even_sum :
        print(i, end=" ")
