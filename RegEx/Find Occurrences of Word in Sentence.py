import re
text = input().lower()
word = input().lower()
regex = r"\b"+word+r"\b"
count_list = []

count_list += re.findall(regex, text)

print(len(count_list))

