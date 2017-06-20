# 过滤，设置一个规则，来过滤
from functools import reduce

print(list(filter(lambda x: x > 0, range(-5, 6))))

# reduce 传递了当前的和或乘积以及列表中的下一个的元素，传给列出的 lambda 函数。默认，序列中的一个元素初始化了起始值。
# 这里是一个队第一个调用的 for 循环的等效，在循环中使用了额外的代码
print(reduce(lambda x, y: x + y, list(range(1, 101))))
print(reduce(lambda x, y: x * y, list(range(1, 5))))
