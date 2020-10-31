n = int(input())

for a in range(0, n):
    for b in range(0, n ):
        for c in range(0, n):
            print(chr(a+97)+chr(b+97)+chr(c+97))