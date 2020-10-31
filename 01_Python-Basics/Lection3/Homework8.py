num = float(input())

is_valid = 100 <= num <= 200 or num == 0

if not is_valid:
    print("invalid")
