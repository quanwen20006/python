# _*_coding:utf-8 _*_

'''
使用画布进行绘制
'''
from tkinter import Tk, Canvas, Label, Button, Frame, Radiobutton, Checkbutton, Entry, Message, Text, IntVar, StringVar, END


def drawRect():
    canvas.create_rectangle(10, 10, 200, 150, fill="red",
                            width=3, activefill="yellow", tag="rect")


def drawArc():
    canvas.create_arc(10, 10, 200, 150, fill="green",
                      width=3, activefill="yellow", tag="arc")


def drawOval():
    canvas.create_oval(10, 10, 200, 150, fill="green",
                       width=3, activefill="yellow", tag="oval")


def drawLine():
    canvas.create_line(10, 10, 200, 150, 250, 250, fill="green",
                       width=3, activefill="blue", arrow="last", tag="line")


def drawPoly():
    canvas.create_polygon(10, 10, 200, 150, 10, 150, fill="green",
                          width=3, activefill="pink", tag="poly")

# 清空canvas


def clearAll():
    canvas.delete("poly", "line", "oval", "arc", "rect")


window = Tk()
window.title("画布与绘制")

# 打包画布到window
canvas = Canvas(window, bg="#FFF")
canvas.pack()

# 打包面板到window
frame = Frame()
frame.pack()
# 创建一个按钮到面板，监听drawRect
btnWidth = 10
btnRect = Button(frame, text="矩形", command=drawRect, width=btnWidth)
btnOval = Button(frame, text="椭圆", command=drawOval, width=btnWidth)
btnArc = Button(frame, text="弧形", command=drawArc, width=btnWidth)
btnLine = Button(frame, text="线段", command=drawLine, width=btnWidth)
btnPoly = Button(frame, text="多边形", command=drawPoly, width=btnWidth)
btnClear = Button(frame, text="清空", command=clearAll, width=btnWidth)

# 布局
btnRect.grid(row=1, column=1)
btnOval.grid(row=1, column=2)
btnArc.grid(row=1, column=3)
btnLine.grid(row=2, column=1)
btnPoly.grid(row=2, column=2)
btnClear.grid(row=2, column=3)
# 窗口消息循环
window.mainloop()
