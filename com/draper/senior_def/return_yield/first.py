def gensquares(N):
    for i in N:
        yield i ** 2


# for x in gensquares(range(5)):
#     print(x)
#
# func = gensquares(range(5))
# print(dir(func))
# print(help(func))
# print(iter(func))

G = (i * i for i in range(5))
a = iter(G)
b = iter(G)
print(next(a))
print(next(b))
print(next(a))
print(next(b))
