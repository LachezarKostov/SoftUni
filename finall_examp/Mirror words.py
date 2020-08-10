import re

text = input()
count = 0
list_of_pairs = []
regex = r'[#][a-zA-Z]{3,}[#][#][a-zA-Z]{3,}[#]|[@][a-zA-Z]{3,}[@][@][a-zA-Z]{3,}[@]'

pairs = re.findall(regex, text)

for pair in pairs:
    pair_middle = int(len(pair) / 2)
    pair_left = pair[:pair_middle]
    pair_right = pair[pair_middle:]

    if pair_left == pair_right[::-1]:
        list_of_pairs.append(pair_left[1: -1] + " <=> " + pair_right[1: -1])

if pairs:
    print(f"{len(pairs)} word pairs found!")
else:
    print("No word pairs found!")

if list_of_pairs:
    print(f"""The mirror words are:
{", ".join(list_of_pairs)}""")
else:
    print("No mirror words!")
