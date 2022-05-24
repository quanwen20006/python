# _*_coding:utf-8 _*_
'''
tkinter动画

功能：按Y键圆形变大，按其他键圆形变小

窗口和标题，
打包一个画布，在画布绑定鼠标事件和监听函数
消息循环
'''
from tkinter import *

radis = 50


def drwa_oval(radis):
    canvas.create_oval(50-radis, 50-radis, 150+radis, 150 +
                       radis, width=2, fill="red", tag="oval")


def bigger(event):
    print("keychar: ", event.char)
    print("keycode: ", event.keycode)
    global radis
    if(event.char == 'y'):
        print("希望原变大")
        canvas.delete("oval")
        radis += 5
        drwa_oval(radis)
    else:
        print("希望圆变小")
        canvas.delete("oval")
        radis -= 5
        drwa_oval(radis)


window = Tk()
window.title("tkinter动画")
canvas = Canvas(bg="#FFF", width=300, height=200)
canvas.pack()
# 画圆
drwa_oval(radis)
# 让画布获得焦点
canvas.focus_set()
# 画布绑定事件 绑定键盘事件
# canvas.bind(sequence="<Key>", func=bigger)
canvas.bind("<Key>", func=bigger)

window.mainloop()