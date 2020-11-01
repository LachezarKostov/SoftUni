GROWING: int = 1  # GLOBAL namespace
SHRINKING: int = -1


def print_rhombus(n: int):  # GLOBAL namespace
    def print_line(i: int, direction: int):  # local namespace: visible in print_rhombus
        if i == 0:
            return
        line = " " * (n - i) + "* " * i
        print(line.rstrip())
        if i == n:
            direction = SHRINKING
        print_line(i + direction, direction)  # recursion

    print_line(1, GROWING)


print_rhombus(int(input()))
