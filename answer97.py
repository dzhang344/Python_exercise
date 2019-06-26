
# 题目097：从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。

path = 'i:/test.txt'
with open(path, 'w+') as f:f.write('')
while 1:
    c = input()
    if c == '#':
        break
    else:
        with open(path, 'a+') as f:f.write(c)