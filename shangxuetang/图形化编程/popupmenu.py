# _*_coding:utf-8 _*_
'''
弹出式菜单
'''

from tkinter import *

# 菜单监听函数


def onCheckSelected():
    print("被点击了")
    label["text"] = "change"

# 事件监听函数


def showPopupMenu(mouseEvent):
    print("展示右键菜单")
    popupMenu.post(mouseEvent.x_root, mouseEvent.y_root)


window = Tk()
window.title("弹出式窗口")

label = Label(text="右键", width=100, height=20)
label.pack()
popupMenu = Menu(tearoff=False)

popupMenu.add_command(label="手撕鸡", command=onCheckSelected)
popupMenu.add_command(label="啤酒鸭", command=onCheckSelected)
popupMenu.add_command(label="水煮鱼", command=onCheckSelected)
popupMenu.add_command(label="红烧肉", command=onCheckSelected)


label.bind(sequence="<Enter>", func=showPopupMenu)

# 消息窗口循环
window.mainloop()
