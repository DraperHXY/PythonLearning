S = 'Span'
print(len(S))
print(S[0])
print(S[1])
print(S[-1])  # 从最后一位
print(S[-2])  # 倒数第二位
print(S[len(S) - 2])  # 与上一行等价
print(S[1:3])  # 一般形式 X[I:J] ,表示“取出在 X 中从偏移量为 I， 直到但不包括偏移量为 J 的内容”
print(S[1:])
print(S[0:3])
print(S[:3])
print(S[:-1])
print(S[:])
print(S)
print(S + 'xyz')
print(S * 8)
print(type(S))