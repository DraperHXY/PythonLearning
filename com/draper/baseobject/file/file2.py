X, Y, Z = 43, 44, 45
S = 'Spam'
D = {'a': 1, 'b': 2}
L = [1, 2, 3]

file = open("file2.txt",'w')
file.write(S +'\n')
file.write('{0},{1},{2}'.format(L,D,Z))
file.close()

file = open('file2.txt')
line = file.readline()
print(repr(line))
print(repr(line.rstrip()))
print(line)