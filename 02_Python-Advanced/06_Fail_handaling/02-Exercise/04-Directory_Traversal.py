import os
import pathlib

directory = input()

directory_dict = {}

for root, dirs, files in os.walk(directory):

    for file in files:
        extension = "." + file.split(".")[-1]

        if extension not in directory_dict:
            directory_dict[extension] = []

        directory_dict[extension].append(file)

output = ""

for extension in (sorted(directory_dict.keys())):
    output += extension + "\n"

    for file in directory_dict[extension]:
        output += f"--- {file} \n "

desktop_path = str(pathlib.Path.home()) + os.path.sep + "Desktop" + os.path.sep + "report.txt"

with open("desktop_path", "x") as file:

    file.write(output)