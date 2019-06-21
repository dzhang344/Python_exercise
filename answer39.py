# 题目039：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

aaa = [1, 5, 8, 14, 28, 39, 60, 89, 134, 324, 612, 900]
b = 1000

for i in range(len(aaa)):
    if aaa[i] > b:
        aaa.insert(i, b)
        break
else:
    aaa.append(b)

print(aaa)
