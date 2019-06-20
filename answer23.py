# 题目023：
# 打印出如下图案（菱形）:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

for i in range(0, 8):
    space = abs((7-i*2)//2)
    print(' '*space + '*'*(7-2*space) + ' '*space)
