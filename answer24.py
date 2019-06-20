# 题目024：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

#l = [1, 2]
# total = 0
# for i in range(20):
#     total += l[i+1]/l[i]
#     l.append(l[i]+l[i+1])
#
# print(total)

a,b,num = 2,1,0
for i in range(20):
    num+=a/b
    a=a+b
    b=a-b
print(num)