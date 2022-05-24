# _*_coding:utf-8 _*_

'''
打开指定文件，并且删除文件里面的指定内容
'''

from tkinter import filedialog

'''
选择一个文件，然后删除文件出现的字符
'''


def replaceKeyword():
    file_name = filedialog.askopenfilename()
    result = ""
    with open(file_name, mode='r', encoding='utf-8') as f:
        temp = input("请输入需要替换的字符")
        result = f.read().replace(temp, "")

    with open(file_name, mode='w', encoding='utf-8') as f:
        f.write(result)


'''
统计文件中出现的字符数，行数，多少个单词
'''


def countInfo():
    file_name = filedialog.askopenfilename()
    words = 0
    lines = 0
    strings = 0
    with open(file_name, mode='r', encoding='utf-8') as f:
        line_list = f.readlines()
        lines = len(line_list)
        print("lines: ", lines)
        for line in line_list:
            words += len(line.split(" "))
            strings += len(line)
        print("words: %d strings: %d" % (words, strings))


'''
图形化选择一个文件，然后把每字节加5，然后将结果写入新文件
'''
def md5():
    src_file = filedialog.askopenfilename()
    dis_file = filedialog.asksaveasfilename()
    dataBytes = bytearray()
    with open(src_file, mode='rb')as f:
        bytes_ = f.read()
        for b in bytes_:
            if b > 250:
                b -= 251
            else:
                b += 5
            dataBytes.append(b)
    with open(dis_file, mode='xb') as f:
        f.write(dataBytes)


def md5_re():
    src_file = filedialog.askopenfilename()
    dis_file = filedialog.asksaveasfilename()
    dataBytes = bytearray()
    with open(src_file, mode='rb')as f:
        bytes_ = f.read()
        for b in bytes_:
            if b < 5:
                b += 251
            else:
                b -= 5
            dataBytes.append(b)
    with open(dis_file, mode='xb') as f:
        f.write(dataBytes)


if __name__ == "__main__":
    # replaceKeyword()
    # countInfo()
    md5()
    # md5_re()
