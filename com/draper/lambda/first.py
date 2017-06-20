f = lambda x, y, z: x + y + z
print(f(1, 2, 3))


def knights():
    title = 'Sir'
    action = (lambda x: title + " " + x)
    return action


a = knights()
print(a("Betty"))

L = [
    lambda x: x ** 2,
    lambda x: x ** 3,
    lambda x: x ** 4
]

for act in L:
    print(act(2))
print(L[1](3))

key = 'got'

{
    'already': (lambda: 2 + 2),
    'got': (lambda: print(2 * 4)),
    'one': (lambda: 2 ** 6)
}[key]()


def inc(x): return x + 10


print(list(map(inc, [1, 2, 3, 4])))
print(list(map(lambda x: x + 10, [1, 2, 3, 4])))


def mymap(func, seq):
    res = []
    for x in seq: res.append(func(x))
    return res


print(list(mymap(inc, [1, 2, 3, 4])))
print(mymap(inc, [1, 2, 3, 4]))

print(list(map(pow, [1, 2, 3], [2, 3, 4])))


