# _*_coding:utf-8 _*_
'''
python文件操作
'''
import pickle
from tkinter import filedialog
import os
import time
# os.mkdir("path")  # 创建目录
# os.makedirs("path")  # 创建目录（可创建多级不存在的目录）
# 增加目录
if os.path.exists("test"):
    print("exists")
else:
    os.mkdir("test")
os.makedirs("./test/test1/test2/test3")
time.sleep(2)

# 删

# os.remove("./test/1.txt")
# os.rmdir("./test/test1/test2")
os.removedirs("./test/test1/test2/test3")


# 查
print("文件是否存在：", os.path.isfile("../../day4/__init__.py"))
print("目录是否存在：", os.path.exists("../../day4/__init__.py"))


'''
文件的读写
'''
f = open('模块.py', mode='r+', encoding='utf-8')
print(f.read())
f.write(str(time.time()))
f.close()

# 文档遍历
with open("正则表达式.py", mode='r', encoding="utf-8") as f:
    result = f.readlines()
    for i in result:
        print("result: ", i)

'''
字节读写模式
'''

fb = open("s90.jpg", mode="rb")
t = fb.read()
fb.close()
if (os.path.exists("s90-bak.jpg")):
    os.remove("s90-bak.jpg")
    time.sleep(1)
fb1 = open("s90-bak.jpg", mode="xb")
fb1.write(t)
fb1.close()


# 可视化打开和存储文件
# tkinter.fileDialog.askopenfilename()
# tkinter.fileDialog.asksaveasfilename()

# 二进制io存
# pickle
py_obj = [0, 1, 3, "test", {"key1": "value1"}]
# src_file = filedialog.asksaveasfilename()
# src_f = open(src_file, mode="xb")
with open(filedialog.asksaveasfilename(), mode="xb") as f:
    pickle.dump(py_obj, f)

# 二进制io取
with open(filedialog.askopenfilename(), mode="rb") as f:
    print(pickle.load(f))
