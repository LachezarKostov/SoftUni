skill_to_decipher = input()

while True:
    command = input()

    if command == "For Azeroth":
        break

    if "GladiatorStance" in command:
        skill_to_decipher = skill_to_decipher.upper()
        print(skill_to_decipher)

    elif "DefensiveStance" in command:
        skill_to_decipher = skill_to_decipher.lower()
        print(skill_to_decipher)

    elif "Dispel " in command:
        command = command.split()
        index = int(command[1])
        letter = command[2]

        if index < 0 or index >= len(skill_to_decipher):
            print("Dispel too weak.")
        else:
            # skill_to_decipher = skill_to_decipher[:index] + letter + skill_to_decipher[index+1:]
            skill_to_decipher = skill_to_decipher.replace(skill_to_decipher[index], letter, 1)
            print("Success!")

    elif "Target Change " in command:
        command = command.split()
        substring = command[2]
        sec_substring = command[3]

        skill_to_decipher = skill_to_decipher.replace(substring, sec_substring)
        print(skill_to_decipher)

    elif "Target Remove " in command:
        command = command.split()
        substring = command[2]
        skill_to_decipher = skill_to_decipher.replace(substring, "")
        print(skill_to_decipher)

    else:
        print("Command doesn't exist!")
