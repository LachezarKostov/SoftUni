import re

regex = r"\d+"
res = []

while True:
    text = input()

    if not text:
        break

    matches = re.findall(regex, text)
    res += matches

print(" ".join(res))
