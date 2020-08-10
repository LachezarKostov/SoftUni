text = input()
command = input().split()

while command[0] != "Finish":

    if command[0] == "Replace":
        current_char = command[1]
        new_char = command[2]
        text = text.replace(current_char, new_char)
        print(text)

    elif command[0] == "Cut":
        start_index = int(command[1])
        end_index = int(command[2])
        len_text = len(text)

        if 0 <= start_index <= len_text and 0 <= end_index <= len_text:
            text = text[:start_index] + text[end_index+1:]
            print(text)
        else:
            print("Invalid indexes!")

    elif command[0] == "Make":
        upper_lower = command[1]
        if upper_lower == "Upper":
            text = text.upper()
        else:
            text = text.lower()
        print(text)

    elif command[0] == "Check":
        is_string = command[1]
        if is_string in text:
            print(f"Message contains {is_string}")
        else:
            print(f"Message doesn't contain {is_string}")

    elif command[0] == "Sum":
        start_index = int(command[1])
        end_index = int(command[2])
        len_text = len(text)
        sum_of_ascii = 0

        if 0 <= start_index <= len_text and 0 <= end_index <= len_text:
            sum_to_add_from_str = text[start_index:end_index+1]
            for i in sum_to_add_from_str:
                sum_of_ascii += ord(i)
            print(sum_of_ascii)

        else:
            print("Invalid indexes!")

    command = input().split()


