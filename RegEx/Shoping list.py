import re

pattern = r">>([a-zA-Z]+)<<([0-9]+(\.[0-9]+)?)!([0-9]+)"
text = input()
money = 0

print("Bought furniture:")

while text != "Purchase":

    match = re.fullmatch(pattern, text)

    if match is None:
        text = input()
        continue

    print(match[1])
    money += (float(match[2]) * int(match[4]))

    text = input()

print(f"Total money spend: {money:.2f}")
