"""
内嵌函数不起作用
因为嵌套作用域中的变量被调用才查找，所以实际上指向了相同的值
"""


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1 = count()
for i in f1:
    print(i())


def count1():
    fs = []
    for i in range(1, 4):
        def f(i):
            def g():
                return i * i

            return g

        fs.append(f(i))
    return fs

# f1, f2, f3 = count1()
# print(f1(), f2(), f3())
