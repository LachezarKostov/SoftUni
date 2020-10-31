item_list = input().split(", ")
command = input()

while command != "Craft!":
    tokens_in_list = command.split(" - ")
    command_token = tokens_in_list[0]
    item = tokens_in_list[1]

    if command_token == "Collect":
        if item not in item_list:
            item_list.append(item)

    elif command_token == "Drop":
        if item in item_list:
            item_list.remove(item)

    elif command_token == "Combine Items":
        item_1 = (item.split(":"))[0]
        item_2 = (item.split(":"))[1]

        if item_1 in item_list:
            new_item_index = item_list.index(item_1) + 1
            item_list.insert(new_item_index, item_2)

    elif command_token == "Renew":
        if item in item_list:
            item_list.remove(item)
            item_list.append(item)

    command = input()

item_list_to_str = ", ".join(item_list)
print(item_list_to_str)
