list_of_char = input().split(", ")

ASCII_dic = {x:ord(x) for x in list_of_char}

print(ASCII_dic)