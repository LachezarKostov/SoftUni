text = input()
command = input()

while command != "Reveal":
    command = command.split(":|:")

    if command[0] == "InsertSpace":
        index = int(command[1])
        text = text[:index] + " " + text[index:]

        print(text)

    elif command[0] == "Reverse":
        substring = command[1]
        if substring in text:
            text = text.replace(substring, "", 1)
            substring = substring[::-1]
            text += substring

            print(text)
        else:
            print("error")

    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]

        if substring in text:
            text = text.replace(substring, replacement)

            print(text)
        else:
            print("error")

    command = input()

print(f"You have a new text message: {text}")
