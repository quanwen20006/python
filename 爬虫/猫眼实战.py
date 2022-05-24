# _*_ coding:utf-8 _*_
# @time  : 2020/8/23 10:36
# @Author: quanwen
# @File  :
import json
from multiprocessing import Pool

import requests
from requests.exceptions import RequestException
import re

def get_one_page(url):
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
    try:
        response = requests.get(url,headers=header)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?'
                         +'releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)

    items = re.findall(pattern,html)
    # 把items的数组格式化为字典,返回的是一个生成器对象
    for item in items:
        yield {
            'index':item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time':item[4].strip()[5:],
            'score':item[5]+item[6]
        }
def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        # json.dumps序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii = False
        f.write(json.dumps(content,ensure_ascii=False) + '\n')
        f.close()

def main(offset):
    url = 'https://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    # for i in range(10):
    #     main(i*10)
    # 多线程
    pool = Pool()
    pool.map(main,[i*10 for i in range(10)])
