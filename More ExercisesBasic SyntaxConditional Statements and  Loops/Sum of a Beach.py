string = input().lower()
count = 0
cicle_true = True

while cicle_true:
    if "water" in string:
        count += 1
        string = string.replace("water", "", 1)
    elif "fish" in string:
        string = string.replace("fish", "", 1)
        count += 1
    elif "sun" in string:
        string = string.replace("sun", "", 1)
        count += 1
    elif "sand" in string:
        string = string.replace("sand", "", 1)
        count += 1
    else:
        cicle_true = False

print(count)
