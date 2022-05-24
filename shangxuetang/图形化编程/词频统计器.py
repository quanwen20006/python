# _*_ coding:utf-8 _*_
from tkinter import *


class WordCount(object):
    def __init__(self):
        window = Tk()
        window.title("词频统计器")
        # 面板
        self.dirPath = StringVar()
        self.dirPath.set("请选择文件夹路径....")
        frame1 = Frame()
        frame1.pack()
        Entry(frame1,textvariable=self.dirPath,width=29).pack(side=LEFT)
        Button(frame1, text="选择文件夹",command=self.doCounter,width=10).pack(side=RIGHT)

        # 按钮
        Button(text="txt文件统计词频",width=40).pack(pady=10)

        # 面板
        frame2 = Frame()
        frame2.pack()
        self.text = Text(frame2,width=50,height=20,bg="pink")
        self.text.pack(side=LEFT)
        self.sb = Scrollbar(frame2)
        self.sb.pack(side=RIGHT,fill=Y,expand=True)

        window.mainloop()
    def doCounter(self):
        pass


if __name__ == '__main__':
    te =WordCount()