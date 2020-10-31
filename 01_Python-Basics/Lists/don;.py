arr = input().split()
count = len(arr)//2
isTelescopic = True

for i in range(0, count):
    num_start = int(arr[i])
    num_end = int(arr[-(i+1)])
    num_next = i+1

    if num_start != num_end or num_start != num_next:
        isTelescopic = False

print(isTelescopic)




