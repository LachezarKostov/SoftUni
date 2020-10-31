year = int(input())+1
while True:
    unique = len(set(str(year)))
    if unique == len(str(year)):
        print(year)
        break
    else:
        year += 1
