S = 'Spam'

print(S[0])

# 这一步报错， String 是不可变的对象
# S[0] = 'z'

S = 'Z' + S[1:]
print(S)
print(S.find('pa'))
print(S.replace('pa', 'XYZ'))

line = 'aaa,bbb,ccccc,dd'
print(line.split(','))

print(S.upper())
print(line.rstrip())

# 高级的格式化操作
print('%s, eggs and %s' % ('spam', 'SPAM!'))
print('{0}, eggs, and {1}'.format('spam', 'SPAM!'))

# 以及寻求帮助
print(dir(S))
print(help(S.replace))  # 注意不用带括号
