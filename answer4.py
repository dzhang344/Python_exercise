
# 题目004：输入某年某月某日，判断这一天是这一年的第几天？

import time
dateStr = input('please enter a date mm/dd/yy ')
st = time.strptime(dateStr, '%m/%d/%y')
num = st.tm_yday
print(num)