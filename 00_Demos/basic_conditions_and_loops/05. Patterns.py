desired_size = int(input())
direction = 1
cur_size = 0

while cur_size < desired_size or (direction == -1 and cur_size >0):
    cur_size += direction
    print("*" * cur_size)

    if desired_size == cur_size:
        direction = -1
    if cur_size < -desired_size:
        break


