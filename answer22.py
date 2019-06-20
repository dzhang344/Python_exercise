# 题目022：两个乒乓球队进行比赛，各出三人。
# 甲队为a,b,c三人，乙队为x,y,z三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。
# a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

import itertools

jia = ['a', 'b', 'c']
yi = ['x', 'y', 'z']

arr = list(itertools.permutations(yi, 3))
arr = [[jia[i]+a[i] for i in range(3)] for a in arr]
for i in arr:
    if 'ax' in i:
        pass
    elif 'cx' in i or 'cz' in i:
        pass
    else:
        print(i)