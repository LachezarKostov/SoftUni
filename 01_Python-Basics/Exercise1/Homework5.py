import math

L = float(input())
W = float(input())
A = float(input())

free_area = ((L*100)*(W*100)) - (((A*100) ** 2)+((L*100)*(W*100))/10)

num = free_area/(40+7000)
num = math.floor(num)
print(num)

