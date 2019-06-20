# 题目026：利用递归方法求5!。


def fac(x):
    if x > 1:
        return x*fac(x-1)
    else:
        return 1


print(fac(5))