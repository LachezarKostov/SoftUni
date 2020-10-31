floors = int(input())
rooms = int(input())

for current_floor in range (floors, 0 , -1):
    for current_room in range (0, rooms, 1):
        if current_floor == floors:
            print(f"L{current_floor}{current_room}", end=" ")
        elif current_floor % 2 == 0:
            print(f"O{current_floor}{current_room}", end=" ")
        elif current_floor % 2 == 1:
            print(f"A{current_floor}{current_room}", end=" ")
    print()
