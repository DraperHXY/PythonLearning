T = (1, 2, 3, 4)
print(len(T))
print(T + (5, 6))
print(T[0])
print(T.index(4))  # 查找 4 的 index
print(T.count(4))  # 4 出现的次数

T = ('spam', 3.0, [11, 22, 33])
print(T)
print(T[2][1])
print(type(T))