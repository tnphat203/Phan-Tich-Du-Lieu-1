z = 1 + 1j
while abs(z) < 100:
    z = z**2 + 1
print(z)

z = 1 + 1j
while abs(z) < 100:
    if z.imag == 0:
        break
    z = z**2 + 1
print(z)

a = [1, 0, 2, 4]
for element in a:
    if element == 0:
        continue
    print(1. / element)