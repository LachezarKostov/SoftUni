word_string = input()
uppercase = []
word_list = [ch for ch in word_string]


for ch in range(0, len(word_list)):
    if word_list[ch].isupper():
        uppercase.append(ch)

print(uppercase)
