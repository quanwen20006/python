# _*_coding:utf-8 _*_

from tkinter import *


def onAddSelected():
    print("selected")


window = Tk()
window.title("熟悉Tkinter使用图片")
# 把menu配置到window
menubar = Menu(window)
window.config(menu=menubar)
# 将tearoff设置为1以后，就是表明这个菜单是可以独立出来的，如果是0的话就不可以独立出来
menuOper = Menu(menubar, tearoff=0)
menuExit = Menu(menubar, tearoff=1)
# add_cascade 的一个很重要的属性就是 menu 属性，它指 明了要把那个菜单级联到该菜单项上，
# 当然，还必不可少 的就是 label 属性，用于指定该菜单项的名称
menubar.add_cascade(label="操作", menu=menuOper)  # 含有子菜单
menubar.add_cascade(label="退出", menu=menuExit)

# 给菜单增加子菜单
menuOper.add_command(label="Add", command=onAddSelected)
menuOper.add_command(label="Substract")
menuOper.add_command()
menuOper.add_command(label="Multiply")
menuOper.add_command(label="Divide")


menuExit.add_command(label="Quit", command=window.quit)
frame1 = Frame()
frame1.pack()

canvas = Canvas(frame1, bg="#FFF", width=400, height=400)
label = Label(frame1, text="标签")
canvas.pack(side=LEFT)
label.pack(side=LEFT)

frame2 = Frame()
frame2.pack()
Button(frame2, text="按钮1").pack(side=LEFT)
Button(frame2, text="按钮2").pack(side=LEFT)


img1 = PhotoImage(file="1.gif")
img2 = PhotoImage(file="2.gif")
img3 = PhotoImage(file="3.gif")
canvas.create_image(200, 200, image=img1)
canvas.create_image(10, 10, image=img2)
canvas.create_image(10, 10, image=img3)
window.mainloop()
