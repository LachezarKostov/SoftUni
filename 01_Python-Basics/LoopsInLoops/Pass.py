n = int(input())
l = int(input())

for first_symbol in range(1, n+1):
    for second_symbol in range(1, n+1):
        for third_symbol in range(97, 97+l):
            for forth_symbol in range(97, 97 + l):
                for fifth_symbol in range(1, n+1):
                    if fifth_symbol>first_symbol and fifth_symbol>second_symbol:
                        password =str(first_symbol)+\
                                  str(second_symbol)+\
                                  chr(third_symbol)+\
                                  chr(forth_symbol)+\
                                  str(fifth_symbol)
                        print(password, end=" ")