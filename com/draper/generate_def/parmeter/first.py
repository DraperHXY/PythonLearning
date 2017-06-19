def changer1(a, b):
    # a 存在调用函数之中，函数之外没有影响
    a = 2
    # list 是可变对象,实际上 b 并没有被修改，
    b[0] = 'spam'


"""
x = 1
L = [1, 2]
changer1(x, L)
print(x, L)
"""

# 改进上述代码
"""
def changer2(a, b):
    a = 2
    b = ['ddd', 'aaa']


x = 1
L = [1, 2]
changer2(x, L)
print(x, L)
"""


# 参数传参
def f1(a, b, c): print(a, b, c)


"""
f1(1, 2, 3)
f1(b=2, a=1, c=3)
"""


# 默认参数
def f2(a, b=2, c=3): print(a, b, c)


"""
f2(1)
f2(1, c=4)
"""


# 可变参数，传字典
def f3(**args): print(args)


"""
f3()
f3(a=1, b=2)
"""


# 解包参数
def f4(a, b, c, d): print(a, b, c, d)


# 注意解包 dict 的 key 自动作为参数名，不可填错
"""
f4(*(1, 2), **{'c': 1, 'd': 2})
"""
