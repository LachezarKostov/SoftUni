words = input().split(", ")

words = [word + (" -> " + str(len(word))) for word in words]

print(", ".join(words))
