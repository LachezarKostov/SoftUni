input_str = input()
vowels = ["a", "o", "u", "e", "i"]

no_vowels = [x for x in input_str if x not in vowels]
print("".join(no_vowels))