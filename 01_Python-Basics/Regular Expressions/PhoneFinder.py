import re
phones = input()
pattern = r"(\+359-2-\d{3}-\d{4}|\+359 2 \d{3} \d{4})\b"
matches = re.findall(pattern, phones)

print(", ".join(matches))