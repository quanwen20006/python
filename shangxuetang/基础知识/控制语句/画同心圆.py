# _*_ coding:utf-8 _*_
# @time  : 2021/1/11 20:36
# @Author: quanwen
# @File  :

'''
画同心圆且每个圆的线条颜色不一致
'''

import turtle
my_colors = ('red','gray','pink','green','orange')
t = turtle.Pen()
t.width(2)
t.speed(0)
for i in range(30):
    t.penup()
    t.goto(0,-4*i)
    t.pendown()
    t.color(my_colors[i%len(my_colors)])
    t.circle(10+4*i)
turtle.done() # 程序执行完毕，窗口保留

