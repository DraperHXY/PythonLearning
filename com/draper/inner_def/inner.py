# p433 上错误示例
def f1():
    x = 99

    def f2():
        def f3():
            print(x)
        f3()
    f2()

f1()
