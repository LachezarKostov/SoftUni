tt = (1, 2, 3)
tt2 = 1, 2, 3

print(tt == tt2)

one_element_tt = (1,)

x, y, z = tt
print(x, y, z)

x, *rest = tt

print(x)
print(rest)