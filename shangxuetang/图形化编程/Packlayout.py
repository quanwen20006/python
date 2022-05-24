# _*_coding:utf-8 _*_

from tkinter import *

window = Tk()
window.title("测试布局")

Label(text="红", bg="red").pack()
# fill填充，在纵向横向填充，需要配合expand一起用
Label(text="绿", bg="green").pack(fill=BOTH, expand=True)
Label(text="蓝", bg="blue").pack(side=RIGHT)


window.mainloop()
