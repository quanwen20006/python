# _*_coding:utf-8 _*_
'''
tkinter的事件处理
'''
from tkinter import *


def processKeyEvent(event):
    print("keysym: ", event.keysym)
    print("keychar: ", event.char)
    print("keycode: ", event.keycode)


window = Tk()
window.title("tkinter事件处理")

canvas = Canvas(window, width=100, height=100, bg="white")
# 让画布获得焦点
canvas.focus_set()
canvas.pack()

# 绑定鼠标键盘事件，func为处理函数
canvas.bind(sequence="<Key>", func=processKeyEvent)

window.mainloop()
