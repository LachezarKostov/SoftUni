skill_to_decipher = input()

while True:
    command = input()

    if command == "For Azeroth":
        break

    command = command.split()

    if len(command) == 1 and command[0] == "GladiatorStance":
        skill_to_decipher = skill_to_decipher.upper()
        print(skill_to_decipher)

    elif len(command) == 1 and command[0] == "DefensiveStance":
        skill_to_decipher = skill_to_decipher.lower()
        print(skill_to_decipher)

    elif len(command) == 3 and command[0] == "Dispel":
        index = int(command[1])
        letter = command[2]

        if index < 0 or index > len(skill_to_decipher):
            print("Dispel too weak.")
        else:
            skill_to_decipher = skill_to_decipher.replace(skill_to_decipher[index], letter)
            print("Success!")

    elif len(command) == 4 and command[0] == "Target" and command[1] == "Change":
        substring = command[2]
        sec_substring = command[3]

        skill_to_decipher = skill_to_decipher.replace(substring, sec_substring)
        print(skill_to_decipher)

    elif len(command) == 3 and command[0] == "Target" and command[1] == "Remove":
        substring = command[2]
        skill_to_decipher = skill_to_decipher.replace(substring, "")
        print(skill_to_decipher)

    else:
        print("Command doesn't exist!")
