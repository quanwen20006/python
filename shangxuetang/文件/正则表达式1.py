# _*_ coding:utf-8 _*_
# @time  : 2020/7/2 08:10
# @Author: quanwen
# @File  :
'''
正则表达式特殊字符
1：^ $ *?+{2}{2,}{2,5} |
2：[] [^] [a-z] .
3：\s \S \w \W
4：[\u4E00-\u9FA5] () \d
'''


import  re
line = 'teeeeestt12tt3tt2tdemon20200702'
# line='t112'
# 匹配以t开头的字符串
# 点号匹配一个字符  ^匹配以什么开头 t开头的字符 *号匹配一个或多个 $匹配以什么字符结尾
regex_str = '.*?(^t.*?2).*'
match_obj = re.match(regex_str,line)
if match_obj:
    print('yes',match_obj.group(1))
else:
    print('no')

# ? 需求  匹配字符串 t***t
# 匹配t到t的字符串第一组字符串--不加？是贪婪模式，从右往左搜索(反向匹配)，加了？就从左往右搜索
# 贪婪模式是持续匹配，非贪婪模式就是匹配出现的第一次
regex_str1 = '.*?(t.*?t).*'
line1 = 'ateeeeestt12tt3tt2ttxtttdemon20200702'
match_obj = re.match(regex_str1,line1)
if match_obj:
    print(match_obj.group(1))
else:
    print('no')

# + 号使用
regex_str1 = '.*(t.+t).*'
line1 = 'ateeeeestt12tt3tt2ttxta1tdemon20200702'
match_obj = re.match(regex_str1,line1)
if match_obj:
    print('+号的使用： ',match_obj.group(1))
else:
    print('no')

# {} 匹配前面一个字符出现的次
regex_str1 = '.*?(t.{2,3}t).*'
line1 = 'ateeeeestt12tt3tt2ttxta613tdemon20200702'
match_obj = re.match(regex_str1,line1)
if match_obj:
    print('{} 的使用: ',match_obj.group(1))
else:
    print('no')

# | 或
regex_str1 = '.*(t12t|ta613t).*'
line1 = 'ateeeeestt12tt3tt2ttxta613tdemon20200702'
match_obj = re.match(regex_str1,line1)
if match_obj:
    print('| 的使用: ',match_obj.group(1))
else:
    print('no')

# []使用 中括号里面的任意字符
regex_str1 = '.*?([abcd]t.*?t).*'
line1 = 'ateeeeestt12tt3tt2ttxata613tttademon20200702'
match_obj = re.match(regex_str1,line1)
if match_obj:
    print('[] 的使用: ',match_obj.group(1))
else:
    print('no')

# 提取电话号码
phone = '18589009234'
phone1 = '1.589009234'
regex_str1 = '(1[8354][0-9]{9})'
regex_str2 = '(1[8354][^1]{9})'
regex_str3 = '(1[.][^1]{9})'
match_obj = re.match(regex_str1,phone)
match_obj1 = re.match(regex_str2,phone)
match_obj2 = re.match(regex_str3,phone1)
if match_obj:
    print('[区间] 的使用: ',match_obj.group(1))
else:
    print('no')

if match_obj1:
    print('[区间^的使用--不能出现的字符] 的使用: ',match_obj1.group(1))
else:
    print('no')

if match_obj2:
    print('[中括号点号的作用-在中括号中的点号无特殊意义] 的使用: ',match_obj2.group(1))
else:
    print('no')


# \s 匹配任何不可见字符 \S 匹配任何可见字符
# \w 匹配包括下划线的任何单词字符  \W 匹配任何非单词字符
# [\u4E00-\u9FA5] 提取中文
string = 'hello world'
string1 = 'study in 北京大学123'
regex_str = '(hello\sw.*)'
regex_str1 = '(he\S+o.*)'
regex_str2 = '.*?([\u4E00-\u9FA5]+)'
match_obj = re.match(regex_str,string)
match_obj1 = re.match(regex_str1,string)
match_obj2 = re.match(regex_str2,string1)
if match_obj:
    print('\s的使用: ',match_obj.group(1))
else:
    print('no')

if match_obj1:
    print('\S的使用: ',match_obj1.group(1))
else:
    print('no')

if match_obj2:
    print('[\u4E00-\u9FA5]的使用: ',match_obj2.group(1))
else:
    print('no')

# \d代表是数字
line='出生于2003年'
reg_str = '.*?(\d+).*'
match_obj = re.match(reg_str,line)
if match_obj:
    print('\d的使用: ',match_obj.group(1))
else:
    print('no')


# 实践
line = 'XXX出生于2001年06月2日'
# line = 'XXX出生于2001/6/2/'
# line = 'XXX出生于2001-6-2'
# line = 'XXX出生于2001-06'
# line = 'XXX出生于2001-06月'

reg_str = '.*出生于(\d{4}[年/-]\d{1,2}([月/-]$]|[月/-]$|$|[月/-]\d{1,2}[日]|[月/-]\d{1,2}))'
match_obj = re.match(reg_str,line)
if match_obj:
    print('综合实践---',match_obj.group(1))
else:
    print('综合实践---','no')
