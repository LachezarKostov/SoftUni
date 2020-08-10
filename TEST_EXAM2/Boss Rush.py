from re import fullmatch

num_of_bosses = int(input())

regex = r'\|([A-Z]{4,})\|:#([A-Za-z]+\s[a-zA-z]+)#'

for _ in range(num_of_bosses):
    boss = input()

    valid_boss = fullmatch(regex, boss)

    if valid_boss:
        print(f"""{valid_boss[1]}, The {valid_boss[2]}
>> Strength: {len(valid_boss[1])}
>> Armour: {len(valid_boss[2])}""")

    else:
        print("Access denied!")