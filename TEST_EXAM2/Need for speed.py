number_of_cars = int(input())
garage = {}

for i in range(number_of_cars):
    car_miles_gas = input().split("|")

    garage[car_miles_gas[0]] = [int(car_miles_gas[1]), int(car_miles_gas[2])]

command = input()
while command != "Stop":
    command = command.split(" : ")

    if command[0] == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])

        if garage[car][1] > fuel:
            garage[car][0] += distance
            garage[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if garage[car][0] >= 100000:
                print(f"Time to sell the {car}!")
                garage.pop(car)

        else:
            print("Not enough fuel to make that ride")

    elif command[0] == "Refuel":
        car = command[1]
        fuel = int(command[2])

        if fuel + garage[car][1] >= 75:
            print(f"{car} refueled with {75 - garage[car][1]} liters")
            garage[car][1] = 75

        else:
            garage[car][1] += fuel
            print(f"{car} refueled with {fuel} liters")

    elif command[0] == "Revert":
        car = command[1]
        distance = int(command[2])

        garage[car][0] -= distance
        if garage[car][0] < 10000:
            garage[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {distance} kilometers")

    command = input()

garage = dict(sorted(garage.items(), key=lambda item: (-item[1][0], item[0][0])))

for car in garage:
    print(f"{car} -> Mileage: {garage[car][0]} kms, Fuel in the tank: {garage[car][1]} lt.")
