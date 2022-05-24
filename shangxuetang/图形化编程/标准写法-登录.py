# _*_ coding:utf-8 _*_
# @time  : 2021/2/2 12:29
# @Author: quanwen
# @File  :

from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.passwd = StringVar()
        self.user = StringVar()
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.userLabel = Label(self,text='用户名：',width=20,bg='pink',borderwidth=4)
        self.userLabel.pack()

        self.userInput = Entry(self,bg='white',width=20,textvariable = self.user)
        self.userInput.pack()

        self.passLabel = Label(self, text='密  码：', width=20, bg='pink', borderwidth=4)
        self.passLabel.pack()
        # 绑定密码输入框的值到passwd变量
        self.passInput = Entry(self, bg='white', width=20,textvariable = self.passwd)
        self.passInput.pack()

        self.loginBtn = Button(self, text='确定', bg='white', width=4,command = self.console)
        self.loginBtn.pack()

    def console(self):
        print('用户名： {0} 密 码：{1}'.format(self.user.get(),self.passwd.get()))


if __name__ == '__main__':
    root = Tk()
    root.geometry('400x400+100+100')
    app = Application(root)
    root.mainloop()