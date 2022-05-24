# _*_coding:utf-8 _*_
'''
使用tkinter实现跑马灯效果
'''
from tkinter import *

x = 160
dx = 5


def draw_text():
    print("x: ", x)
    canvas.create_text(x, 100, text="学python，得永生", tag="text")


window = Tk()
window.title("thinter跑马灯")

canvas = Canvas(bg="#FFF", width=400, height=300)
canvas.pack()

draw_text()

while True:
    # 画布等待100毫秒
    canvas.after(100)
    # 画布移动得对象（移动的是text属性值），及step
    canvas.move("text", dx, 0)
    x += dx
    print('x: {0} --- dx: {1}: '.format(x, dx))
    canvas.update()
    if x > int(canvas["width"]):
        print('---- ', canvas["width"])
        canvas.delete("text")
        x = 0
        draw_text()

window.mainloop()
