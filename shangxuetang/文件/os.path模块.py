# _*_ coding:utf-8 _*_
# @time  : 2021/1/23 22:57
# @Author: quanwen
# @File  :
'''
os.path 提供了目录相关的操作
'''
import os
import os.path

###########判断：绝对路径，是否目录 目录、文件是否存在##################
print('是不是绝对路径：',os.path.isabs('./temp'))
print('是不是目录：',os.path.isdir('./temp'))
print('是不是文件：',os.path.isfile('./temp'))
print('目录是否存在：',os.path.exists('./temp'))

##########获得文件基本信息##################
print('文件大小：',os.path.getsize('./Hotel California.txt'))
print('绝对路径：',os.path.abspath('./Hotel California.txt'))
print('目录名：',os.path.dirname('./Hotel California.txt'))
print('返回最文件修改时间：{0} 返回文件path创建时间：{1}'.format(os.path.getmtime('./Hotel California.txt'),os.path.getctime('./Hotel California.txt')))

##########对路径对操作##################
path = os.path.abspath('./Hotel California.txt')
print('path ',path,os.path.split(path),os.path.splitext(path))
print(os.path.join('a','b','c'))

# 输出工作目录下对所以py文件，并输出文件名
path = os.getcwd()
path = os.path.join(path,'temp')

for t in os.listdir(path):
    if t.endswith('.py'):
        print('python文件: ',t[:len(t)-3])

# 使用列表推导式
filelist = [filename for filename in os.listdir(path) if filename.endswith('.py')]
print('filelist: ',filelist)


# 使用os.walk()遍历
'''
返回包含3个元素对元组（dirpath,dirnames,filenames）
'''
filelist1 = (filename for filename in os.walk(path) if filename.endswith('.py'))
print('filelist1: ',filelist1)
for fl in filelist1:
    print('fl: ',fl)

