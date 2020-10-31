# from _collections import deque as dq
#
# input_str = input().split('|')
# result = dq()
#
# for i in range(len(input_str)):
#     result.appendleft(input_str[i].split())
#
# [print(" ".join(row), end=" ") for row in result]

lists = [x.split() for x in input().split("|")]

output_list = [elem
               for list in reversed(lists)
               for elem in list]

print(" ".join(output_list))