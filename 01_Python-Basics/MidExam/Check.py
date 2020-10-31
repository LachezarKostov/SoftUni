n = int(input())  # the number of temperatures to analyse

t_positive = [ 10001]
t_negative = [-10001]

t = list(map(int, input().split()))

t_positive += [x for x in t if x > 0]
t_negative += [x for x in t if x < 0]

if min(t_positive) < abs(max(t_negative)) or min(t_positive) == abs(max(t_negative)):

    print(min(t_positive))

if min(t_positive) > abs(max(t_negative)):

    print(max(t_negative))

else:
    print(0)