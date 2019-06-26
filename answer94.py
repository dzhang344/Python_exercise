
# 题目094：时间函数举例4,一个猜数游戏，判断一个人多久猜出来。

import time
import random

expectNum = random.randint(0, 1000)
startT = time.time()
while 1:
    inputNum = int(input('enter a int number '))
    if inputNum > expectNum:
        print('great than')
    elif inputNum < expectNum:
        print('less than')
    else:
        print('correct')
        break
endT = time.time()
print('total time %.2f second' % (endT - startT))