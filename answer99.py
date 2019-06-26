
# 题目099：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。

with open ('i:/test.txt', 'r+') as f:a=f.read()
with open ('i:/test1.txt', 'r+') as f:b=f.read()
a = list(a)
b = list(b)
c = a + b
c.sort()
c = ''.join(c)
with open ('i:/test2.txt', 'w+') as f:f.write(c)