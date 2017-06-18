s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
print(L[0], L[1], L[2], L[3], sep=" haha ")
for x in L:
    if x in s:
        s.remove(x)
    else:
        s.add(x)


