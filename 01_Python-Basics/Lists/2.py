n = int(input())
search_word = input()

with_the_word = []
not_with_the_word = []

for _ in range(n):
    adding_string = input()

    if search_word in adding_string:
        with_the_word.append(adding_string)

    else:
        not_with_the_word.append(adding_string)

print(with_the_word)
print(not_with_the_word)




