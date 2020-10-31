product = input()

products = {}

while product != "stop":
    quantity = int(input())

    if product not in products:
        products[product] = 0
    products[product] += quantity

    product = input()

for key, value in products.items():
    print(f"{key} -> {value}")