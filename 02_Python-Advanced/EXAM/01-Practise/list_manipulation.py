def list_manipulator(list_of_num, *args):
    from collections import deque as dq
    list_of_num = dq(list_of_num)
    command = args[0]
    where = args[1]
    numbers = dq(args[2:])

    if command == "add":
        if where == "beginning":
            list_of_num = numbers + list_of_num
        elif where == "end":
            list_of_num = list_of_num + numbers

    elif command == "remove":
        if where == "beginning":
            if numbers:
                for _ in range(int(numbers[0])):
                    list_of_num.popleft()
            else:
                list_of_num.popleft()
        elif where == "end":
            if numbers:
                for _ in range(int(numbers[0])):
                    list_of_num.pop()
            else:
                list_of_num.pop()
    return list(list_of_num)
