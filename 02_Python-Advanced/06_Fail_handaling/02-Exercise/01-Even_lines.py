symbols = ["-", ",", ".", "!", "?"]

with open("test.txt") as file:
    i = 0
    for line in file:
        if i % 2 == 0:
            for symbol in symbols:
                line = line.replace(symbol, "@")

            line_list = line[:-1].split()
            line_reverse = reversed(line_list)
            line_output = " ".join(line_reverse)

            print(line_output, end="\n")

        i += 1
        