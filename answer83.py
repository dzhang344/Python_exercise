
# 题目083：求0—7所能组成的奇数个数。

s = [i for i in '01234567']
import itertools
arr = []
for i in range(1, 9):
    a = list(itertools.permutations(s, i))
    l = list(map(lambda x:int(''.join(x)), a))
    arr += l
    print(i, len(l))

arr1 = set(arr)
arr2 = list(filter(lambda x:x%2==1, arr1))
print(len(arr2))