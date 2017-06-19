def f1():
    # 若前面没有定义 x 单独使用 nonlocal 报错
    x = 1

    def f2():
        nonlocal x
        x = 4
        return

    print(x)
    f2()
    print(x)
    return

# f1()
