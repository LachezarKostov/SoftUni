import re

regex = r"\b_([a-zA-Z0-9]+)\b"
res = []

text = input()

res += re.findall(regex, text)

print(",".join(res))
