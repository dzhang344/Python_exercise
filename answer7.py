
# 题目007：将一个列表的数据复制到另一个列表中。

l = [1, 2, 3, 4]
copyl = l.copy()
# another way to copy list
copy2 = l[:]
l.append(5)

print(l)
print(copyl)
print(copy2)