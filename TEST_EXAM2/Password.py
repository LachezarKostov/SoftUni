import re

regex = r"(^.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1$"
count = int(input())

for _ in range(count):
    password = input()
    valid_password = ""
    valid_password = re.fullmatch(regex, password)

    if valid_password:
        print(f"Password: {valid_password[2]+valid_password[3]+valid_password[4]+valid_password[5]}")
    else:
        print("Try another password!")