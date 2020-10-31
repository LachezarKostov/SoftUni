rows = int(input())

list_2 = []
for i in range(0, rows):
    coff = 1

    for k in range(0, i + 1):
        list_1 = []
        coff = int(coff * (i - k) / (k + 1))
        list_1.append(coff)
        list_2.append(list_1)

print(list_2)

# rows = int(input("Enter the number of rows : "))
# for i in range(0, rows):
#     coff = 1
#     for j in range(1, rows - i):
#         print("  ", end="")
#
#     for k in range(0, i + 1):
#         print("  ", coff, end="")
#         coff = int(coff * (i - k) / (k + 1))
#     print()