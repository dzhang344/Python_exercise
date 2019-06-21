# 题目031：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
inStr = ''
while 1:
    inStr += input('please enter a letter ')
    arr = []
    for j in week:
        if j[:len(inStr)] == inStr:
            arr.append(j)

    if len(arr) == 1:
        print(arr[0])
        break
    elif len(arr) == 0:
        print('didnot find')
        break