def func():
    x = 4
    action = (lambda n: x ** n)
    return action


# action = func()
# print(action(2))


def make_actions():
    acts = []
    for i in range(5):
        # 在这一步传入默认的参数
        # 默认参数在函数创建时确定，而不是在最后调用的时候
        acts.append(lambda x, i=i: i ** x)
    return acts


acts = make_actions()
for a in acts:
    print(a(2))
