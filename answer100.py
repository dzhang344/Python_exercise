
# 题目100：列表转换为字典。

l = ['ert', 'ddd', 'ffff']
d = {}

for i in range(len(l)):
    d[str(i)] = l[i]

print(d)