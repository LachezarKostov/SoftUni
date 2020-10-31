file_name = "test.txt"


with open(file_name, "r") as file:
    file_data = file.readlines()


with open("output.txt", "x") as file:
    for i in range(len(file_data)):
        letters = 0
        comas_and_stuff = 0

        for ch in file_data[i]:
            if ch.isalpha():
                letters += 1
            elif ch != " " and ch != "\'":
                comas_and_stuff += 1

        file.write(f"Line: {i+1}: {file_data[i][:-1]} ({letters}) ({comas_and_stuff}) \n")




