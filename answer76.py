# 题目076：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n

inputNum = input('enter number')
inputNum = int(inputNum)

numberList = range(inputNum, 0, -2)

s = sum([1/i for i in numberList])
print(s)