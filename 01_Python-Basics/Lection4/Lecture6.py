word = str(input())

length_word = len(word)

num = 0

for position in range(length_word):
        char = word[position]
        if char == "a" :
            num += 1
        elif char == "e":
            num += 2
        elif char == "i":
            num += 3
        elif char == "o":
            num += 4
        elif char == "u":
            num += 5

print(num)