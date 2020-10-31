n = int(input())
even = []
odd = []
negative = []
positive = []

while True:
    number = input()

    if number == "even":
        print(even)
        break

    if number == "odd":
        print(odd)
        break

    if number == "negative":
        print(negative)
        break

    if number == "positive":
        print(positive)
        break

    number = int(number)

    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)

