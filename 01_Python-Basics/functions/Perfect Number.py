def is_perfect(num):
    num = int(num)
    dividers = []
    for divider in range(1, num//2+1):
        if num % divider == 0:
            dividers.append(divider)

    if sum(dividers) == num:
        return True


number = input()
if is_perfect(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")


