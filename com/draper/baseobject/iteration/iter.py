l = [line.rstrip(chars='p') for line in open('iteration.py')]
for item in l:print(item)

def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]
