# _*_coding:utf-8 _*_

from tkinter import Tk, Label, Button, Frame, Radiobutton, Checkbutton, Entry, Message, Text, IntVar, StringVar, END


def dealok():
    print("ok")


def dealcancel():
    print("cancel")


def tkinter_demo():
    # 创建窗口
    window = Tk()
    # 创建一个标签
    label = Label(window, text="lable1", foregroun="red", background="green")
    # 创建一个按钮,command是按钮响应函数
    btn_ok = Button(window, text="Ok", foreground="red", command=dealok)
    btn_cancel = Button(window, text="Cancel",
                        background="green", command=dealcancel)

    # 将标签打包到窗口
    label.pack()
    btn_ok.pack()
    btn_cancel.pack()
    # 消息循环（死循环，程序不退出，等候用户交互）
    window.mainloop()


class EatChickenWindow(object):
    def __init__(self):
        window = Tk()
        window.title("吃鸡窗口")

        frame1 = Frame(window)
        frame2 = Frame(window)
        frame1.pack()
        frame2.pack()
        self.cbValue = IntVar()
        cb = Checkbutton(frame1, text="Bold",
                         # 将variable的值存储值cbValue里面
                         variable=self.cbValue, command=self.cb)

        # 创建一个按钮,command是按钮响应函数
        # btn_ok = Button(window, text="Ok", foreground="red",
        #                 command=self.dealok)
        # btn_cancel = Button(window, text="Cancel",
        #                     background="green", command=self.dealcancel)

        self.rbValue = IntVar()
        self.rbValue.set(2)
        rb1 = Radiobutton(frame1, text="red", bg="red",
                          variable=self.rbValue, value=1, command=self.rb)
        rb2 = Radiobutton(frame1, text="yellow", background="yellow",
                          variable=self.rbValue, value=2, command=self.rb)
        rb3 = Radiobutton(frame1, text="green", background="green",
                          variable=self.rbValue, value=3, command=self.rb)

        # 表格布局，不必pack
        cb.grid(row=1, column=1)
        rb1.grid(row=1, column=2)
        rb2.grid(row=1, column=3)
        rb3.grid(row=1, column=4)

        # 创建一个标签
        label = Label(frame2, text="Enter you name",
                      foregroun="red", background="green")
        # 输入框及数据绑定
        self.entryValue = StringVar()
        enter = Entry(frame2, textvariable=self.entryValue)

        # message
        btnGet = Button(frame2, text="Get Name", command=self.BtnGet)
        message = Message(frame2, text="Message")
        label.grid(row=1, column=1)
        enter.grid(row=1, column=2)
        btnGet.grid(row=1, column=3)
        message.grid(row=1, column=4)
        text = Text(window, width=50, height=10)
        text.insert(END, "ABCD")
        text.insert(END, "1234")
        text.insert(END, "0000")
        text.pack()
        window.mainloop()

    def IntVar(self):
        pass

    def cb(self):
        print("cb")

    def BtnGet(self):
        print("btn get")

    def rb(self):
        print("rbValue: ", self.rbValue.get())
        print("rb")


if __name__ == "__main__":
    # tkinter_demo()
    EatChickenWindow()
