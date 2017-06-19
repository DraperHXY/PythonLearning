def minmax(test, *args):
    res = args[0]
    for i in args[1:]:
        if test(i, res):
            res = i
    return res


def lessthan(x, y): return x < y


def grtrthan(x, y): return x > y


print(minmax(lessthan, 4, 2, 1, 5, 6, 3))
print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))
