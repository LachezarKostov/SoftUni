def is_six_to_ten_char(password):
    valid = False
    if 6 <= len(password) <= 10:
        valid = True
    return valid


def is_letters_and_digits(password):
    valid = True
    for char in password:
        ascii = ord(char)
        if (ascii < 48) or (57 < ascii < 65) or (90 < ascii < 97) or (ascii > 122):
            valid = False
            break
    return valid


def is_there_two_digits(password):
    valid = False
    dig_cout = 0

    for char in password:
        ascii = ord(char)
        if 48 <= ascii <= 57:
            dig_cout += 1
        if dig_cout >= 2:
            valid = True

    return valid


def is_valid_password(password):
    valid_1 = is_six_to_ten_char(password)
    valid_2 = is_letters_and_digits(password)
    valid_3 = is_there_two_digits(password)

    if not valid_1:
        print("Password must be between 6 and 10 characters")
    if not valid_2:
        print("Password must consist only of letters and digits")
    if not valid_3:
        print("Password must have at least 2 digits")
    if valid_1 and valid_2 and valid_3:
        print("Password is valid")


password = input()
is_valid_password(password)
