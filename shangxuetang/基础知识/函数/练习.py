# _*_ coding:utf-8 _*_
# @time  : 2021/1/18 17:32
# @Author: quanwen
# @File  :
'''
LEGB是指python搜索变量的顺序

Local      局部变量
Enclosed   嵌套函数的变量
Global     全局变量
Built in   python内置变量
'''
import random
import turtle

# 编写一个函数，实现反向输出一个整数
def reverseOutPut():
    inp = input('请输入一个数字:')
    print('inp: ',inp[::-1])

# 输入一个毫秒数，将该数据换算成 小时、分钟、秒数
def getHours():
    inp = eval(input('请输入一个数字:'))
    s = int(inp/1000)
    m,h = int(s/60),int(s/3600)
    print('秒数：{0},分钟数：{1}，小时数：{2} '.format(s,m,h))

# 使用海龟画图，输入多个点，将这些点，两两相连
def drawLine():
    num = eval(input('请输入点的数量：'))
    points = []
    while num>0:
        point = eval(input('请输入点的x,y值：'))
        points.append(point)
        num -= 1

    t = turtle.Pen()
    colors=['black','green','pink']
    t.penup()
    for i in points:
        t.pendown()
        color_tmp = colors[random.randint(0,len(colors)-1)]
        t.color(color_tmp)
        t.goto(i)
    t.goto(points[0])
    # 画图完成
    turtle.done()


if __name__ == '__main__':
    # reverseOutPut()
    # getHours()
    drawLine()