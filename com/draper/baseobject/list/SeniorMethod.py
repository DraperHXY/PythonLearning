# 括号自动解析

M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

col2 = [raaa[2] for raaa in M]
print(col2)
print([row[1] + 1 for row in M])
print([row[1] for row in M if row[1] % 2 == 0])

diag = [M[i][i] for i in [0, 1, 2]]
print(diag)

doubles = [c * 2 for c in 'spam']
print(doubles)
doubles = [c * 2 for c in ['s', 'p', 'a', 'm']]
print(doubles)

G = (sum(row) for row in M)
print(next(G))
print(next(G))

print(list(map(sum, M)))
print({sum(row) for row in M})
print({i : sum(M[i]) for i in range(3)})
print([ord(x) for x in 'spaam'])
print({ord(x) for x in 'spaam'})
print({x : ord(x) for x in 'spaam'})
