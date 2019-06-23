
# 题目049：使用lambda来创建匿名函数。

# lambda函数也叫匿名函数，即，函数没有具体的名称。先来看一个最简单例子


def f(x):
    return x**2


print(f(4))

# Python中使用lambda的话，写成这样
g = lambda x:x**2
print(g(4))

# lambda存在意义就是对简单函数的简洁表示。
# lambda语句中，冒号前是参数，可以有多个，用逗号隔开，冒号右边的返回值。
# 常搭配内置函数map、filter、reduce，都是应用于序列的内置函数。常见的序列包括list、tuple、str。
# map(func, *iterables) --> map object
# filter(function or None, iterable) --> filter object
# reduce(function, sequence[, initial]) -> value
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print(list(map(lambda x: x * 2 + 10, foo)))       # 映射 [14, 46, 28, 54, 44, 58, 26, 34, 64]
print(list(filter(lambda x: x % 3 == 0, foo)))    # 过滤 [18, 9, 24, 12, 27]
from functools import reduce                      # 在Python 3里,reduce()函数已经被从全局名字空间里移除了,它现在被放置在fucntools模块里
print(reduce(lambda x, y: x + y, foo))            # 累积 139
