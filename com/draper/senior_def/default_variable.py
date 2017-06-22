def server(x=[]):
    x.append(1)
    return x

x = [5]
print(server())
print(server(x))
print(server())
print(server())
print(server())
print(server())