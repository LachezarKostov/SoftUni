import re

count = int(input())
regex = r"!([A-Z][a-z]{3,})!:\[([A-Za-z]{8,})\]"
list_of_numbers = []
for i in range(count):
    msg = input()

    valid_msg = re.fullmatch(regex , msg)

    if valid_msg:
        msg = valid_msg[1]
        for chr in valid_msg[2]:
            list_of_numbers.append(str(ord(chr)))

        list_of_numbers = " ".join(list_of_numbers)
        print(f"{msg}: {list_of_numbers}")
    else:
        print("The message is invalid")