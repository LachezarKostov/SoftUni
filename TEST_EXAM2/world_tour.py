places_to_go = input()

while True:
    commands = input().split(":")
    if commands[0] == "Travel":
        break

    if commands[0] == "Add Stop":
        index = int(commands[1])
        string = commands[2]
        if 0 <= index < len(places_to_go):
            places_to_go = places_to_go[:index] + string + places_to_go[index:]

    elif commands[0] == "Remove Stop":
        start_index = int(commands[1])
        end_index = int(commands[2])
        if 0 <= start_index <= end_index < len(places_to_go):
            places_to_go = places_to_go[:start_index] + places_to_go[end_index+1:]

    elif commands[0] == "Switch":
        old_string = commands[1]
        new_string = commands[2]
        places_to_go = places_to_go.replace(old_string, new_string)

    print(places_to_go)

print(f"Ready for world tour! Planned stops: {places_to_go}")