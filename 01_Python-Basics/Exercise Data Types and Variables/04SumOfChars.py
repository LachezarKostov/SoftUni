n = int(input())
sumASCII = 0

while n > 0:
    a = input()
    a = ord(a)
    sumASCII += a
    n -= 1

print(f"The sum equals: {sumASCII}")

