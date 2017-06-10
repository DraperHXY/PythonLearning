x = 1
print(x << 2)  # 100 = 4
print(x | 2)  # 001 | 010 = 011 = 3
print(x & 1)  # 001 & 001 = 001 = 1

x = 0b0001
print(bin(x << 2))  # 0b100 = 4
print(bin(x | 0b010))  # 0b11
print(bin(x & 0b1))  # 0b1

X = 0xFF
print(bin(X))
print(X ^ 0b10101010)
print(bin(X ^ 0b10101010))
print(int('1010101', 2))
print(hex(85))
