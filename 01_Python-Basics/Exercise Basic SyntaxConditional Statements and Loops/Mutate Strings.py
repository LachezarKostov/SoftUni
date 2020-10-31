string1 = input()
string2 = input()
new_string = ''
for i in range(len(string2)):
    if string1[i] != string2[i]:
        new_string = string2[:i+1]+string1[i+1:]
        print(new_string)


