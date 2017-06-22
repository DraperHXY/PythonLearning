def func(x, y):
    return x * y


print(list(map(func, [1, 2, 3, 4, 5], [8, 7, 6, 5, 4])))


def mymap(func, *list):
    res = []
    for args in zip(*list):
        res.append(func(*list))

    return res


def myzip(*seqs):
    seqs = [list(s) for s in seqs]
    while all(seqs):
        yield tuple(s.pop(0) for s in seqs)


s1, s2 = 'abc', 'xyz123'
print(list(myzip(s1, s2)))
