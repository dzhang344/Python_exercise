# 题目025：求1+2!+3!+...+20!的和。


def fac(x):
    if x > 1:
        return x*fac(x-1)
    else:
        return 1


total = 0
for i in range(1, 21):
    total += fac(i)

print(total)