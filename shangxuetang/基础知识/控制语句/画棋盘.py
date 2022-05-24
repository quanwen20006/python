# _*_ coding:utf-8 _*_
# @time  : 2021/1/11 21:09
# @Author: quanwen
# @File  :

'''
画一个18*18的棋盘
'''

import turtle
t = turtle.Pen()
t.speed(0)
step = 20
times = 18
width = 180
height = 180
for i in range(times+1):
    t.penup()
    t.goto(-width,height-step*i)
    t.pendown()
    t.fd(width*2)  #画直线

t.left(-90)
for i in range(times+1):
    t.penup()
    t.goto(-width+step*i,height)
    t.pendown()
    t.fd(width*2)

turtle.done()