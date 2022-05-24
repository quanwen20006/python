# _*_coding:utf-8 _*_
'''
房贷计算器
'''
from tkinter import *


class FangDai(object):
    def __init__(self):
        window = Tk()
        # 设置窗口的大小及离原点的距离 宽度x高度 距离原点的x距离（正值为距离左边的位置），最后一个值y的距离
        window.geometry("300x300+100+200")
        window.title("房贷计算器")

        self.lilv = StringVar()
        self.money = StringVar()
        self.years = StringVar()
        self.month = StringVar()
        self.total = StringVar()

        frame = Frame()
        frame.pack()
        label1 = Label(frame,text="贷款金额")
        entery1 = Entry(frame, textvariable=self.money)
        label1.grid(row=1, column=1)
        entery1.grid(row=1, column=2)

        label2 = Label(frame, text="年化利率")
        entery2 = Entry(frame, textvariable=self.lilv)
        label2.grid(row=2, column=1)
        entery2.grid(row=2, column=2)

        label3 = Label(frame, text="贷款年限")
        entery3 = Entry(frame,textvariable=self.years)

        label3.grid(row=3, column=1)
        entery3.grid(row=3, column=2)

        label4 = Label(frame, text="每月还款")
        self.entery4 = Label(frame)
        label4.grid(row=4, column=1)
        self.entery4.grid(row=4, column=2)

        label5 = Label(frame, text="还款总计")
        self.entery5 = Label(frame)
        label5.grid(row=5, column=1)
        self.entery5.grid(row=5, column=2)

        Button(text="计算",width=28,command=self.count).pack(pady=5)

        window.mainloop() # 调用组件的mainloop 进入事件循环

    def count(self):
        month_money=eval(self.money.get())*(eval(self.lilv.get())/12)/(1-(1/(1+eval(self.lilv.get())/12)*eval(self.years.get())))
        money_total = month_money*eval(self.years.get())*12
        self.entery4["text"] = abs(money_total)
        self.entery5["text"] = abs(month_money)

if __name__ == '__main__':
    fd = FangDai()