number_line = list(map(int, (input().split())))

command = input().split()

while command[0] != "end":

    if command[0] == "swap":
        index_1 = int(command[1])
        index_2 = int(command[2])
        if index_1 > index_2:
            num_1 = number_line.pop(index_1)
            num_2 = number_line.pop(index_2)
            number_line.insert(index_2, num_1)
            number_line.insert(index_1, num_2)
        else:
            num_2 = number_line.pop(index_2)
            num_1 = number_line.pop(index_1)
            number_line.insert(index_1, num_2)
            number_line.insert(index_2, num_1)


    elif command[0] == "multiply":

        index_1 = int(command[1])
        index_2 = int(command[2])
        if index_1 > index_2:
            num_1 = number_line.pop(index_1)
            num_2 = number_line.pop(index_2)
            number_line.insert(index_2, num_2)
            number_line.insert(index_1, num_1 * num_2)


        else:
            num_2 = number_line.pop(index_2)
            num_1 = number_line.pop(index_1)
            number_line.insert(index_1, num_1 * num_2)
            number_line.insert(index_2, num_2)



    elif command[0] == "decrease":

        number_line = [x - 1 for x in number_line]

    command = input().split()

print(", ".join(list(map(str, number_line))))
