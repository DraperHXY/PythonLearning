S = 'Spam'

print(S[0])

# 这一步报错， String 是不可变的对象
# S[0] = 'z'

S = 'Z' + S[1:]
print(S)
print(S.find('pa'))
print(S = S.replace('pa', 'XYZ'))

