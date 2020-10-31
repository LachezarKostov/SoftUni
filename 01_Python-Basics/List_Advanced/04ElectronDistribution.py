total_electron = int(input())

res = []
shield_index = 1

while total_electron > 0:
    value = 2 * shield_index ** 2

    if total_electron < value:
        res.append(total_electron)
    else:
        res.append(value)

    total_electron -= value
    shield_index += 1

print(res)

