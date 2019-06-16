
# 题目010：暂停一秒输出，并格式化当前时间。

import time

a = time.strftime('%m/%d/%Y %H:%M:%S', time.localtime(time.time()))
print(a)
time.sleep(1)
b = time.strftime('%m/%d/%Y %H:%M:%S', time.localtime(time.time()))
print(b)