s = 'spamm'
z = zip([ord(c) for c in s], [c for c in s])
for line in z: print(line[0], ":", line[1])
