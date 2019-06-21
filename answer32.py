# 题目032：按相反的顺序输出列表的值。

# 方法一
a = [1, 2, 3, 4, 5]
print(a[::-1])
# 方法二
a = [1, 2, 3, 4, 5]
a.reverse()
print(a)
# 方法三
a = [1, 2, 3, 4, 5]
a.sort(reverse=True)
print(a)
