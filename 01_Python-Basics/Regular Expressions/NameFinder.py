import re
names = input()
pattern = r"([A-Z][a-z]+\s[A-Z][a-z]+ )"
matches = re.findall(pattern, names)

print("".join(matches))