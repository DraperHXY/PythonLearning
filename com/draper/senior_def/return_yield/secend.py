L = [1, 2, 3, 4]
I1, I2 = iter(L), iter(L)
print(next(I1))
print(next(I2))
print(next(I1))
print(next(I2))
