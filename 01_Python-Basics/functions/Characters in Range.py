def characters_in_range(start, end):

    ord_start = ord(start)
    ord_end = ord(end)
    return_str = ""

    for char in range(ord_start+1, ord_end):
        return_str += chr(char) + " "
    return return_str


a = input()
b = input()

res = characters_in_range(a, b)

print(res)



