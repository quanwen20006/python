# _*_coding:utf-8 _*_
'''
作一个文本域和滚动条
'''

from tkinter import *

window = Tk()
window.title("文本域和滚动条")
# 打包滚动条到右侧窗口
scrollball = Scrollbar(window, width=20)
scrollball.pack(side=RIGHT, fill=Y, expand=True)


text = Text(bg="white", width=400, height=20)
# 打包文本域到窗口左侧
text.pack(fill=BOTH, expand=False)
# 滚动条和文本域到双向关联
scrollball.config(command=text.yview)  # 将滚动条到y滚动事件交给文本域到yview
text.config(yscrollcommand=scrollball.set)
window.mainloop()
