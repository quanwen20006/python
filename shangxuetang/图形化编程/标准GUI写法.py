# _*_ coding:utf-8 _*_
# @time  : 2021/2/1 00:19
# @Author: quanwen
# @File  :
'''
使用面向对象编写GUI程序
'''
from tkinter import *
from tkinter.messagebox import askyesno

class Application(Frame):
    '''使用面向对象编写GUI程序'''
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack() # 通过布局管理器显示
        self.createWidget()

    def createWidget(self):
        '''创建组件'''
        self.btn01 = Button(self,width=10, height=3, text="点击按钮",command=self.console)
        # 设置按钮的位置，使用e n s w（东南西北来标记且可以组合）
        self.btn01['anchor']=NE
        self.btn01.pack()

        global photo
        photo = PhotoImage(file='imgs/b1.gif')
        # state表示按钮的状态是否为可点击
        self.btn02 = Button(self, image=photo, state=DISABLED, command=self.console)
        self.btn02.pack()

        # 创建退出按钮
        self.btnQuit = Button(self,text="退出",command=self.quit)
        self.btnQuit.pack()
        # bg背景色 fg 文字的颜色
        self.label = Label(self,text="Label", width=10,bg='black',fg='red')
        self.label.pack()

        self.label1 = Label(self,text="Label学习", height=1, width=10, bg='green', fg='pink',font=("宋体",22))
        self.label1.pack()

        # 显示多行文本  relief 3d效果 justify 文本显示效果
        self.label3 = Label(self,text='多行文本\n多行文本1111\n多行文本22222',borderwidth=3, relief='groove',justify='right')
        self.label3.pack()

        # 显示图像
        global photo1 # 申明成全局变量，不然方法执行完毕后，局部变量图像对象销毁
        photo1 = PhotoImage(file='imgs/b1.gif')
        self.label2 = Label(self,image=photo1)
        self.label2.pack()

    def console(self):
        print('按钮被调用----')

    def quit(self):
        ans = askyesno(title='Warning',message='确认是否关闭窗口')
        if ans:
            self.master.destroy()
        else:
            return


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x400+200+200")
    root.title("测试Label")
    app = Application(master=root)
    root.mainloop()
