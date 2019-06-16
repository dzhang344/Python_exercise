
# 题目012：判断101-200之间有多少个素数，并输出所有素数。

arr = [2, 3]
lst = []
for i in range(4, 201):
    for j in arr:
        if i % j == 0:
            break
    else:
        arr.append(i)

print(arr)

for i in range(len(arr)):
    if arr[i] > 100:
        lst = arr[i:]
        break
print(lst)