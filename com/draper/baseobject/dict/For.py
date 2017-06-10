D = {'a': 1, 'b': 2, 'c': 3}
print(D)

Ks = list(D.keys())
print(Ks)
Ks.sort()
print(Ks)

for key in Ks:
    print(D[key])
print(D)

for key in sorted(D):
    print(key, '=>', D[key])

for x in 'spamm':
    print(x.upper())

x = 4
while x > 0:
    print('spam!' * x)
    x -= 1

square = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(square)

square = []
for x in [1, 2, 3, 4, 5]:
    square.append(x ** 2)
print(square)

print(D)
D['e'] = 99
print(D)

print('f' in D)

if not 'f' in D:
    print('missing')

value = D.get('x', 0)
print(value)

value = D['x'] if 'x' in D else 0
print(value)

