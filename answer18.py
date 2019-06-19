# 题目018：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

value = input('please enter a value ')
times = input('please enter times ')
total = 0
for i in range(1, int(times)+1):
    total += int(value*i)

print(total)