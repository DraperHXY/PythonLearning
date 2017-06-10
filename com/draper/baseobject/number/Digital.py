import math
import random

# 高级的数学工具，以及少见的数学对象 复数
# 固定精度十进制数、有理数、集合、布尔值、
# 第三方领域更多(矩阵和向量)

print(123 + 222)
print(1.5 * 3)
print(2 ** 100)
print(len(str(2 ** 100000)))
print(3.1315 * 2)
print(math.pi)
print(math.sqrt(85))
print(random.random())
print(random.choice([1, 2, 3, 4]))

print(0o1, 0o20, 0o377)
print(0x01, 0x10, 0xff)
print(0b1, 0b10000, 0b11111111)
print(oct(64), hex(64), bin(64))
print(int('64'), int('100', 8), int('40', 16), int('1000000', 2))
print(int('0x40', 16), int('0b1000000', 2))
# print(eval('64', 16), eval('0o100'), eval('0x40'), eval('0b1000000'))
x = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
print(x)
print(oct(x))
print(bin(x))
