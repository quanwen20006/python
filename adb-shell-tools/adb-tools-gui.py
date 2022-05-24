from tkinter import *

root = Tk()
root.title('abd shell工具简化版')
root.geometry('600x600')
# 禁止窗口拖动
root.resizable(width=False, height=False)

frame = Frame(root)
frame.pack(padx=8, pady=8, ipadx=4)

lbTitle = Label(frame, text='请在下方输入包名就可以进行App性能指标监测')
lbTitle.grid(row=0, column=0, sticky=W, columnspan=4)

labPackage = Label(frame, text="包名: ")
labPackage.grid(row=1, column=0, sticky='w')
# 绑定对象到Entry
var = StringVar()
inp1 = Entry(frame, textvariable=var)


def getPackageName():
    return inp1.get()


inp1.grid(row=1, column=1, sticky='w')
lbStartBtn = Button(frame, text='开始', command=getPackageName)
lbStartBtn.grid(row=1, column=2, sticky='w')

lbStopBtn = Button(frame, text='停止')
lbStopBtn.grid(row=1, column=3, sticky='w')

text = Text(root)
text.place(relx=0, rely=0.3, relwidth=1, relheight=1)
text.insert(INSERT, "text.get()")


# packageName = text.get()
# print('包名: ', packageName)
root.mainloop()

