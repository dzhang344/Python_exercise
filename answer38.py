# 题目038：求一个3*3矩阵主对角线元素之和。

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = 0
n = len(a)

for i in range(n):
    s += a[i][i]
    s += a[i][n-1-i]

if n % 2 == 1:
    s -= a[n//2][n//2]

print(s)