# _*_ coding:utf-8 _*_
# @time  : 2020/12/31 22:22
# @Author: quanwen
# @File  :
import turtle
import math

x1,y1 = 100,100
x2,y2 = 100,0
x3,y3 = -100,0
x4,y4 = -100,100

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)

distance = math.sqrt((x1-x4)**2+(y1-y4)**2)
print('距离是： ',distance)

turtle.mainloop()
