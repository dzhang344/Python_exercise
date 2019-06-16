
# 题目005：输入三个整数x,y,z，请把这三个数由小到大输出

x = input('input first number')
y = input('input second number')
z = input('input third number')
array = [int(x), int(y), int(z)]
array = sorted(array)
print(array)