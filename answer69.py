# 题目069：有n个人围成一圈，顺序排号。
# 从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
from typing import List

n = 34
count = 0
arr = list(range(1, n+1))
count3List = []
while len(arr+count3List)>1:
    number = arr.pop(0)
    count += 1
    if count % 3 != 0:
        count3List.append(number)
    if len(arr) == 0:
        arr = count3List
        count3List = []

print(arr[0])
