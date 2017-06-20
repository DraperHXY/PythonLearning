def func(a):
    b = 'spam'
    return a * b


print(func(3))
print(dir(func))
print(func.__name__)
print(func.__code__)
print(func)
print(dir(func.__code__))
print(func.__code__.co_name)
print(func.__code__.co_varnames)
print(func.__code__.co_argcount)
print(func.__code__.co_code)
print(func.__code__.__str__)

# 模拟其他语言的静态变量，变量的名称对于一个函数来说是本地的

print(dir(func))
func.count = 0
func.count += 1
print(dir(func))
