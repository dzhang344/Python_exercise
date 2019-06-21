# 题目037：对10个数进行排序。

#bubble sort
a = [1, 5, 7, 3, 2, 4, 9, 10, 6, 8]

n = len(a)

for j in range(n-1):
    for i in range(n-1-j):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]


print(a)
