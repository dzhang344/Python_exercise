
# 题目085：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。


oddNum = int(input('please enter a odd number'))
for i in range(1,100):
    num = int('9'*i);
    if num % oddNum == 0:
        print(i)
        break
else:
    print('did not find available number')