
# 题目006：斐波那契数列。
array = [0, 1]
for i in range(1, 30):
    array.append(array[i-1] + array[i])

print(array)