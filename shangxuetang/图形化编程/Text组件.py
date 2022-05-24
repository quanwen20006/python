# _*_ coding:utf-8 _*_
# @time  : 2021/2/2 12:29
# @Author: quanwen
# @File  :

from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.textV = StringVar()

        self.pack()
        self.createWidget()

    def createWidget(self):
        self.text = Text(self,width=40,height=12,bg='pink')
        self.text.pack()

        # 根据下标插入数据
        self.text.insert(1.0, '1测试数据---')
        self.text.insert(2.4, '2测试数据---')

        self.btn = Button(self,text='确定', bg='red', width=4,command = self.console)
        self.text.window_create(INSERT, window=self.btn)
        self.btn.pack()

    def console(self):
        # print('文本框的值是：{0}'.format(self.textV))

        text_content = self.text.get("0.0","end")
        print('11111 ', text_content)



if __name__ == '__main__':
    root = Tk()
    root.geometry('400x400+100+100')
    app = Application(root)
    root.mainloop()