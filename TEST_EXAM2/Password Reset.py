password = input()
command = input().split()
temp_pass = ""
while command[0] != "Done":

    if command[0] == "TakeOdd":
        for oddindex in range(1, len(password), 2):
            temp_pass += password[oddindex]
        password = temp_pass
        print(password)

    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        str_to_remove = password[index:length+index]
        password = password.replace(str_to_remove, "", 1)
        print(password)

    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    command = input().split()

print(f"Your password is: {password}")
