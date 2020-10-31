a = int(input())
b = int(input())

print(f"""Before:
a = {a}
b = {b}""")

c = 0
c = a
a = b
b = c


print(f"""After:
a = {a}
b = {b}""")