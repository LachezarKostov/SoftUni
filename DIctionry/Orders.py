order = input()
order_dict = {}

while order != "buy":
    name, price, quantity = order.split()

    if name not in order_dict:
        order_dict[name] = [float(price), int(quantity)]
    else:
        order_dict.get(name)[0] = float(price)
        order_dict.get(name)[1] += int(quantity)
    order = input()

for name, price in order_dict.items():
    total_price = price[0]*price[1]
    print(f"{name} -> {total_price:.2f}")

