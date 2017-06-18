# 杨辉三角
n = input()
L = [1]
for i in range(int(n, 2)):
    for j in L: print(j, end=" ")
    print("\n", end="")
    L.append(0)
    # 列表自动解析，且 第一项
    L = [L[j] + L[j - 1] for j in range(len(L))]

"""
L = [1]
print(L)
L.append(0)
L = [L[0] + L[0 - 1], L[1] + L[0]]
print(L)
L.append(0)
L = [L[0] + L[0 - 1], L[1] + L[0], L[2] + L[1]]
print(L)
"""
