import re

regex = r"(\bwww.[a-zA-Z0-9-]+(\.[a-z]+)+\b)"

while True:
    text = input()

    if not text:
        break

    valid_site = re.findall(regex, text)

    if valid_site:
        print(valid_site[0][0])

