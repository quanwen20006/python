# _*_ coding:utf-8 _*_
# @time  : 2020/8/2 15:00
# @Author: quanwen
# @File  :
import requests
import re

# re.mathch -- 从第一个字符开始匹配
content = 'hello 123 456 789 world'
result = re.match('^hello .* world$',content)
print('result: ',result.group())

# group 即匹配模式里面的第一个括号里面的内容
result1 = re.match('^hello\s(\d+).* world$',content)
print('result1: ',result1.group(1))

# 贪婪匹配（匹配尽可能多的字符）
result2 = re.match('^hello.*(\d+).* world$',content)
print('result2: ',result2.group(1))

# 非贪婪匹配--使用问号（匹配前面的内容0次或者1次）
result3 = re.match('^hello.*?(\d+).* world$',content)
print('result3: ',result3.group())

# 匹配模式--匹配模式 re.S(有换行符情况下使用)
content1 = '''hello 1234567 world 
          demo'''
result4 = re.match('^hello.*?(\d+).*demo$',content1,re.S)
print('result4: ',result4)


# 转义--特殊字符
content2 = 'price is $5.00'
result5 = re.match('price is \$5\.00',content2)
print('result5: ',result5)

# re.search（扫描整个字符串，返回第一个成功的匹配）
content3 = 'Whenever you need me， 124342424 in trouble， 87878 always near。Whenever you feel alone， and you think everyone has given up。。。Reach out for me， and I will give you my everlasting love'
result6 = re.search('you.*?(\d+).*love$',content3)
print('result6: ',result6)

html = '''
<div id="song">
<h2>经典老歌</h2>
<p>经典老歌列表</p>
<ul>
<li data-view="2">a</li>
<li data-view="3">
    <a href="/3.mp3" singer="张学友">情书</a>
</li>
<li data-view="3">
    <a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="4" class="active">
    <a href="/3.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="5"><a href="/3.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="6">e</li>
</ul>
</div>
'''

# result7 = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
result7 = re.search('<li.*?singer="(.*?)">(.*?)</a>',html,re.S)
result7 = re.search('<li.*?singer="(.*?)">(.*?)</a>',html)

if result7:
    print('result7: ', result7.group(1), result7.group(2))

html1 = '''
<div id="song">
<h2>经典老歌</h2>
<p>经典老歌列表</p>
<ul>
<li data-view="2">一路上有你</li>
<li data-view="3">
    <a href="/1.mp3" singer="张学友">情书</a>
</li>
<li data-view="4">
    <a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="5" class="active">
    <a href="/34.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="6"><a href="/3.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="7">换到千般恨</li>
</ul>
</div>
'''
# findall 搜索字符串，以列表形式返回全部能匹配的子串
result8 = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html1,re.S)
result8 = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>',html1,re.S)
if result8:
    for song in result8:
        print('result8: ', song[1])

# sub 替换字符串中每一个匹配的子串后，返回替换后的字符串
content4 = 'Extra stings Hello 1245676 World_this is a Regex Demo Extra stings'
result9 = re.sub('\d+','---',content4)
# 替换字符串同时包括原来的字符串，注意点
# 1：正则匹配的时候需要加上group即小括号
# 2：在替换字符中加上 r \1
result9 = re.sub('(\d+)',r'\1 ---',content4)
print(result9)

# 查找歌名
result10 = re.sub('<a.*?>|</a>','',html1)
print('result10: ',result10)
result10 = re.findall('<li.*?>(.*?)</li>',result10,re.S)
print('result10: ',result10)
for song in result10:
    print('song: ',song.strip())

# compile 将正则字符串编译成正则表达式对象
content5 = "Hello 1245676 World_this is a Regex Demo"
pattern = re.compile('Hello.*Demo',re.S)
result11 = re.match(pattern,content5)
result11 = re.match('Hello.*Demo',content5,re.S)
print('result11: ',result11)

# 实战 ---- 使用正则表达式，抓取豆瓣图书书本的信息
douban = requests.get('https://book.douban.com/')
print('douban: ',type(douban))