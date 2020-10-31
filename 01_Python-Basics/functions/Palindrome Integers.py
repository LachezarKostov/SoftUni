def is_palidrome(text):
    counter = len(text) // 2
    is_palindrome = True

    for i in range(counter):
        if text[i] != text[len(text) - 1 - i]:
            is_palindrome = False

            break

    return is_palindrome


def solve(items):
    for item in items:
        print(is_palidrome(item))


items = input().split(", ")
solve(items)