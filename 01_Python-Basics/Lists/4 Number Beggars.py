input_list = input().split(", ")
counter = int(input())
beggars_list = []
int_input = []
index = 0

for i in input_list:
    int_input.append(int(i))

for _ in range(counter):
    beggars_list.append(0)

for j in int_input:
    beggars_list[index] += j
    index += 1
    if index == counter:
        index = 0

print(beggars_list)





