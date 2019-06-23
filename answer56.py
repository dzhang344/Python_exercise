# 题目056：画图，学用circle画圆形。
# # 题目057：画图，学用line画直线。
# # 题目058：画图，学用rectangle画方形。
# # 题目059：画图，综合例子。
# # 题目063：画椭圆。
# # 题目064：利用ellipse 和 rectangle 画图。
# # 题目065：一个最优美的图案。　

import tkinter
canvas = tkinter.Canvas(width=600, height=500, bg='yellow')
canvas.pack(expand='yes', fill='both')
k = 1
j = 1
for i in range(0,26):
    canvas.create_oval(300 - k,250 - k,300 + k,250 + k, width=1)
    k += j
    j += 0.6
canvas.mainloop()
