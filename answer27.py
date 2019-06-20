# 题目027：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。


def convertOutput(x):
    if len(x) > 1:
        anX = x[:len(x)-1]
        return x[len(x)-1] + convertOutput(anX)
    else:
        return x


stringInput = input('list of charactor ')
print(convertOutput(stringInput))