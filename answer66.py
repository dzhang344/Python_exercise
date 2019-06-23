
# 题目066：输入3个数a,b,c，按大小顺序输出。

arr = []
for i in range(3):
    a = input('please enter number ')
    arr.append(int(a))

arr.sort(reverse=True)
print(arr)