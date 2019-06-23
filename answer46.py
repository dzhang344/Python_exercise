
# 题目046：求输入数字的平方，如果平方运算后小于 50 则退出。


import math

while 1:
    num = input('please enter a number ')
    num = int(num)
    sq = math.pow(num, 2)
    print(sq)
    if sq < 50:
        break

