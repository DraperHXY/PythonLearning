def kwonly1(a, *, b, c): print(a, b, c)


# kwonly1(1,2,3) #* 后必须指定关键字
# kwonly1(1, b=2, c=3)


def kwonly2(a, *, b, c=3): print(a, b, c)


# kwonly2(1, b=2)

def kwonly3(a, *b, c=6, **d): print(a, b, c, d)


# kwonly3(1, (2, 3), x=4, y=5)
# kwonly3(1, *(2, 3), c=7, **dict(ddd=1, fff=2))  # dict 里的变量名不要起错
