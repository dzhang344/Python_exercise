
# 题目071：编写input()和output()函数输入，输出5个学生的数据记录。


def inp(data):
    name = input('enter student name ')
    score = input('enter student score ')
    data[name] = score
    print('enter success')
    return data


def outp(data):
    name = input('enter student name ')
    print('student score: ', data[name])


if __name__ == '__main__':
    data = {}
    while 1:
        a = input('i/o student score ')
        if a == 'i':
            data = inp(data)
        elif a == 'o':
            outp(data)
        elif a == 'break':
            break
        else:
            print('output is not correct')