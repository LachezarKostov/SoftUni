n = int(input())
all_elements = set()

for _ in range(n):
    elements = set(input().split())
    all_elements = all_elements.union(elements)

[print(x) for x in all_elements]

