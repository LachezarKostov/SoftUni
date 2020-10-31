n = int(input())
total_free_chairs = 0
has_enough_chairs = True

for i in range(1, n + 1):
    room_data = input().split()
    charis_count = len(room_data[0])
    number_of_people = int(room_data[1])

    if charis_count >= number_of_people:
        total_free_chairs += charis_count - number_of_people

    else:
        has_enough_chairs = False
        print(f"{number_of_people - charis_count} more chairs needed in room {i}")

if has_enough_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")
