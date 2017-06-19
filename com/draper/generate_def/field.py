var = 99


# 本地变量
def local():
    var = 0
    print("local()")


def glob1():
    # 设置全局变量
    global var
    var += 1
    print("global1()")


def glob2():
    var = 0
    print("global2() import 前")
    # 导入的全局变量
    import field
    field.var += 1
    print("global2() import 后")

# def glob3():
#     var = 0
#     # 导入的全局变量
#     import sys
#     glob = sys.modules["field"]
#     glob.var += 1


def glob4():
    var = 0
    print("global4() import 前")
    # 导入的全局变量
    import field
    field.var += 1
    print("global4() import 后")



def glob5():
    var = 0
    print("global5() import 前")
    # 导入的全局变量
    import field
    field.var += 1
    print("global5() import 后")



def test():
    print(var)  # 99
    local()
    glob1()  # 99 + 1 = 100
    glob2()  # 导入 101
    # glob3()
    glob4()  # 导入 102
    glob5()  # 导入 103
    print(var)

