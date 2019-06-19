# 题目020：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

length = 100

total = length

for i in range(1, 10):
    length = length / 2
    total += length*2

print(total)
print(length/2)