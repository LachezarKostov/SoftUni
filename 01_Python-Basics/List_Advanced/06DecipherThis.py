def parse_to_char(word):
    temp = ""
    for ch in word:
        if not str(ch).isdigit():
            break

        temp += ch

    ascii_value = int(temp)
    char_value = chr(ascii_value)
    new_word = word.replace(temp, char_value)
    return new_word


def replace_in_word(word):
    temp = list(word)
    temp[1], temp[-1] = temp[-1], temp[1]
    return "".join(temp)


word_input = input().split()

res = [(replace_in_word(parse_to_char(word))) for word in word_input]
res = " ".join(res)

print(res)
