# 题目030：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

num = 12321
s = str(num)

for i in range(len(s)//2):
    if s[i] != s[-i-1]:
        print(False)
        break

else:
    print(True)