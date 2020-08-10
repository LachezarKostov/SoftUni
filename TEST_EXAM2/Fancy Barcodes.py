from re import findall
count = int(input())

regex = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"

for i in range(count):
    to_print = ""
    barcode = input()
    barcode = findall(regex, barcode)

    if barcode:
        barcode = str(barcode[0])
        for i in barcode:
            if i.isnumeric():
                to_print += i

        if not to_print:
            to_print = "00"

        print(f"Product group: {to_print}")
    else:
        print("Invalid barcode")

