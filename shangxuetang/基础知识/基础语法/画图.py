# _*_ coding:utf-8 _*_
# @time  : 2020/12/31 16:38
# @Author: quanwen
# @File  :
import turtle

def drarCirle():
    turtle.bgcolor("pink")
    turtle.screensize(1000,1000)
    # 显示箭头
    turtle.showturtle()
    # 设置画笔的宽度
    turtle.width(10)
    turtle.color("blue")
    turtle.circle(50)
    # 写字符串
    # turtle.write("全文")
    # 设置画笔的颜色
    turtle.penup()
    turtle.goto(120,0)
    turtle.color("yellow")
    # 放下笔
    turtle.pendown()
    turtle.circle(50)

    # 抬笔
    turtle.penup()
    turtle.goto(240, 0)
    turtle.color("black")
    # 放下笔
    turtle.pendown()
    turtle.circle(50)

    turtle.penup()
    turtle.goto(60, -50)
    turtle.pendown()
    turtle.color("green")
    # 放下笔
    turtle.pendown()
    turtle.circle(50)

    turtle.penup()
    turtle.goto(180, -50)
    turtle.color("red")
    # 放下笔
    turtle.pendown()
    turtle.circle(50)
    # 设置箭头的方向
    # turtle.left(90)
    # turtle.goto(0, 100)
    # turtle.mainloop()



if __name__ == '__main__':
    drarCirle()
    a = 123
    print(id(a))




