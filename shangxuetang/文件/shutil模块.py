# _*_ coding:utf-8 _*_
# @time  : 2021/1/23 23:42
# @Author: quanwen
# @File  :
'''
    主要是用来对文件进行拷贝，压缩，移动，删除等
'''
import shutil
import zipfile
import os

# 文件拷贝
shutil.copyfile('./Hotel California.txt','./Hotel California-new.txt')
# 目录完整拷贝
if os.path.isdir('./temp-new') and os.path.isdir('./temp-bak'):
    print('目录存在--删除')
    shutil.rmtree('./temp-new')
    shutil.rmtree('./temp-bak')
shutil.copytree('./temp','./temp-new',ignore=shutil.ignore_patterns('*.txt','*.html'))

# 压缩和解压--把temp目录压缩到temp目录，压缩文件名是2.zip
# shutil.make_archive('./temp/2','zip','./temp')

# zip 压缩
z1 = zipfile.ZipFile('temp.zip','w')
z1.write('./temp/1.txt')
z1.write('./temp/1.py')
z1.close()
# zip解压
z2 = zipfile.ZipFile('temp.zip','r')
z2.extractall('./temp-bak')
z2.close()




