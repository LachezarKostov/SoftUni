username = input()

cmd_input = input().split()

while cmd_input[0] != "Sign":
    args = cmd_input
    cmd = args[0].lower()

    if cmd == "case":
        type = args[1]
        if type == "lower":
            username = username.lower()
            print(username)
        elif type == "upper":
            username = username.upper()
            print(username)

    elif cmd == "reverse":
        start_index = int(args[1])
        end_index = int(args[2])
        if 0 <= start_index < end_index < len(username):

            res = username[start_index:end_index+1]
            print(res[::-1])

    elif cmd == "cut":
        substring = args[1]

        if substring not in username:
            print(f"The word {username} doesn't contain {substring}.")
        else:
            username = username.replace(substring, "", 1)
            print(username)

    elif cmd == "replace":
        char = args[1]
        username = username.replace(char, "*")
        print(username)

    elif cmd == "check":
        char = args[1]
        if char in username:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")

    cmd_input = input().split()
