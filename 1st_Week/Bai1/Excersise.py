pi = 2.
for i in range(1, 100000):
    pi *= 4. * i**2 / (4. * i**2 - 1.)

print(pi)