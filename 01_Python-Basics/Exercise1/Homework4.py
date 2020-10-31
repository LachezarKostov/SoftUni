num_table = int(input())
x_table = float(input())
y_table = float(input())

area_care = (x_table/2) ** 2

area_top = (x_table + 0.6) * (y_table + 0.6)

price_care = area_care * 9 * num_table
price_top = area_top * 7 * num_table

price_USD = price_care + price_top
price_BGN = price_USD * 1.85

print(f'{price_USD:.2f} USD')
print(f'{price_BGN:.2f} BGN')
