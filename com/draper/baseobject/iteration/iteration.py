a = list(range(5))
print(a)
for x in a: print(x, end=" ")
print("\n")
l = iter(a)
print(l.__next__())
print(l.__next__())
print(l.__next__())
print(l.__next__())
print(l.__next__())