from _collections import deque

n = int(input())
pumps = deque()

for _ in range(n):
    pump = [int(x) for x in input().split()]
    pumps.append(pump)

for i in range(n):
    is_valid = True
    fuel = 0
    for _ in range(n):
        current = pumps.popleft()
        fuel += current[0] - current[1]
        if fuel < 0:
            is_valid = False
        pumps.append(current)
    if is_valid:
        print(i)
        break
    pumps.append(pumps.popleft())

# from _collections import deque
#
# total_pumps = int(input())
#
# pumps = deque()
# temp_deque = deque()
#
# for i in range(total_pumps):
#     pumps_info = list(map(int, input().split(" ")))
#     pumps.append(pumps_info[0] - pumps_info[1])
#
# total_fuel = 0
# current_inx = 0
#
# while pumps:
#     if total_fuel < 0:
#         while temp_deque:
#             pumps.append((temp_deque.popleft()))
#
#         current_inx += 1
#
#         if current_inx == total_pumps:
#             break
#
#     pump = pumps.popleft()
#     temp_deque.append(pump)
#
#     total_fuel += pump
#
# print(current_inx)