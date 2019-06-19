
# 题目016：输出指定格式的日期。

import time

print(time.strftime('%m/%d/%y %H:%M:%S', time.localtime()))
print(time.strftime('%m/%d/%y %H:%M:%S', time.gmtime()))
