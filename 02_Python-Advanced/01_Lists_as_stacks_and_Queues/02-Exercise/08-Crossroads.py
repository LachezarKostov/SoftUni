from _collections import deque

green_light = int(input())
free_window = int(input())

cars_waiting = deque()
passed_cars = 0

while True:

    next_command = input()

    if next_command == "green":
        time_remaining = green_light

        while cars_waiting:
            next_car = cars_waiting.popleft()
            time_remaining -= len(next_car)

            if time_remaining < 0:
                if next_car[time_remaining + free_window:]:
                    hot_char = next_car[time_remaining + free_window:][0]
                    print("A crashed happened!")
                    print(f"{next_car} was hit at {hot_char}")
                    exit()
            else:
                passed_cars += 1
                cars_waiting.append(next_car)
                break

    elif next_command == "End":
        print("Everyone is safe.")
        print(f'{passed_cars} total cars passed the crossroads.')
        exit()

