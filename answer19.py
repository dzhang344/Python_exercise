
# 题目019：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

l = []

for i in range(2, 1000):
    total = 0
    for j in range(1, i):
        if i%j == 0:
            total += j
    if i == total:
        l.append(i)

print(l)
