# 题目051~053、055：
# 学习使用按位与 &
# 学习使用按位或 |
# 学习使用按位异或 ^
# 学习使用按位取反 ~

x = set('runoob')
y = set('google')
print(x, y)          # 重复的被删除 {'n', 'o', 'b', 'u', 'r'} {'o', 'g', 'e', 'l'}
# 集合的交集、并集、差集
print(x & y)         # 交集 {'o'}
print(x | y)         # 并集 {'e', 'o', 'g', 'l', 'u', 'n', 'b', 'r'}
print(x - y)         # 差集 {'n', 'b', 'u', 'r'}
# 当然也可以写成函数形式，不过确实没有上面符号好记。
print(x.intersection(y))
print(x.union(y))
print(x.difference(y))
