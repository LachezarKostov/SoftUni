n = int(input())

for one in range(1, 10):
    for two in range(1, 10):
        for three in range(1, 10):
             for four in range(1, 10):
                 if n % one == 0 and \
                    n % two == 0 and \
                    n % three == 0 and \
                    n % four == 0:
                        number = (str(one)+str(two)+str(three)+str(four))
                        print(number, end=" ")