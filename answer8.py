
# 题目008：题目：输出 9*9 乘法口诀表。

for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            str = '%d*%d=%d' % (i, j, i*j)
            print('%-7s' % str, end='')
    print('')

