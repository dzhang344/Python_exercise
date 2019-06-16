
# 题目014：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

num = input('positive number ')
strt = num
num = int(num)
lst = []
for i in range(2, num):
    while num%i == 0:
        lst.append(i)
        num = num//i
    if num == 1:
        break

lst = list(map(str, lst))
mul = '*'
mul = mul.join(lst)
print('%s = %s' % (strt, mul))