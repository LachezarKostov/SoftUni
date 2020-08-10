num = input()
num_list = []

for num in num:
    num_list.append(num)

num_list.sort(reverse=True)
big_num = "".join(num_list)

print(big_num)