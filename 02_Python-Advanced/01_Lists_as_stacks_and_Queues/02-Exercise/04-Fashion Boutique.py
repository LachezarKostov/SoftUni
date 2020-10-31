full_box = list(map(int, input().split(" ")))

rack_cap = int(input())
new_rack = rack_cap
count = len(full_box)
rack_count = 1

while count > 0:
    count -= 1
    cloth = full_box.pop()
    if new_rack - cloth >= 0:
        new_rack -= cloth
    else:
        full_box.append(cloth)
        rack_count += 1
        new_rack = rack_cap
        count += 1

print(rack_count)

