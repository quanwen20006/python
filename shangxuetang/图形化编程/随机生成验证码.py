# _*_coding:utf-8 _*_
'''
验证码生成器
'''
import string
from tkinter import *
import random


class VerifyCodeGenerator(object):
    def __init__(self):
        window = Tk()
        window.title("验证码生成器")
        # 定义stringvar存取用户输入到组数
        self.chars = StringVar()
        self.groups = StringVar()
        self.chars.set(4)
        self.groups.set(10)

        frame = Frame()
        frame.pack(padx=5, pady=5)
        label1 = Label(frame, text="每组字符数")
        label2 = Label(frame, text="生成组数")
        entery1 = Entry(frame, textvariable=self.chars)
        entery2 = Entry(frame, textvariable=self.groups)
        label1.grid(row=1, column=1)
        entery1.grid(row=1, column=2)
        label2.grid(row=1, column=3)
        entery2.grid(row=1, column=4)

        Button(width=60, bg="green", text="生成", command=self.generator).pack(
            padx=(5, 5), pady=(0, 0))
        self.text = Text(width=70, height=20, bg="pink")
        # x y边距
        self.text.pack(padx=5, pady=5)
        window.mainloop()

    def generator(self):
        # 拿到用户entery输入到字符数和组数，然后生成
        groups = eval(self.groups.get())
        chars = eval(self.chars.get())
        # 生成验证码，并且插入文本域
        temp = []
        # mylist = []
        for i in range(groups):
            mysample = string.ascii_uppercase+string.digits
            mylist = random.sample(mysample, chars)
            temp.append("".join(mylist))
        ret = "-".join(temp)
        self.text.insert(END,ret+"\n")


if __name__ == "__main__":
    vg = VerifyCodeGenerator()
    result = vg.generator()
    print(result)
