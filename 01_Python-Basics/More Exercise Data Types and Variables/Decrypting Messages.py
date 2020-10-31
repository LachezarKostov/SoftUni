key = int(input())
num_of_lines = int(input())
msg = ""

for _ in range(num_of_lines):
    characters = ord(input())
    new_char = chr(characters + key)
    msg += new_char

print(msg)
